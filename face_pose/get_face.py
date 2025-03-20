import cv2
import numpy as np

image = cv2.imread("./face_pose/image/faces.png")
face_cascade = cv2.CascadeClassifier('face_pose/face.xml')

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
print(faces)
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
    
cv2.imshow('detected', image)
cv2.waitKey(0)
cv2.destroyAllWindows()