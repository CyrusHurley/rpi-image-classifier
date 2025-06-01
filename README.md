# Raspberry Pi Image Classifier

This project runs a lightweight AI image classifier on a Raspberry Pi 4 using PyTorch and a pre-trained ResNet-18 model. It classifies an input image (e.g., a dog photo) using CPU-only inference.

## Features

- Loads and processes images using torchvision and Pillow
- Performs inference with ResNet-18
- Runs fully on Raspberry Pi without GPU (CUDA not required)
- Easy to modify or adapt for Raspberry Pi camera input

## Requirements

- Raspberry Pi 4 with Raspberry Pi OS 64-bit
- Python 3.9+
- pip install: `torch`, `torchvision`, `Pillow`

## Usage

From the project directory, run:

```bash
python3 classify.py

