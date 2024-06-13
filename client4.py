import requests
import json
import time

url = 'http://127.0.0.1:5000/process_images'

json_data = {
    "images_data": [
        {
            "image_path": r"C:\Users\utkar\Downloads\DS_images\image1.png",
            "offloading_time": 0.3,
            "task_type": "image_classification",
            "task_number": "D1",
            "initial_priority": 7
        },
        {
            "image_path": r"C:\Users\utkar\Downloads\DS_images\image4.jpg",
            "offloading_time": 0.6,
            "task_type": "object_detection",
            "task_number": "D2",
            "initial_priority": 6
        },
        {
            "image_path": r"C:\Users\utkar\Downloads\DS_images\image6.jpg",
            "offloading_time": 0.1,
            "task_type": "image_classification",
            "task_number": "D3",
            "initial_priority": 8

        },
        {
            "image_path": r"C:\Users\utkar\Downloads\DS_images\image8.jpg",
            "offloading_time": 0.2,
            "task_type": "object_detection",
            "task_number": "D4",
            "initial_priority": 4
        },
        {
            "image_path": r"C:\Users\utkar\Downloads\DS_images\image9.jpg",
            "offloading_time": 0.1,
            "task_type": "image_classification",
            "task_number": "D5",
            "initial_priority": 3
        },
        {
            "image_path": r"C:\Users\utkar\Downloads\DS_images\image2.jpg",
            "offloading_time": 0.2,
            "task_type": "object_detection",
            "task_number": "D6",
            "initial_priority": 9
        },
        {
            "image_path": r"C:\Users\utkar\Downloads\DS_images\image1.png",
            "offloading_time": 0.3,
            "task_type": "image_classification",
            "task_number": "D7",
            "initial_priority": 7
        },
        {
            "image_path": r"C:\Users\utkar\Downloads\DS_images\image4.jpg",
            "offloading_time": 0.6,
            "task_type": "image_classification",
            "task_number": "D8",
            "initial_priority": 6
        },
        {
            "image_path": r"C:\Users\utkar\Downloads\DS_images\image6.jpg",
            "offloading_time": 0.1,
            "task_type": "object_detection",
            "task_number": "D9",
            "initial_priority": 8

        },
        {
            "image_path": r"C:\Users\utkar\Downloads\DS_images\image8.jpg",
            "offloading_time": 0.2,
            "task_type": "image_classification",
            "task_number": "D10",
            "initial_priority": 4
        },
        {
            "image_path": r"C:\Users\utkar\Downloads\DS_images\image9.jpg",
            "offloading_time": 0.1,
            "task_type": "object_detection",
            "task_number": "D11",
            "initial_priority": 3
        },
        {
            "image_path": r"C:\Users\utkar\Downloads\DS_images\image2.jpg",
            "offloading_time": 0.2,
            "task_type": "image_classification",
            "task_number": "D12",
            "initial_priority": 9
        }
    ]
}

start_time = time.time()
response = requests.post(url, json=json_data)
print(response.json())
print("--- %s seconds ---" % (time.time() - start_time))