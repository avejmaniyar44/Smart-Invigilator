# import cv2
# from Backend.mobile import detect_mobile
# from Backend.face_detection import detect_faces

# class WebcamProcessor:
#     def __init__(self):
#         self.cap = cv2.VideoCapture(0)

#     def process_frames(self):
#         while True:
#             # Capture frame-by-frame
#             ret, frame = self.cap.read()
            
#             # Mirroring the frame
#             frame = cv2.flip(frame, 1)

#             # If frame is successfully captured
#             if ret:
#                 # Detect mobile phones and faces in the frame
#                 frame_with_detections = detect_mobile(frame)
#                 frame_with_detections = detect_faces(frame_with_detections)

#                 cv2.imshow('Frame', frame_with_detections)

#                 # Break the loop if 'q' is pressed
#                 if cv2.waitKey(1) & 0xFF == ord('q'):
#                     break

#         self.cap.release()
#         cv2.destroyAllWindows()

# Instantiate the class and start processing frames
# webcam_processor = WebcamProcessor()
# webcam_processor.process_frames()
import cv2
from PIL import Image, ImageTk
from Backend.mobile import detect_mobile
import tkinter as tk
from Backend.face_detection import detect_faces


def webcam_processor(canvas):
    video_source = 0
    vid = cv2.VideoCapture(video_source)
    
    vid.set(cv2.CAP_PROP_FRAME_WIDTH, 210)
    vid.set(cv2.CAP_PROP_FRAME_HEIGHT, 150)
    
    delay = 10
    
    def update():
        ret, frame = vid.read()
        
        # Mirroring the frame
        frame = cv2.flip(frame, 1)

        if ret:
            frame_with_detections = detect_mobile(frame)
            frame_with_detections = detect_faces(frame_with_detections)
            # print(demo)
            
            # Resize the frame to 210x150 pixels
            frame_resized = cv2.resize(frame_with_detections, (210, 150))
            
            frame_rgb = cv2.cvtColor(frame_resized, cv2.COLOR_BGR2RGB)
            photo = ImageTk.PhotoImage(image=Image.fromarray(frame_rgb))
            canvas.create_image(0, 0, image=photo, anchor=tk.NW)
            canvas.photo = photo

        canvas.after(delay, update)

    update()