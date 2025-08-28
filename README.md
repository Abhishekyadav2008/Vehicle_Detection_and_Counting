# Vehicle_Detection_and_Counting
Overview
This project focuses on detecting, tracking, and counting vehicles in video footage using deep learning and computer vision. It utilizes state-of-the-art technologies such as YOLO and OpenCV to enable real-time and robust traffic analytics.

Features
Vehicle detection using YOLO (You Only Look Once) models

Tracking and counting with unique IDs

Visual overlays on video for tracked objects and counts

Easily customizable for different detection zones or counting lines

Tech Stack
Python 3.8+

OpenCV

PyTorch or TensorFlow (depending on YOLO implementation)

Numpy

Installation
Clone the repository:

bash
git clone https://github.com/<your-username>/<your-repo-name>.git
cd <your-repo-name>
Install dependencies:

bash
pip install -r requirements.txt
Usage
Download pretrained YOLO weights (YOLOv8 or YOLOv5 recommended) and place them in the project directory.

To run vehicle detection and counting on a video:

bash
python main.py --input data/sample_video.mp4 --weights yolov8.pt
Change the arguments as needed for your setup.

Output
Processed video with bounding boxes and vehicle count overlay

