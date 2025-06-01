# Raspberry Pi Image Classifier

A simple image classification web app built with PyTorch and Flask on a Raspberry Pi.

### 🔍 Features
- Classifies images using a pretrained ResNet model
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

### 🖼️ Sample Image
Included: `1024px-Cute_dog.jpg` — used to test the classifier locally.

---

### 🚀 How to Run

#### 1. Clone the repo
```bash
git clone https://github.com/CyrusHurley/rpi-image-classifier.git
cd rpi-image-classifier
```

#### 2. Create and activate a virtual environment
```bash
python3 -m venv ~/edge-env
source ~/edge-env/bin/activate
```

#### 3. Install dependencies
```bash
pip install torch torchvision flask pillow
```

#### 4. Run the Flask app
```bash
python app.py
```

Flask will start on http://127.0.0.1:5000 or http://192.168.1.xxx:5000

#### 5. (Optional) Use ngrok to share
```bash
ngrok http 5000
```

You’ll get a public URL like `https://abcd1234.ngrok-free.app` that anyone can use to access your app.

---

### 🧠 Acknowledgments
- PyTorch's pretrained ResNet-18 model
- Raspberry Pi Foundation
- ngrok for quick sharing