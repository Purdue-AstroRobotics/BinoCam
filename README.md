
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
```

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/YourUsername/BinocularDebrisDetection.git
   cd BinocularDebrisDetection
   ```

2. **Connect External Cameras**:
   - Ensure that two external cameras are connected and recognized by your system.

3. **Run the Project**:
   Start the debris detection system with:
   ```bash
   python debris_detection.py
   ```

## Usage

- Run the main script to initiate video capture from both cameras and process the stereo feed.
- Adjust camera parameters in the `config.json` file for specific needs, such as resolution or frame rate.

## Configuration

Edit `config.json` for settings such as:
- **Camera IDs**: IDs for the left and right cameras.
- **Resolution**: Width and height of the camera feed.
- **Thresholds**: Customize sensitivity for debris detection and tracking.

## Example Workflow

1. **Initialize Cameras**: Connect and configure camera feeds.
2. **Calibration**: Calibrate the stereo setup for accurate depth measurements.
3. **Debris Detection**: Run the system to detect debris in real-time.
4. **Data Output**: Location and details of debris are logged or sent to a central processing unit.

## Contributing

Contributions are welcome! Please feel free to submit issues, fork the repository, and create pull requests to improve detection accuracy, tracking algorithms, or add new features.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Acknowledgments

This project is a collaboration between **Purdue Astrobotics** and **Purdue University's Computer Science Department**, focusing on advancing robotics through vision-based detection systems.
