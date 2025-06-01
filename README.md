# Raspberry Pi Image Classifier

A simple image classification web app built with **PyTorch**, **Flask**, and a **pretrained ResNet-18 model**, running on a **Raspberry Pi 4**.

### 🔍 Features
- Classifies images using a pretrained ResNet model from `torchvision.models`
- Uses `Pillow` to handle JPEG/PNG input
- Displays prediction results through a Flask web interface
- Optional tunneling with `ngrok` for public access

### 🖥️ Tech Stack
- **Raspberry Pi 4 (64-bit OS)**
- **Python 3.11**
- **PyTorch + torchvision**
- **Flask**
- **ngrok** (for external tunneling)
- **HTML (Jinja2 templates)**

### 📸 Sample Image
Included: `1024px-Cute_dog.jpg` — used to test the classifier

### 🚀 How to Run

#### 1. Clone the repo
```bash
git clone https://github.com/CyrusHurley/rpi-image-classifier.git
cd rpi-image-classifier