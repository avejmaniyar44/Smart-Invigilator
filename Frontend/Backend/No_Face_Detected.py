import cv2
import time

# Initialize the camera
cap = cv2.VideoCapture(0)

# Initialize the face detection classifier
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Variables for tracking time
start_time = time.time()
face_detected = False

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Convert frame to grayscale for face detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the grayscale frame
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    if len(faces) > 0:
        # If faces are detected, update time and flag
        start_time = time.time()
        face_detected = True
    else:
        # If no faces detected and more than 10 seconds have passed, capture photo
        if time.time() - start_time > 10 and not face_detected:
            cv2.imwrite('no_face_detected.jpg', frame)
            print("No face detected for more than 10 seconds. Photo captured.")
            break

    # Display the frame
    cv2.imshow('Frame', frame)

    # Check for 'q' key to exit loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
