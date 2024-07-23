import cv2
import time
import os
from datetime import datetime
import dlib

face_detected_count = 0

# Load the pre-trained Haar Cascade face detection model (outside the function)
# face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

detector = dlib.get_frontal_face_detector()

# Load the pre-trained facial landmark detector model
predictor = dlib.shape_predictor("D:/Exam Proctoring System/libraries/shape_predictor_68_face_landmarks.dat")  # You need to download this file

def detect_faces(frame):
  global face_detected_count
  # Convert frame to grayscale for face detection (once per frame)
  gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

  # Detect faces in the frame
#   faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)
  faces = detector(gray)

  # Loop over the detected faces
  for face in faces:
        # Predict facial landmarks
        landmarks = predictor(gray, face)
        
        # Draw facial landmarks on the frame
        for n in range(0, 68):
            x = landmarks.part(n).x
            y = landmarks.part(n).y
            cv2.circle(frame, (x, y), 1, (0, 255, 0), -1)  # Draw a small circle for each landmark

            
  # Capture logic (moved outside the loop for single execution)
  if len(faces) > 1:
    face_detected_count+=1
    print("Multiple faces detected! Photo captured.",face_detected_count)
    current_datetime = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    capture_folder = 'Face_Capture'
    if not os.path.exists(capture_folder):
      os.makedirs(capture_folder)
    photo_path = os.path.join(capture_folder, f"multiple_faces_detected_{current_datetime}.jpg")
    cv2.imwrite(photo_path, frame)
    time.sleep(20)

  return frame
