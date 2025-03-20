import cv2
import mediapipe as mp

mp_pose = mp.solutions.pose
pose = mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5)

image = cv2.imread("./face_pose/image/yoga.png")

results = pose.process(image)

mp_drawing = mp.solutions.drawing_utils
annotated_image = image.copy()
mp_drawing.draw_landmarks(annotated_image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

cv2.imshow('a', annotated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()