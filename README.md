# 🧥 Invisible Cloak with Black Cloth | OpenCV Magic

This Python project uses OpenCV to simulate an *invisibility cloak* effect. When you wear a black cloth in front of the webcam, it disappears, revealing the background behind you — like magic!

---

## 🎬 How It Works

- The webcam captures a static **background image**.
- Every frame is checked for **black regions** (your cloak).
- The black parts are **masked** and replaced with pixels from the stored background.
- The result is an illusion where the black cloth appears invisible.

---

## 📸 Demo

> *(Insert a video/GIF showing the effect)*

---

## 🛠️ Requirements

- Python 3.x
- OpenCV
- NumPy

### 🔧 Install Dependencies

```bash
pip install opencv-python numpy
