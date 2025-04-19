# 🧠 Tumor Diagnosis Web App using ResNet50

## 📌 Overview

This is a simple Django-based web application built to diagnose brain tumors using a pre-trained **ResNet50** model. The app allows users to upload tumor images, processes them using the model, and returns a prediction indicating whether the tumor is **benign** or **malignant**.

## 🚀 Features

- 🔍 **Image-Based Tumor Diagnosis**: Upload an image, and the model predicts the tumor type.
- 💡 **Transfer Learning**: Uses ResNet50 pre-trained on ImageNet, fine-tuned for medical image classification.
- 🖥️ **Clean Web Interface**: Simple and intuitive UI built with HTML and CSS.
- ⚙️ **Backend with Django**: Robust Python web framework for server-side logic.

## 🛠️ Technologies Used

- **Django** – Python web framework
- **ResNet50** – Deep CNN model for image classification
- **TensorFlow / Keras** – Used to load and run the ML model
- **Python** – Main programming language
- **HTML/CSS** – Frontend design

---

## 🧪 Installation & Setup (Local)

Follow these steps to set up the project on your local machine:

```bash
# 1. Clone the repository
git clone https://github.com/mastervikramk/Brain_tumor_Detection_using_Tranfer_Learning.git

# 2. Navigate to the project directory
cd Brain_tumor_Detection_using_Tranfer_Learning

# 3. Create a virtual environment
python -m venv venv

# 4. Activate the virtual environment
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# 5. Install required dependencies
pip install -r requirements.txt

# 6. Run database migrations
python manage.py migrate

# 7. Start the Django development server
python manage.py runserver
