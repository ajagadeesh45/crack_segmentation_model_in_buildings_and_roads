import os
import torch
from torch.utils.data import DataLoader
from torchvision import transforms
from dataset import CrackDataset      # You can create a small dataset class
from model import UNet               # Your U-Net implementation

# Paths
train_img_dir = "data/train"
train_mask_dir = "masks/train"
model_save_path = "models/trained_model.pth"

# Hyperparameters
batch_size = 4
epochs = 50
lr = 1e-3

# Dataset & DataLoader
transform = transforms.Compose([
    transforms.ToTensor(),
])
train_dataset = CrackDataset(train_img_dir, train_mask_dir, transform=transform)
train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)

# Model, Loss, Optimizer
model = UNet()
criterion = torch.nn.BCELoss()
optimizer = torch.optim.Adam(model.parameters(), lr=lr)

# Training Loop
for epoch in range(epochs):
    model.train()
    epoch_loss = 0
    for imgs, masks in train_loader:
        optimizer.zero_grad()
        outputs = model(imgs)
        loss = criterion(outputs, masks)
        loss.backward()
        optimizer.step()
        epoch_loss += loss.item()
    print(f"Epoch {epoch+1}/{epochs}, Loss: {epoch_loss/len(train_loader)}")

# Save model
torch.save(model.state_dict(), model_save_path)
print(f"Model saved at {model_save_path}")

