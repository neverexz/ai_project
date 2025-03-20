from django.urls import path
from .views import *

urlpatterns = [
    path('', filter, name='filter.url')
]
