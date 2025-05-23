from ultralytics import YOLO
import cv2
import random
import os

def generate_random_name():
    characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    random_name = ''
    for i in range(10):
        random_name += random.choice(characters)
    return random_name

def find_obj(image):
    model = YOLO("yolo11n.pt")
    name = generate_random_name()
    results = model.predict(source=image, save=True, name=f'{name}')
    filename = os.path.basename(image)
    new_image = cv2.imread(f'../runs/detect/{name}/{filename}')
    return new_image
