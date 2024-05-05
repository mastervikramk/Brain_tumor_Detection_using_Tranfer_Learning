from django.shortcuts import render, redirect
from .models import ImagePrediction
from .forms import ImagePredictionForm
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image as keras_image
from tensorflow.keras.applications.resnet50 import preprocess_input
import os
import numpy as np

# tumor_prediction/views.py
from django.shortcuts import render

def index(request):
    return render(request, 'tumor_prediction/index.html')
# Load the trained model
def load_prediction_model():
    model_path = os.path.join(os.getcwd(), 'models', 'model.h5')  # Replace 'your_model.h5' with the actual model filename
    model = load_model(model_path)
    return model

def predict_image_from_file(image_field, model):
    # Get the path of the image file
    image_path = image_field.path
    
    # Load the image file
    img = keras_image.load_img(image_path, target_size=(224, 224))
    
    # Convert the image to a numpy array
    img_array = keras_image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    
    # Preprocess the image
    img_array = preprocess_input(img_array)

    # Perform prediction
    prediction = model.predict(img_array)

    # Assuming binary classification, if the prediction value is greater than 0.5, it belongs to class 1, otherwise class 0
    if prediction > 0.5:
        return "Tumor"
    else:
        return "Non Tumor"
def upload_image(request):
    if request.method == 'POST':
        form = ImagePredictionForm(request.POST, request.FILES)
        if form.is_valid():
            image_instance = form.save(commit=False)  # Save the uploaded image to the database
            image_instance.save()  # Save the instance
            model = load_prediction_model()  # Load the prediction model
            prediction = predict_image_from_file(image_instance.image, model)  # Perform prediction
            return render(request, 'tumor_prediction/index.html', {'diagnosis_output': prediction})
    else:
        form = ImagePredictionForm()
    return render(request, 'tumor_prediction/upload.html', {'form': form})
