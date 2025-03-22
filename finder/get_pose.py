import cv2
import mediapipe as mp

def find_pose(image):
    mp_pose = mp.solutions.pose
    pose = mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5)

    new_image = cv2.imread(image)

    results = pose.process(new_image)

    mp_drawing = mp.solutions.drawing_utils
    annotated_image = new_image.copy()
    mp_drawing.draw_landmarks(annotated_image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)
    
    return annotated_image
    
    

# cv2.imshow('a', annotated_image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()