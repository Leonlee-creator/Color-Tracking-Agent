# 🤖 Color Tracking AI Agent

This is a real-time AI agent built with Python and OpenCV. It uses computer vision to detect colors (red, green, blue) and identify obstacles based on edge detection. The agent then makes decisions like STOP, MOVE FORWARD, TURN, or AVOID OBSTACLE — simulating how a self-driving robot might behave in the real world.

---

##  Features

- 🎯 Color Detection (Red = Stop, Green = Go, Blue = Turn)
-  Obstacle Detection (Edge-based ROI scanning)
-  Simple Decision Logic for autonomous behavior
-  Real-time camera feed with action overlays
-  Easy to extend into a real robot using Arduino or Raspberry Pi

---

##  How It Works

- Uses OpenCV to capture video from your webcam.
- Converts frames to HSV color space for accurate color detection.
- Detects edges in a Region of Interest (ROI) to find obstacles.
- Based on the area of detected colors and obstacles, it decides what action to take.
- Displays the chosen action on the video feed.

---

## 🎮 Controls

- Press `Q` to quit the live video.

---

## 🧪 Requirements

- Python 3.7+
- OpenCV
- NumPy

Install with:

```bash
pip install opencv-python numpy

## Run It

python color_tracking_agent.py

## 💡Future Ideas
Add motor control to move a robot in real life.

Add sound feedback ("Beep" on STOP, etc).

Integrate with voice commands or remote control.

Train an ML model for smarter decisions.

🙌 Created By
Leon Taderera — Built as part of a real-world robotics and AI learning journey.