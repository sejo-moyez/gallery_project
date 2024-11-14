from django.shortcuts import render

# Create your views here.

from .forms import ImageForm
from django.shortcuts import render, redirect
from .models import Image 

def gallery_view(request):
  images = Image.objects.all()
  return render(request, 'gallery/gallery_view.html', {'images' : images})

def upload_image(request):
  if request.method == 'POST':
    form = ImageForm(request.POST, request.FILES)
    if form.is_valid():
      form.save()
      return redirect('gallery_view')
  else:
    form = ImageForm()
  return render(request, 'gallery/upload_image.html', {'form' : form})
