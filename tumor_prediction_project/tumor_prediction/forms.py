

# tumor_prediction/forms.py
from django import forms
from .models import ImagePrediction

class ImagePredictionForm(forms.ModelForm):
    class Meta:
        model = ImagePrediction
        fields = ['image']
