# tumor_prediction/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # URL for the main page
    path('upload/', views.upload_image, name='upload_image'),  # URL for image upload
]
    