import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, random_split
from torchvision import datasets, transforms

from train_and_evaluate import SimpleCNN, train_model, evaluate_model

# Data augmentation for training and simple transforms for validation
train_transform = transforms.Compose([
    transforms.RandomResizedCrop(224),
    # You can add more transform here...
    # ...
    transforms.RandomRotation(10),  # Random rotation within a range of -20 to 20 degrees
    transforms.RandomHorizontalFlip(),  # Random horizontal flip
    transforms.ColorJitter(brightness=0.2, contrast=0.2, saturation=0.2),
    # # Randomly change the brightness, contrast, saturation, and hue
    transforms.RandomAffine(degrees=0, translate=(0.1, 0.1), scale=(0.8, 1.2)),
    # Randomly erase parts of the image with a certain probability (helps with robustness)
    transforms.ToTensor(),
    # If you use ImageNet1K pretrained-model, normalize as follows
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
])
test_transform = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    # If you use ImageNet1K pretrained-model, normalize as follows
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])])
# Define the dataset path
dataset_path = 'C:/Users/Jinx/Downloads/caltech-101/101_ObjectCategories/'
dataset = datasets.ImageFolder(dataset_path, transform=train_transform)
# Split dataset into training and testing
train_size = int(0.8 * len(dataset))
test_size = len(dataset) - train_size
train_dataset, test_dataset = random_split(dataset, [train_size, test_size])
# Apply different transform s to test dataset
test_dataset.dataset.transform = test_transform
# Create data loaders
train_loader = DataLoader(train_dataset, batch_size=32, shuffle=True)
test_loader = DataLoader(test_dataset, batch_size=32, shuffle=False)
# Instantiate the model
model = SimpleCNN()
# Move model to GPU if available
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)
# Define loss function and optimizer
epochs = 10
criterion = nn.CrossEntropyLoss()
optimizer = optim.SGD(model.parameters(), lr=0.01, momentum=0.9, weight_decay=2e-4)
scheduler = optim.lr_scheduler.CosineAnnealingLR(optimizer, T_max=epochs)
# Run training and evaluation
train_model(epochs, model, criterion, optimizer, scheduler, train_loader, device, test_loader)
evaluate_model(model, test_loader, device)
