# Tumor Diagnosis Web App using ResNet50

## Overview

This is a simple Django-based web application built to diagnose tumors using a pre-trained ResNet50 model. The app takes in an image of a tumor, processes it using the ResNet50 model for classification, and returns a diagnosis (whether the tumor is benign or malignant).

## Features

- **Tumor Diagnosis**: Upload an image, and the model will predict if the tumor is benign or malignant.
- **User-Friendly Interface**: A simple web interface for uploading images.
- **Model**: Utilizes the ResNet50 model pre-trained on ImageNet and fine-tuned for tumor classification.

## Technologies Used

- **Django**: Web framework for Python used to build the backend.
- **ResNet50**: A pre-trained Convolutional Neural Network model used for image classification.
- **TensorFlow/Keras**: Libraries used to load and run the ResNet50 model.
- **HTML/CSS**: Frontend for the user interface.
- **Python**: Programming language used for both the backend and machine learning.

## Installation

#!/bin/bash

# 1. Clone the repository

git clone https://github.com/mastervikramk/Brain_tumor_Detection_using_Tranfer_Learning.git

# 2. Navigate to the project directory

cd tumor-diagnosis-webapp

# 3. Create a virtual environment

python -m venv venv

# 4. Activate the virtual environment (for Windows users, use venv\Scripts\activate)

# For Mac/Linux users:

source venv/bin/activate

# 5. Install the required packages

pip install -r requirements.txt

# 6. Run Django migrations (if needed)

python manage.py migrate

# 7. Start the development server

python manage.py runserver
