import torch
import torch.nn as nn
import torch.nn.functional as F
from matplotlib import pyplot as plt
from tqdm import tqdm


class SimpleCNN(nn.Module):
    def __init__(self, num_classes=102):
        super(SimpleCNN, self).__init__()
        self.conv1 = nn.Conv2d(in_channels=3, out_channels=32, kernel_size=3, padding=1)
        self.conv2 = nn.Conv2d(in_channels=32, out_channels=64, kernel_size=3, padding=1)
        self.pool = nn.MaxPool2d(kernel_size=2, stride=2)
        self.conv3 = nn.Conv2d(in_channels=64, out_channels=128, kernel_size=3, padding=1)
        self.conv4 = nn.Conv2d(in_channels=128, out_channels=256, kernel_size=3, padding=1)
        self.pool2 = nn.MaxPool2d(kernel_size=2, stride=2)
        self.fc1 = nn.Linear(256 * 14 * 14, 1024)  # Adjusting for the flattened output size
        self.fc2 = nn.Linear(1024, num_classes)

    def forward(self, x):
        # Apply the first convolution layer with ReLU activation function, then max pooling
        x = self.pool(F.relu(self.conv1(x)))
        x = self.pool(F.relu(self.conv2(x)))
        x = self.pool(F.relu(self.conv3(x)))
        x = self.pool2(F.relu(self.conv4(x)))
        # Flatten the output for the fully connected layer
        x = x.view(-1, 256 * 14 * 14)
        # Apply the fully connected layer with ReLU activation function
        x = F.relu(self.fc1(x))
        x = self.fc2(x)
        return x


def evaluate_model(model, test_loader, device):
    model.eval()
    correct = 0
    total = 0
    with torch.no_grad():
        for images, labels in test_loader:
            images, labels = images.to(device), labels.to(device)
            outputs = model(images)
            _, predicted = torch.max(outputs, 1)
            total += labels.size(0)
            correct += (predicted == labels).sum().item()
    accuracy = 100 * correct / total
    print(f'Test Accuracy: {accuracy:.2f}%')
    return accuracy


def train_model(num_epochs, model, criterion, optimizer, scheduler, train_loader, device, test_loader):
    train_losses = []
    train_accuracies = []
    test_accuracies = []
    model.train()
    for epoch in range(num_epochs):
        print(f'training on epoch:{epoch}')
        running_loss = 0.0
        total = 0
        correct = 0
        for images, labels in tqdm(train_loader):
            images, labels = images.to(device), labels.to(device)
            optimizer.zero_grad()
            outputs = model(images)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()
            running_loss += loss.item() * images.size(0)
            _, predicted = torch.max(outputs, 1)
            total += labels.size(0)
            correct += (predicted == labels).sum().item()
        scheduler.step()
        epoch_loss = running_loss / len(train_loader.dataset)
        epoch_accuracy = 100 * correct / total
        train_losses.append(epoch_loss)
        train_accuracies.append(epoch_accuracy)

        # Test accuracy
        test_accuracy = evaluate_model(model, test_loader, device)
        test_accuracies.append(test_accuracy)
        print(f'Epoch [{epoch + 1}/{num_epochs}], Loss: {epoch_loss:.4f}, Train Accuracy: {epoch_accuracy:.2f}%')
    # Plot the metrics
    plt.figure(figsize=(12, 4))

    # Training Loss Curve
    plt.subplot(1, 3, 1)
    plt.plot(range(1, num_epochs + 1), train_losses, label='Training Loss')
    plt.xlabel('Epochs')
    plt.ylabel('Loss')
    plt.title('Training Loss Curve')

    # Training Accuracy Curve
    plt.subplot(1, 3, 2)
    plt.plot(range(1, num_epochs + 1), train_accuracies, label='Training Accuracy')
    plt.xlabel('Epochs')
    plt.ylabel('Accuracy (%)')
    plt.title('Training Accuracy Curve')
    # Test Accuracy Curve
    plt.subplot(1, 3, 3)
    plt.plot(range(1, num_epochs + 1), test_accuracies, label='Test Accuracy', color='orange')
    plt.xlabel('Epochs')
    plt.ylabel('Accuracy (%)')
    plt.title('Test Accuracy Curve')
    plt.legend()

    # Display the plots
    plt.tight_layout()  # Adjust layout for better spacing
    plt.show()
