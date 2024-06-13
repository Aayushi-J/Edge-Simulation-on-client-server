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
            "task_number": "E1",
            "initial_priority": 8

        },
        {
            "image_path": r"C:\Users\utkar\Downloads\DS_images\image2.jpg",
            "offloading_time": 0.6,
            "task_type": "object_detection",
            "task_number": "E2",
            "initial_priority": 9
        },
        {
            "image_path": r"C:\Users\utkar\Downloads\DS_images\image3.jpg",
            "offloading_time": 0.1,
            "task_type": "image_classification",
            "task_number": "E3",
            "initial_priority": 7
        },
        {
            "image_path": r"C:\Users\utkar\Downloads\DS_images\image4.jpg",
            "offloading_time": 0.2,
            "task_type": "object_detection",
            "task_number": "E4",
            "initial_priority": 4
        },
        {
            "image_path": r"C:\Users\utkar\Downloads\DS_images\image6.jpg",
            "offloading_time": 0.2,
            "task_type": "object_detection",
            "task_number": "E6",
            "initial_priority": 5
        },
        {
            "image_path": r"C:\Users\utkar\Downloads\DS_images\image7.jpg",
            "offloading_time": 0.2,
            "task_type": "object_detection",
            "task_number": "E7",
            "initial_priority": 3
        },
        {
            "image_path": r"C:\Users\utkar\Downloads\DS_images\image8.jpg",
            "offloading_time": 0.1,
            "task_type": "image_classification",
            "task_number": "E8",
            "initial_priority": 8
        },
        {
            "image_path": r"C:\Users\utkar\Downloads\DS_images\image9.jpg",
            "offloading_time": 0.2,
            "task_type": "object_detection",
            "task_number": "E9",
            "initial_priority": 2
        },
        {
            "image_path": r"C:\Users\utkar\Downloads\DS_images\image1.png",
            "offloading_time": 0.3,
            "task_type": "image_classification",
            "task_number": "E1",
            "initial_priority": 8

        },
        {
            "image_path": r"C:\Users\utkar\Downloads\DS_images\image2.jpg",
            "offloading_time": 0.6,
            "task_type": "object_detection",
            "task_number": "E2",
            "initial_priority": 9
        },
        {
            "image_path": r"C:\Users\utkar\Downloads\DS_images\image3.jpg",
            "offloading_time": 0.1,
            "task_type": "image_classification",
            "task_number": "E3",
            "initial_priority": 7
        },
        {
            "image_path": r"C:\Users\utkar\Downloads\DS_images\image4.jpg",
            "offloading_time": 0.2,
            "task_type": "object_detection",
            "task_number": "E4",
            "initial_priority": 4
        },
        {
            "image_path": r"C:\Users\utkar\Downloads\DS_images\image6.jpg",
            "offloading_time": 0.2,
            "task_type": "object_detection",
            "task_number": "E6",
            "initial_priority": 5
        },
        {
            "image_path": r"C:\Users\utkar\Downloads\DS_images\image7.jpg",
            "offloading_time": 0.2,
            "task_type": "object_detection",
            "task_number": "E7",
            "initial_priority": 3
        },
        {
            "image_path": r"C:\Users\utkar\Downloads\DS_images\image8.jpg",
            "offloading_time": 0.1,
            "task_type": "image_classification",
            "task_number": "E8",
            "initial_priority": 8
        },
        {
            "image_path": r"C:\Users\utkar\Downloads\DS_images\image9.jpg",
            "offloading_time": 0.2,
            "task_type": "object_detection",
            "task_number": "E9",
            "initial_priority": 2
        }
    ]
}

start_time = time.time()
response = requests.post(url, json=json_data)
print(response.json())
print("--- %s seconds ---" % (time.time() - start_time))
