
# DRISHYAM

## Overview
**DRISHYAM** is an assistive technology project designed to facilitate communication and recognition for individuals with hearing or speech impairments. The project integrates video frame extraction, object detection using MobileNet models, basic GUI interaction, and image processing utilities to help bridge communication gaps.

This system is modular and consists of:
- A graphical user interface (GUI) for user input
- A dataset collection pipeline
- Real-time camera interfacing and frame collection
- Labelling tools for training datasets
- Pre-trained object detection models

---

## Features

- GUI with accessible interaction points
- Real-time frame extraction from video or webcam
- Word segmentation logic using OpenCV
- Folder automation for dataset creation
- Object detection with pre-trained TensorFlow models
- Labelling utility using labelImg
- Multi-user support in image processing folder

---

## Project Structure

```
DRISHYAM/
├── Dataset Collection/         # Frame extraction and folder setup
├── ImageProcessing/            # User-wise processed image data
├── Labelling tool/            # Includes labelImg.exe and class labels
├── Partial Implementation/    # Main GUI, segmentation logic, video input
├── WithImages/                # Frame collection script
├── _models/                   # Pre-trained MobileNet model files (.pb, .pbtxt)
├── requirements.txt
```

---

## Tech Stack

### Core Languages & Frameworks:
- **Python 3**
- **Tkinter** for GUI
- **OpenCV** for image and video processing
- **TensorFlow 1.15** for object detection

---

## Setup Instructions

### 1. Install Python dependencies
```bash
pip install -r requirements.txt
```

> Ensure Python version is compatible with TensorFlow 1.15.

### 2. Launch GUI
```bash
cd "Partial Implementation"
python gui.py
```

### 3. Frame Extraction for Dataset
```bash
cd "Dataset Collection"
python extract_frame.py
```

### 4. Run Word Segmentation
```bash
cd "Partial Implementation"
python wordSegmentation.py
```

---

## Requirements

Make sure the following are installed:
- Python 3.6+
- TensorFlow 1.15
- numpy, scipy

---

## Notes

- The application is not fully integrated end-to-end but provides a strong foundation for building assistive AI interfaces.
- LabelImg is included as an executable and helps prepare datasets for further training.
- GUI allows switching between modes like normal communication and mute screen with language dropdown (currently limited).

---

## Use Case

This tool can assist in:
- Translating signs or visual cues to actions
- Assisting speech-impaired users via GUI prompts and object detection
- Rapid prototyping for vision-based AI assistance

