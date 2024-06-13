import requests
import json
import time

url = 'http://127.0.0.1:5000/process_images'

json_data = {
    "images_data": [
        {
            "image_path": r"C:\Users\utkar\Downloads\DS_images\image6.jpg",
            "offloading_time": 0.3,
            "task_type": "image_classification",
            "task_number": "C1",
            "initial_priority": 8
        },
        {
            "image_path": r"C:\Users\utkar\Downloads\DS_images\image4.jpg",
            "offloading_time": 0.6,
            "task_type": "object_detection",
            "task_number": "C2",
            "initial_priority": 8
        }
    ]
}

start_time = time.time()
response = requests.post(url, json=json_data)
print(response.json())
print("--- %s seconds ---" % (time.time() - start_time))
