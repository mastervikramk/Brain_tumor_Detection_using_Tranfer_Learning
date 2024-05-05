
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np

# Load the saved model
saved_model_path = "model.h5"  # Update this with the path to your saved model
loaded_model = load_model(saved_model_path)

# Define a function to preprocess the image for prediction
def preprocess_image(image_path, target_size=(224, 224)):
    img = image.load_img(image_path, target_size=target_size)
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    return img_array

# Path to the image you want to predict
image_path = "y701.jpg"  # Update this with the path to your image

# Preprocess the image
processed_image = preprocess_image(image_path)

# Make prediction
prediction = loaded_model.predict(processed_image)

# Assuming binary classification, if the prediction value is greater than 0.5, it belongs to class 1, otherwise class 0
if prediction > 0.5:
    print("Class 1")
else:
    print("Class 0")
