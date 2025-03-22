import cv2
import os
import base64

def find_face(image):
    cascade_path = os.path.join(os.path.dirname(__file__), 'face.xml')

    image = cv2.imread(image)
    face_cascade = cv2.CascadeClassifier(cascade_path)

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
        
    return image

def image_to_base64(image) -> str:
    
    _, buffer = cv2.imencode('.png', image)
    img_str = base64.b64encode(buffer).decode('utf-8')
    
    return img_str