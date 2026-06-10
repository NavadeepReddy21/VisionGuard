# VisionGuard

**VisionGuard** is a real-time motion detection and surveillance system built with Python and OpenCV. It uses background subtraction, contour analysis, and image processing techniques to detect, highlight, and track moving objects in video streams.

The system is designed to demonstrate practical computer vision concepts commonly used in surveillance, security monitoring, and video analytics applications.

---

## Features

* Real-time motion detection
* Background subtraction using MOG2
* Noise reduction with filtering and morphological operations
* Motion region highlighting with transparent overlays
* Bounding box visualization for detected objects
* Motion area estimation
* FPS (Frames Per Second) monitoring
* Output video recording and saving

---

## Technology Stack

* **Python**
* **OpenCV**
* **NumPy**

---

## Project Architecture

```text
Video Input
     │
     ▼
Background Subtraction (MOG2)
     │
     ▼
Noise Reduction & Morphology
     │
     ▼
Contour Detection
     │
     ▼
Motion Analysis
     │
     ├── Bounding Boxes
     ├── Motion Overlay
     └── Area Calculation
     │
     ▼
Processed Output Video
```

---

## Installation

### Clone the Repository

```bash
git clone https://github.com/NavadeepReddy21/VisionGuard.git
cd VisionGuard
```

### Create a Virtual Environment

**Windows**

```bash
python -m venv venv
venv\Scripts\activate
```

**Linux/macOS**

```bash
python3 -m venv venv
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Requirements

```txt
opencv-python
numpy
```

---

## Usage

1. Place your video file inside the project directory.
2. Update the video path in the script:

```python
video_path = "sample.mp4"
```

3. Run the application:

```bash
python motion_detection.py
```

4. Press **ESC** to exit the program.

---

## Example Output

The system performs:

* Motion detection in video frames
* Real-time object highlighting
* Bounding box generation
* Motion area measurement
* FPS tracking

Processed videos are automatically saved as:

```text
motion_output.mp4
```

---

## Project Structure

```text
VisionGuard/
│
├── motion_detection.py
├── requirements.txt
├── README.md
├── .gitignore
├── LICENSE
└── demo_output.mp4
```

---

## Future Enhancements

* YOLOv8 object detection integration
* Vehicle and pedestrian tracking
* Motion event logging
* Email and notification alerts
* Live webcam monitoring
* Multi-camera surveillance support
* Web dashboard for monitoring

---

## Applications

* Smart surveillance systems
* Security monitoring
* Traffic analysis
* Industrial monitoring
* Motion analytics
* Computer vision learning projects

---

## License

This project is licensed under the MIT License.

---

## Author

**Navadeep Reddy**

A computer vision project developed to explore real-time motion analysis, object tracking, and video processing using OpenCV and Python.
