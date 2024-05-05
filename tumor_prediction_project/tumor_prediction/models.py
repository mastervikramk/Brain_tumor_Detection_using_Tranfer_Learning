from django.db import models

class ImagePrediction(models.Model):
    image = models.ImageField(upload_to='images/')  # Specify the directory where images will be stored
    image = models.ImageField(upload_to='images/') 
    class Meta:
        app_label = 'tumor_prediction'

