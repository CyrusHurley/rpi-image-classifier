from torchvision import models, transforms
from PIL import Image
import torch

img = Image.open("1024px-Cute_dog.jpg")

preprocess = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406],
                         std=[0.229, 0.224, 0.225]),
])

batch = preprocess(img).unsqueeze(0)

model = models.resnet18(weights='DEFAULT')
model.eval()

with torch.no_grad():
    output = model(batch)
    print(torch.argmax(output))                                                                                                                                                                                                                                                                             



