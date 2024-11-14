from django.urls import path
from . import views

urlpatterns = [
    path('', views.gallery_view, name='gallery_view'),
    path('upload/', views.upload_image, name='upload_image'),
]
