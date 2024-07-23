import tkinter as tk
from tkinter import messagebox
import json

class QuestionWindow:
    def __init__(self, parent, json_file):
        self.parent = parent
        self.frame = tk.Frame(parent, width=740, height=500)
        self.frame.grid_propagate(False)
        self.frame.grid(row=1, column=1, columnspan=3, rowspan=2, sticky="nsew")

        self.load_questions(json_file)
        self.user_answers = [-1] * len(self.questions)
        self.current_question = 0

        self.create_widgets()
        self.show_question()

    def load_questions(self, json_file):
        with open(json_file, 'r') as file:
            self.questions = json.load(file)

    def create_widgets(self):
        self.question_label = tk.Label(self.frame, text="", font=("Arial", 16), wraplength=700)
        self.question_label.pack(pady=20)

        self.var = tk.IntVar()

        self.radio_buttons = []
        for i in range(4):
            rb = tk.Radiobutton(self.frame, text="", variable=self.var, value=i, font=("Arial", 14), wraplength=700)
            rb.pack(anchor=tk.W, padx=100, pady=30)
            rb.pack(anchor='w')
            self.radio_buttons.append(rb)

        self.nav_frame = tk.Frame(self.frame)
        self.nav_frame.pack(pady=10)

        self.prev_button = tk.Button(self.nav_frame, text="Back", command=self.prev_question, bg='#57a1f8', fg='white', border=0)
        self.prev_button.grid(row=0, column=0, padx=(0, 380))  # Adjust padx to set distance from the next button

        # Place Next button
        self.next_button = tk.Button(self.nav_frame, text="Next", command=self.next_question, bg='#57a1f8', fg='white', border=0)
        self.next_button.grid(row=0, column=1)

    def show_question(self):
        question_data = self.questions[self.current_question]
        question = question_data["question"]
        options = question_data["options"]

        self.question_label.config(text=question)
        for i, option in enumerate(options):
            self.radio_buttons[i].config(text=option)

        if self.user_answers[self.current_question] != -1:
            self.var.set(self.user_answers[self.current_question])
        else:
            self.var.set(-1)

    def next_question(self):
        if self.var.get() == -1:
            messagebox.showwarning("Warning", "Please select an option!")
            return

        self.user_answers[self.current_question] = self.var.get()
        if self.current_question < len(self.questions) - 1:
            self.current_question += 1
            self.show_question()

    def prev_question(self):
        if self.current_question > 0:
            self.current_question -= 1
            self.show_question()