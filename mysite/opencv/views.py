from django.shortcuts import render

from .forms import ImageForm
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))
from face_pose import get_face
import cv2

# Create your views here.
def filter(request):
    return render(request, template_name='opencv/filter.html')

def image_upload(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            img_obj = form.instance
            path = img_obj.image.path
            img_obj = get_face.find_face(path)
            img_obj = get_face.image_to_base64(img_obj)
            return render(request, 'opencv/photo.html', {'photo': f"data:image/jpeg;base64,{img_obj}"})
    else:
        form = ImageForm()
    return render(request, 'opencv/filter.html', {'form': form})
