from torchvision.models import resnet50, ResNet50_Weights
from flask import Flask, request, jsonify
from PIL import Image, ImageDraw
import torchvision.transforms as transforms
import torch
import gpustat
import queue
import threading
import time
from concurrent.futures import ThreadPoolExecutor

app = Flask(__name__)

# Alpha increment value
ALPHA_INCREMENT = 0.1

# Function to calculate priority value for a task
def calculate_priority(C, O, T, W, alpha):
    return (W + O + T - C) + alpha

# Function to get available GPU memory
def get_gpu_memory():
    gpu_stats = gpustat.GPUStatCollection.new_query()
    gpu_memory = gpu_stats.jsonify()["gpus"][0]["memory.used"]
    return gpu_memory

# Initialize priority queue
task_queue = queue.PriorityQueue()

# Initialize ThreadPoolExecutor
executor = ThreadPoolExecutor(max_workers=4)  # Adjust max_workers as needed

# Function to execute tasks in the queue
def execute_queued_tasks():
    results = []
    while not task_queue.empty():
        priority, task = task_queue.get()
        image_path, task_type, task_number = task
        result = executor.submit(execute_task, image_path, task_type, task_number, priority)
        results.append(result.result())  # Collect the result of each task
    return results

# Function to add tasks to the queue
def add_tasks_to_queue(data):
    results = []
    # Get available GPU memory
    C = get_gpu_memory()  # Total GPU memory available

    # Enqueue tasks into the priority queue
    for image_info in data['images_data']:
        image_path = image_info.get('image_path')
        task_type = image_info.get('task_type')
        task_number = image_info.get('task_number')
        offloading_time = image_info.get('offloading_time', 1)
        initial_priority = image_info.get('initial_priority', 10)

        # Calculate priority for the task
        current_time = time.time()
        elapsed_time = current_time - data.get('timestamp', current_time)
        alpha = elapsed_time * ALPHA_INCREMENT  # Update alpha based on elapsed time
        W = initial_priority  # Weight of computation of task
        T = 1 if task_type == 'object_detection' else 2
        priority = calculate_priority(C, offloading_time, T, W, alpha)

        # Enqueue task with priority
        task_queue.put((priority, (image_path, task_type, task_number)))

    # Start executing queued tasks
    results = execute_queued_tasks()
    return results

# Route to receive requests
@app.route('/process_images', methods=['POST'])
def process_images_endpoint():
    data = request.json
    if not data:
        return jsonify({"error": "No JSON data received"}), 400

    # Add tasks to the queue
    results = add_tasks_to_queue(data)

    return jsonify({"status": "Tasks received and added to the queue", "results": results}), 200

def execute_task(image_path, task_type, task_number, priority):
    # Load and preprocess the image
    image = Image.open(image_path)
    preprocess = transforms.Compose([
        transforms.Resize((224, 224)),  # Resize to match input size of ResNet
        transforms.ToTensor(),  # Convert to tensor
        transforms.Normalize(  # Normalize image
            mean=[0.485, 0.456, 0.406],
            std=[0.229, 0.224, 0.225]
        )
    ])
    processed_image = preprocess(image)

    if task_type == 'image_classification':
        # Load classification model
        weights = ResNet50_Weights.IMAGENET1K_V2
        classification_model = resnet50(weights=ResNet50_Weights.IMAGENET1K_V2)
        classification_model.eval()
        classification_model.to('cuda')

        # Perform classification
        preprocessed_image = processed_image.unsqueeze(0).to("cuda")
        with torch.no_grad():
            output = classification_model(preprocessed_image)
        probabilities = torch.nn.functional.softmax(output[0], dim=0)
        top_prob, top_catid = torch.topk(probabilities, 1)
        category_name = weights.meta["categories"][top_catid[0].item()]
        result = {
            "task_type": "image_classification",
            "category_name": category_name,
            "score": top_prob[0].item(),
            "task_number": task_number
        }
        return result

    elif task_type == 'object_detection':
        # Load detection model
        detection_model = torch.hub.load('ultralytics/yolov5', 'yolov5s').to("cuda")

        # Convert processed image to numpy array
        processed_image_np = processed_image.mul(255).byte().numpy()

        # Transpose the image data
        processed_image_np = processed_image_np.transpose(1, 2, 0)

        # Perform detection
        result = detection_model([processed_image_np], augment=False)

        # Draw bounding boxes and labels on the image
        img_with_boxes = Image.open(image_path).convert("RGB")
        draw = ImageDraw.Draw(img_with_boxes)
        detected_regions = []
        detected_labels = []
        for detection in result.xyxy[0]:
            xmin, ymin, xmax, ymax, class_id, conf = detection.tolist()
            draw.rectangle([xmin, ymin, xmax, ymax], outline="red", width=3)
            detected_region = processed_image_np[int(ymin):int(ymax), int(xmin):int(xmax)]
            detected_regions.append(detected_region)
            detected_labels.append(int(class_id))

        result = {
            "task_type": "object_detection",
            "detected_labels": detected_labels,
            "image_path": image_path,
            "task_number": task_number
        }
        return result

    else:
        return {
            "task_type": task_type,
            "error": "Unsupported task type",
            "task_number": task_number
        }

if __name__ == '__main__':
    # Run Flask app
    app.run(debug=False, threaded=True)
