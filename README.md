# Binocular Camera Debris Detection System

This project, developed under **Purdue Astrobotics**, uses external binocular cameras and computer vision techniques to detect debris in various environments. By leveraging OpenCV and other computer vision libraries, the system processes stereo camera feeds to identify and track debris, improving object detection capabilities for robotics applications.

## Project Overview

The **Binocular Camera Debris Detection System** is designed to:
- Capture real-time video feed using dual external cameras.
- Use stereo vision to calculate depth information for accurate debris detection.
- Detect, classify, and track debris based on size, shape, and movement.
- Assist robotics systems in navigating or avoiding hazardous areas by marking debris locations.

## Features

- **Stereo Vision Processing**: Utilizes two cameras to create depth perception, enabling the system to locate debris in 3D space.
- **Real-time Detection**: Processes video frames in real-time to detect moving or stationary debris.
- **Object Tracking**: Tracks identified debris and marks its location relative to the robotic platform.
- **Adaptable to Various Environments**: Configurable to operate under different lighting conditions and terrains.

## Requirements

- **Python 3.x**
- **OpenCV**: For image processing and video capture.
- **NumPy**: For array operations.
- **(Optional) PyTorch / TensorFlow**: For advanced machine learning models if needed.

To install the necessary dependencies, run:
```bash
pip install -r requirements.txt
