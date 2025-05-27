from django.shortcuts import render

from .forms import ImageForm
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))
from finder import get_face, yolo, get_pose
import cv2

def filter(request):
    return render(request, template_name='opencv/filter.html')

def image_upload(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            img_obj = form.instance
            path = img_obj.image.path
            category = form.cleaned_data['category']
            print(category)
            if category == 'f':
                img_obj = get_face.find_face(path)
            if category == 'y':
                img_obj = yolo.find_obj(path)
            if category == 'p':
                img_obj = get_pose.find_pose(path)
            img_obj = get_face.image_to_base64(img_obj)
            
            return render(request, 'opencv/photo.html', {'photo': f"data:image/jpeg;base64,{img_obj}"})
            
    else:
        form = ImageForm()
    return render(request, 'opencv/filter.html', {'form': form})
