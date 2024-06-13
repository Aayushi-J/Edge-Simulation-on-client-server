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
            "task_number": "A1",
            "initial_priority": 10
        },
        {
            "image_path": r"C:\Users\utkar\Downloads\DS_images\image2.jpg",
            "offloading_time": 0.6,
            "task_type": "object_detection",
            "task_number": "A2",
            "initial_priority": 9
        },
        {
            "image_path": r"C:\Users\utkar\Downloads\DS_images\image2.jpg",
            "offloading_time": 0.1,
            "task_type": "image_classification",
            "task_number": "A3",
            "initial_priority": 12
        },
        {
            "image_path": r"C:\Users\utkar\Downloads\DS_images\image1.png",
            "offloading_time": 0.2,
            "task_type": "object_detection",
            "task_number": "A4",
            "initial_priority": 11
        },
        {
            "image_path": r"C:\Users\utkar\Downloads\DS_images\image1.png",
            "offloading_time": 0.3,
            "task_type": "image_classification",
            "task_number": "A5",
            "initial_priority": 10
        },
        {
            "image_path": r"C:\Users\utkar\Downloads\DS_images\image2.jpg",
            "offloading_time": 0.6,
            "task_type": "object_detection",
            "task_number": "A6",
            "initial_priority": 9
        },
        {
            "image_path": r"C:\Users\utkar\Downloads\DS_images\image2.jpg",
            "offloading_time": 0.1,
            "task_type": "image_classification",
            "task_number": "A7",
            "initial_priority": 12
        },
        {
            "image_path": r"C:\Users\utkar\Downloads\DS_images\image1.png",
            "offloading_time": 0.2,
            "task_type": "object_detection",
            "task_number": "A8",
            "initial_priority": 11
        },
        {
            "image_path": r"C:\Users\utkar\Downloads\DS_images\image1.png",
            "offloading_time": 0.3,
            "task_type": "image_classification",
            "task_number": "A9",
            "initial_priority": 10
        },
        {
            "image_path": r"C:\Users\utkar\Downloads\DS_images\image2.jpg",
            "offloading_time": 0.6,
            "task_type": "object_detection",
            "task_number": "A10",
            "initial_priority": 4
        },
        {
            "image_path": r"C:\Users\utkar\Downloads\DS_images\image2.jpg",
            "offloading_time": 0.1,
            "task_type": "image_classification",
            "task_number": "A11",
            "initial_priority": 1
        },
        {
            "image_path": r"C:\Users\utkar\Downloads\DS_images\image1.png",
            "offloading_time": 0.2,
            "task_type": "object_detection",
            "task_number": "A12",
            "initial_priority": 11
        },
        {
            "image_path": r"C:\Users\utkar\Downloads\DS_images\image1.png",
            "offloading_time": 0.3,
            "task_type": "image_classification",
            "task_number": "A13",
            "initial_priority": 16
        },
        {
            "image_path": r"C:\Users\utkar\Downloads\DS_images\image2.jpg",
            "offloading_time": 0.6,
            "task_type": "object_detection",
            "task_number": "A14",
            "initial_priority": 9
        },
        {
            "image_path": r"C:\Users\utkar\Downloads\DS_images\image2.jpg",
            "offloading_time": 0.1,
            "task_type": "image_classification",
            "task_number": "A15",
            "initial_priority": 14
        },
        {
            "image_path": r"C:\Users\utkar\Downloads\DS_images\image1.png",
            "offloading_time": 0.2,
            "task_type": "object_detection",
            "task_number": "A16",
            "initial_priority": 7
        }
    ]
}

start_time = time.time()
response = requests.post(url, json=json_data)
print(response.json())
print("--- %s seconds ---" % (time.time() - start_time))
