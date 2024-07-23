import cv2
import os
import time

# Set the capture interval (in seconds)
CAPTURE_INTERVAL = 10  # for example, 5 seconds

# Initialize the last captured time
last_captured_time = 0

# Flag count to track if mobile phone has been detected.
mobile_detect_count = 0

# Load pre-trained model outside the function (one-time load)
model_path = 'D:/Exam Proctoring System/libraries/frozen_inference_graph.pb'
config_path = 'D:/Exam Proctoring System/libraries/ssd_mobilenet_v2_coco_2018_03_29.pbtxt'
net = cv2.dnn.readNetFromTensorflow(model_path, config_path)

# Set minimum confidence outside the function (avoid redundant assignment)
min_confidence = 0.5

def detect_mobile(frame):
  # global mobile_detected_before
  global mobile_detect_count
  # Pre-process frame once per call (resize)
  blob = cv2.dnn.blobFromImage(frame, size=(300, 300), swapRB=True)
  net.setInput(blob)
  detections = net.forward()

  # Initialize flag inside the function (reset per frame)
  # mobile_detected = False

  # Loop over detections, break early if mobile found
  for detection in detections[0, 0, :, :]:
    confidence = detection[2]
    if confidence > min_confidence:
      class_id = int(detection[1])
      if class_id == 77:  # Check for mobile and previous detection
        # Get coordinates, draw box, label (logic moved inside loop for single execution)
        box = detection[3:7] * [frame.shape[1], frame.shape[0], frame.shape[1], frame.shape[0]]
        (startX, startY, endX, endY) = box.astype("int")
        cv2.rectangle(frame, (startX, startY), (endX, endY), (0, 255, 0), 2)
        cv2.line(frame, (startX, startY), (endX, endY), (0, 255, 0), 2)
        label = f"Mobile: {startX}, {startY}, {endX}, {endY}"
        cv2.putText(frame, label, (startX, startY - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)


        global last_captured_time
        current_time = time.time()
        # print(current_time-last_captured_time,CAPTURE_INTERVAL)
        if current_time - last_captured_time >= CAPTURE_INTERVAL:
          
          # Capture logic (moved inside loop for single capture)
          capture_folder = 'Mobile_Capture'
          if not os.path.exists(capture_folder):
            os.makedirs(capture_folder)
          mobile_detect_count+=1
          print("Mobile phone detected! Photo captured.",mobile_detect_count)
          print("Stop using mobile otherwise kick out form test")
          photo_path = os.path.join(capture_folder, f"mobile_detected_{startX}_{startY}_{endX}_{endY}.jpg")
          cv2.imwrite(photo_path, frame)
          last_captured_time = current_time
        
        # mobile_detected = True
        # mobile_detected_before = True  # Set flag after capture
        break  # Exit loop after finding mobile (optional optimization)

  # Return frame and mobile detection status
  return frame
