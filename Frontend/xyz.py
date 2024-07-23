import tkinter as tk
from tkinter import messagebox
import cv2
from PIL import Image, ImageTk
import threading

# Sample quiz questions
questions = [
    {
        "question": "What is the capital of France?",
        "options": ["Paris", "London", "Berlin", "Rome"],
        "answer": "Paris"
    },
    {
        "question": "What is the largest mammal?",
        "options": ["Elephant", "Blue Whale", "Giraffe", "Polar Bear"],
        "answer": "Blue Whale"
    },
    # Add more questions as needed
]

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.question_number = 0
        self.score = 0
        self.label_question = tk.Label(root, text="")
        self.label_question.pack()
        self.radio_var = tk.StringVar()
        self.radio_buttons = []
        for i in range(4):
            rb = tk.Radiobutton(root, text="", variable=self.radio_var, value="", command=self.select_option)
            rb.pack(anchor="w")
            self.radio_buttons.append(rb)
        self.label_score = tk.Label(root, text="Score: 0")
        self.label_score.pack()
        self.next_question()

    def next_question(self):
        if self.question_number < len(questions):
            question_data = questions[self.question_number]
            self.label_question.config(text=question_data["question"])
            self.radio_var.set(None)
            for i, option in enumerate(question_data["options"]):
                self.radio_buttons[i].config(text=option, value=option)
            self.question_number += 1
        else:
            messagebox.showinfo("Quiz Completed", f"You have completed the quiz! Your final score is {self.score}")

    def select_option(self):
        selected_option = self.radio_var.get()
        correct_answer = questions[self.question_number - 1]["answer"]
        if selected_option == correct_answer:
            self.score += 1
            messagebox.showinfo("Correct", "Your answer is correct!")
        else:
            messagebox.showerror("Incorrect", f"Sorry, the correct answer is {correct_answer}")
        self.label_score.config(text=f"Score: {self.score}")
        self.next_question()

class FaceRecognitionApp:
    def __init__(self, root):
        self.cap = cv2.VideoCapture(0)
        self.root = root
        self.label = tk.Label(root)
        self.label.pack()
        self.process_frames()

    def process_frames(self):
        while True:
            ret, frame = self.cap.read()
            if ret:
                frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                img = Image.fromarray(frame_rgb)
                imgtk = ImageTk.PhotoImage(image=img)
                self.label.imgtk = imgtk
                self.label.configure(image=imgtk)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        self.cap.release()
        cv2.destroyAllWindows()

# Create the main tkinter window
root = tk.Tk()
root.title("Quiz and Face Recognition")

# Create frames for quiz and face recognition
quiz_frame = tk.Frame(root)
quiz_frame.pack(side=tk.LEFT)

face_frame = tk.Frame(root)
face_frame.pack(side=tk.RIGHT)

# Create instances of both classes within their respective frames
quiz_app = QuizApp(quiz_frame)
face_recognition_app = FaceRecognitionApp(face_frame)

# Run the main tkinter loop
root.mainloop()