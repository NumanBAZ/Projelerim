import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.utils.data import DataLoader
from torchvision import datasets, transforms

class SimpleCNN(nn.Module):
    def __init__(self):
        super(SimpleCNN, self).__init__()
        self.conv1 = nn.Conv2d(in_channels=3, out_channels=256, kernel_size=3, padding=1)  # Conv2D (3, 256)
        self.pool1 = nn.MaxPool2d(kernel_size=2, stride=2)                                  # MaxPooling2D (2, 2)
        
        self.conv2 = nn.Conv2d(in_channels=256, out_channels=128, kernel_size=3, padding=1) # Conv2D (256, 128)
        self.pool2 = nn.MaxPool2d(kernel_size=2, stride=2)                                  # MaxPooling2D (2, 2)
        
        self.conv3 = nn.Conv2d(in_channels=128, out_channels=64, kernel_size=3, padding=1)  # Conv2D (128, 64)
        self.pool3 = nn.MaxPool2d(kernel_size=2, stride=2)                                  # MaxPooling2D (2, 2)

        self.flatten = nn.Flatten()                                                        # Flatten layer
        self.fc1 = nn.Linear(64 * 32 * 32, 64)                                             # Dense (Flatten to 64)
        self.fc2 = nn.Linear(64, 10)                                                       # Dense (64 to 10)

    def forward(self, x):
        x = F.relu(self.conv1(x))
        x = self.pool1(x)
        x = F.relu(self.conv2(x))
        x = self.pool2(x)
        x = F.relu(self.conv3(x))
        x = self.pool3(x)
        x = self.flatten(x)
        x = F.relu(self.fc1(x))
        x = self.fc2(x)
        return x

# Veri seti hazırlığı
train_transform = transforms.Compose([
    transforms.Resize((256, 256)),
    transforms.ToTensor(),
])

test_transform = transforms.Compose([
    transforms.Resize((256, 256)),
    transforms.ToTensor(),
])

train_dataset = datasets.ImageFolder(root='archive/train_zip', transform=train_transform)
test_dataset = datasets.ImageFolder(root='archive/test_zip', transform=test_transform)

train_loader = DataLoader(train_dataset, batch_size=32, shuffle=True)
test_loader = DataLoader(test_dataset, batch_size=32, shuffle=False)

# Modeli oluştur
model = SimpleCNN()

# Modelin özetini yazdır
print(model)

# Kayıp fonksiyonu ve optimizer tanımla
criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)

# Eğitim döngüsü
def train(model, train_loader, criterion, optimizer, device):
    model.train()
    running_loss = 0.0
    for images, labels in train_loader:
        images, labels = images.to(device), labels.to(device)

        # Sıfırlama
        optimizer.zero_grad()

        # İleri yayılım
        outputs = model(images)
        loss = criterion(outputs, labels)

        # Geri yayılım ve ağırlık güncellemesi
        loss.backward()
        optimizer.step()

        running_loss += loss.item()
    return running_loss / len(train_loader)

# Test döngüsü
def test(model, test_loader, criterion, device):
    model.eval()
    test_loss = 0.0
    correct = 0
    with torch.no_grad():
        for images, labels in test_loader:
            images, labels = images.to(device), labels.to(device)

            # İleri yayılım
            outputs = model(images)
            loss = criterion(outputs, labels)

            test_loss += loss.item()
            _, predicted = torch.max(outputs, 1)
            correct += (predicted == labels).sum().item()

    accuracy = 100 * correct / len(test_loader.dataset)
    return test_loss / len(test_loader), accuracy

# Modeli eğitme ve test etme
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

num_epochs = 10
for epoch in range(num_epochs):
    train_loss = train(model, train_loader, criterion, optimizer, device)
    test_loss, accuracy = test(model, test_loader, criterion, device)

    print(f"Epoch {epoch+1}/{num_epochs}, Train Loss: {train_loss:.4f}, Test Loss: {test_loss:.4f}, Accuracy: {accuracy:.2f}%")
