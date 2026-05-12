# 🧠 Outfit Matching Assistant

## 🎯 Project Overview

Outfit Matching Assistant is an AI-powered system that analyzes fashion images and provides smart outfit recommendations.

Given an input image such as a T-shirt, the system can:

- 👕 Detect clothing type such as T-shirt, Shirt, or Hoodie
- 🎨 Extract the dominant color from the image
- 🧠 Recommend matching outfit colors using a rule-based engine
- 🌐 Provide a simple web interface for interaction

This project combines:

- Deep Learning with CNN and Transfer Learning
- Computer Vision with OpenCV color extraction
- Rule-based AI recommendation logic
- Web deployment using Streamlit

## 🚀 Pipeline Architecture

```text
Image Input
     ↓
[1] Clothing Type Classification (CNN / ResNet50)
     ↓
[2] Color Extraction (OpenCV + KMeans)
     ↓
[3] Recommendation Engine (Rule-Based System)
     ↓
Final Output:
Type + Color + Outfit Suggestions
```

## 🧩 Project Structure

```text
outfit-matching-assistant/
│
├── data/
│   ├── raw/
│   ├── processed/
│   ├── train/
│   ├── val/
│   └── test/
│
├── notebooks/
│   ├── 01_data_exploration.ipynb
│   ├── 02_preprocessing.ipynb
│   ├── 03_cnn_scratch.ipynb
│   ├── 04_transfer_learning.ipynb
│   └── 05_evaluation.ipynb
│
├── src/
│   ├── data_loader.py
│   ├── preprocessing.py
│   ├── model_scratch.py
│   ├── model_transfer.py
│   ├── train.py
│   ├── evaluate.py
│   ├── color_detection.py
│   ├── recommender.py
│   └── utils.py
│
├── models/
│   ├── cnn_scratch.h5
│   └── transfer_model.h5
│
├── results/
│   ├── plots/
│   ├── confusion_matrix.png
│   └── metrics.txt
│
├── app/
│   └── app.py
│
├── reports/
│   ├── final_report.pdf
│   └── presentation.pptx
│
├── requirements.txt
├── main.py
└── README.md
```

## 🧠 Project Modules

### 1. Dataset Preparation

- Source: Fashion Product Images from Kaggle
- Classes: Tops, T-shirts, Shirts, Hoodies
- Labels: `articleType`
- Extra: automatic color extraction

### 2. Preprocessing

- Resize to 224×224
- Normalize images
- Apply data augmentation
- Split the dataset into:
  - 70% Train
  - 15% Validation
  - 15% Test

### 3. CNN from Scratch

- Custom Convolutional Neural Network
- Task: clothing classification

### 4. Transfer Learning

- Model: ResNet50
- Fine-tuned on the dataset
- Expected to outperform the scratch model

### 5. Color Detection

- OpenCV and KMeans clustering
- Extract the dominant color from an image

```python
from sklearn.cluster import KMeans
```

### 6. Recommendation System

| Color | Suggested Colors |
| --- | --- |
| White | Any color |
| Black | White / Gray |
| Blue | Beige / White |
| Red | Black / White |

## 🎯 Final Output Example

```text
Type: T-shirt
Color: Blue
Recommendations:
- White Pants
- Beige Pants
```

## 📊 Evaluation Metrics

- Accuracy
- Precision
- Recall
- F1 Score
- Confusion Matrix

## 🌐 Web App

Built using Streamlit.

Run:

```bash
streamlit run app/app.py
```

## ⚙️ Installation & Setup

### Clone Repo

```bash
git clone https://github.com/your-username/outfit-matching-assistant.git
cd outfit-matching-assistant
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Train Model

```bash
python main.py
```

### Run App

```bash
streamlit run app/app.py
```

## 🔥 Why This Project is Strong

- Real AI and deep learning
- Transfer learning included
- Complete computer vision pipeline
- Smart recommendation engine
- Easy deployment with Streamlit
- Clean academic structure

