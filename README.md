# crack_segmentation_model_in_buildings_and_roads

## Overview
The Crack Segmentation Project focuses on **automated detection and segmentation of cracks** in concrete and road surfaces using deep learning techniques.  
The project implements a **U-Net-based segmentation model** trained on annotated crack datasets, helping infrastructure engineers automate inspection and maintenance tasks.  

---

## Dataset

### 1. CRACK500 Dataset
- **Source:** [CRACK500 dataset](https://github.com/cool-mist/CRACK500)  
- **Content:** 500 images of concrete surfaces with cracks, each annotated with pixel-wise masks.  
- **Purpose:** Train the model to segment cracks accurately in varying lighting and surface conditions.  
- **Image Types:** RGB images, `.jpg` format  
- **Mask Types:** Binary masks, `.png` format  
- **Folder Structure:**
```
- data/
├─ train/ # Training images
├─ test/ # Testing images
masks/
└─ train/ # Ground truth masks for training
```

### 2. Preprocessing
- Images resized to 256x256 pixels  
- Normalized pixel values to [0,1]  
- Data augmentation applied (optional): rotation, flipping, and brightness adjustment  

---

## Project Structure
```
CrackSegmentation/
├─ notebooks/
│ └─ CrackSegmentation.ipynb # Main Colab notebook
├─ data/ # Training and testing images
├─ masks/ # Ground truth segmentation masks
├─ models/
│ └─ trained_model.pth # Saved trained U-Net model
├─ scripts/
│ ├─ train.py # Script for model training
│ └─ inference.py # Script for predicting cracks on new images
├─ results/ # Sample output predictions
├─ requirements.txt # Required Python packages
├─ README.md # Project documentation
└─ .gitignore # To exclude unnecessary files
```

## Sample outputs:

<img width="993" height="339" alt="image" src="https://github.com/user-attachments/assets/91a5c822-4ff6-4120-9119-334be1735b6e" />
<img width="993" height="339" alt="image" src="https://github.com/user-attachments/assets/d8e66501-4781-4dee-b403-a23be8ff9cac" />

## Evaluation Metrics

IoU (Intersection over Union): Measures overlap between predicted mask and ground truth

Dice Coefficient: Measures similarity between predicted mask and ground truth

Pixel-wise Accuracy: Measures the proportion of correctly predicted pixels.

## Key Features

U-Net architecture for precise crack segmentation

Supports custom dataset input

Preprocessing and optional data augmentation

Training and inference scripts with visualization of predictions


## Results

The model outputs binary masks highlighting cracks in images.



## Author


 JAGADEESH.A
 <br>
 B.Tech Artificial Intelligence and Data Science Engineering







