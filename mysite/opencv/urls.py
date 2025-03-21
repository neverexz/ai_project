from django.urls import path
from .views import *

urlpatterns = [
    path('', image_upload),
    path('upload/', image_upload)
]
