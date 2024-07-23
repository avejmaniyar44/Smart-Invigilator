from tkinter import *
import keyboard
from CountdownTimer import create_countdown_timer
import tkinter as tk
import cv2
from PIL import Image, ImageTk
import Backend.main as bc
from question_window import QuestionWindow


class Dashboard:
          
    def __init__(self, user):
        self.user = user
        self.prev_button = None
        
        self.dashboard_window = Tk()
        self.dashboard_window.title("Dashboard")
        
        self.dashboard_window.state('zoomed')
        self.dashboard_window.configure(bg="#fff")
        
        self.widthx = self.dashboard_window.winfo_screenwidth() 
        self.heightx = self.dashboard_window.winfo_screenheight()
        
        self.frame = Frame(self.dashboard_window, width=self.widthx, height=self.heightx, bg="white")
        self.frame.grid(row=0, column=0)
        
        self.userName = Label(self.frame, text=self.user, bg="white", padx=10, pady=10, font=("Microsoft YaHei UI Light", 12, "bold"))
        self.userName.grid(row=0, column=0, columnspan=2)
        
        self.examName = Label(self.frame, text="Exam Name: B.Tech SL", bg="green", font=("Microsoft YaHei UI Light", 12, "bold"))
        self.examName.grid(row=1, column=0)
        
        self.timer = Label(self.frame, bg="green", padx=10, pady=10, font=("Microsoft YaHei UI Light", 12, "bold"))
        self.timer.grid(row=0, column=5)
        create_countdown_timer(self.timer, 2 * 60 * 60)
        
        # self.cap = cv2.VideoCapture(0)
        # self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 210)
        # self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 150)
        self.canvas = tk.Canvas(self.frame, width=210, height=150)
        # self.canvas.pack()
        self.canvas.grid(row=1, column=5, pady=10)
        
        bc.webcam_processor(self.canvas)
        
        # self.update()
        
        self.button = Button(self.frame, width=39, pady=7, text="Submit", bg='#57a1f8', fg='white', border=0, command=self.exit_dashboard)
        self.button.grid(row=3, column=2)
        
        # self.previous = Button(self.frame, text="Previous", bg='#57a1f8', fg='white', border=0)
        # self.previous.grid(row=3, column=1)
        
        # self.next = Button(self.frame,text="Next", bg='#57a1f8', fg='white', border=0)
        # self.next.grid(row=3, column=3)
        
        self.questionWindow = Frame(self.frame, width=740, height=500)
        self.questionWindow.grid(row=1, column=1, columnspan=3, rowspan=2)
        self.question_window = QuestionWindow(self.frame, 'D:/SEP/Temp/questions.json')
        
        self.questionNumber = Frame(self.frame, bg="white")
        self.questionNumber.grid(row=2, column=0, padx=50)
        
        self.itemValue = 25
        self.buttons = []  # Store references to buttons to access later
        self.count = 1
        
        self.create_buttons()
        
        self.block_keys()
        
        
        self.dashboard_window.mainloop()
        
    def create_buttons(self):
        for row in range(self.itemValue):  # Outer loop for rows
            for column in range(4):  # Inner loop for columns (fixed to 4 columns)
                if self.count <= self.itemValue:
                    # Create canvas
                    canvas = Canvas(self.questionNumber, width=50, height=50, bg='white', highlightthickness=0)
                    canvas.grid(row=row, column=column)

                    # Draw circle
                    x0, y0, x1, y1 = 5, 5, 45, 45
                    circle = canvas.create_oval(x0, y0, x1, y1, outline='black', fill='lightgray', tags="circle")

                    # Add text inside circle
                    canvas.create_text((x0+x1)/2, (y0+y1)/2, text=str(self.count))

                    # Set button 1 to green
                    if self.count == 1:
                        canvas.itemconfig("circle", fill="green")

                    # Add button functionality
                    canvas.bind("<Button-1>", lambda event, num=self.count: self.on_button_click(event, num))

                    self.buttons.append(canvas)  # Store reference to button canvas
                    self.count += 1
    
    def on_button_click(self, event, number):
        # Change the color of the clicked button to green
        canvas = self.buttons[number - 1]
        canvas.itemconfig("circle", fill="green")
        # Change the color of the previously clicked button back to light gray
        if self.prev_button is not None and self.prev_button != number:
            prev_canvas = self.buttons[self.prev_button - 1]
            prev_canvas.itemconfig("circle", fill="lightgray")
        self.prev_button = number
        # Reset the color of button 1 to light gray if it's not the clicked button
        if number != 1:
            self.buttons[0].itemconfig("circle", fill="lightgray")
        print("Button", number, "clicked")
    
    def exit_dashboard(self):
        self.dashboard_window.destroy()
    
    def block_keys(self):
        key='alt'
        keyboard.block_key(key)
        key2='windows'
        keyboard.block_key(key2)
        
    # webcam_processor = WebcamProcessor()
    # webcam_processor.process_frames()

if __name__ == "__main__":
    
    # webcam_processor = WebcamProcessor()
    
    # face_thread = threading.Thread(target=Dashboard("chaitanyagokhe732@gmail.com"))
    # tkinter_thread = threading.Thread(target=webcam_processor.process_frames())

    # tkinter_thread.start()
    # face_thread.start()
    
    Dashboard("chaitanya.gokhe.it@ghriet.raisoni.net")