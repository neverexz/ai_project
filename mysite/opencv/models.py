from django.db import models
from matplotlib import category
from sympy import field

# Create your models here.
class Image(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images')
    category = models.CharField(max_length=20, choices=[('f', 'face'), ('p', 'pose'), ('y', 'yolo')], default='y')
    def __str__(self):
        return self.title