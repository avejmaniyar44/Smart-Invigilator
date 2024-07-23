import cv2
import tkinter as tk
from PIL import Image, ImageTk

class CameraApp:
    def __init__(self, window, window_title):
        self.window = window
        self.window.title(window_title)
        
        # Open the camera
        self.cap = cv2.VideoCapture(0)
        
        # Create a canvas that can fit the above video source size
        self.canvas = tk.Canvas(window, width=self.cap.get(cv2.CAP_PROP_FRAME_WIDTH), height=self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        self.canvas.grid(row=0, column=0)
        
        # Button to close the window
        self.close_button = tk.Button(window, text="Close", command=self.close)
        self.close_button.grid(row=1, column=0, pady=5)
        
        # After setting up the GUI, call the update method periodically to keep the video frames updating
        self.update()

    def update(self):
        # Get a frame from the video source
        ret, frame = self.cap.read()
        
        if ret:
            # Convert the frame to RGB format
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            # Convert the frame to PIL format
            self.photo = ImageTk.PhotoImage(image=Image.fromarray(frame_rgb))
            # Display the frame in the Tkinter window
            self.canvas.create_image(0, 0, image=self.photo, anchor=tk.NW)
        
        # Call the update method after 15 milliseconds
        self.window.after(15, self.update)

    def close(self):
        # Release the camera and close the Tkinter window
        self.cap.release()
        self.window.destroy()

# Create a Tkinter window
root = tk.Tk()
# Create the CameraApp instance
app = CameraApp(root, "Camera Feed")
# Start the Tkinter event loop
root.mainloop()