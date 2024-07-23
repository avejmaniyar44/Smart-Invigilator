import tkinter as tk
from tkinter import messagebox
import random

class MCQTestApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Board Exam MCQ Test")
        
        self.sections = [
            {
                "name": "Physics",
                "questions": [
                    {
                        "question": "What is the SI unit of force?",
                        "options": ["Newton", "Watt", "Joule", "Pascal"],
                        "correct_answer": "Newton"
                    },
                    {
                        "question": "What is the SI unit of electric charge?",
                        "options": ["Ampere", "Ohm", "Volt", "Coulomb"],
                        "correct_answer": "Coulomb"
                    }
                ]
            },
            {
                "name": "Chemistry",
                "questions": [
                    {
                        "question": "What is the chemical formula of water?",
                        "options": ["H2O", "CO2", "NaCl", "CH4"],
                        "correct_answer": "H2O"
                    },
                    {
                        "question": "Which gas is known as laughing gas?",
                        "options": ["Nitrous Oxide", "Carbon Dioxide", "Oxygen", "Nitrogen"],
                        "correct_answer": "Nitrous Oxide"
                    }
                ]
            }
        ]
        
        # Shuffle questions in each section
        for section in self.sections:
            random.shuffle(section["questions"])
        
        self.current_section_index = 0
        self.current_question_index = 0
        self.score = 0
        
        self.question_label = tk.Label(master, text="", wraplength=400, justify="center")
        self.question_label.pack()
        
        self.option_var = tk.StringVar()
        self.option_buttons = []
        for i in range(4):
            option_button = tk.Radiobutton(master, text="", variable=self.option_var, value="", command=self.select_option)
            self.option_buttons.append(option_button)
            option_button.pack()
        
        self.next_button = tk.Button(master, text="Next", command=self.next_question)
        self.next_button.pack()
        
        self.section_label = tk.Label(master, text=f"Section: {self.sections[self.current_section_index]['name']}")
        self.section_label.pack()
        
        self.display_question()
        
    def display_question(self):
        section = self.sections[self.current_section_index]
        question_data = section["questions"][self.current_question_index]
        self.question_label.config(text=question_data["question"])
        for i, option in enumerate(question_data["options"]):
            self.option_buttons[i].config(text=option, value=option)
        
    def select_option(self):
        pass
    
    def next_question(self):
        selected_option = self.option_var.get()
        correct_answer = self.sections[self.current_section_index]["questions"][self.current_question_index]["correct_answer"]
        
        if selected_option == "":
            messagebox.showerror("Error", "Please select an option")
            return
        
        if selected_option == correct_answer:
            self.score += 1
        
        self.current_question_index += 1
        if self.current_question_index < len(self.sections[self.current_section_index]["questions"]):
            self.display_question()
        else:
            self.current_question_index = 0
            self.current_section_index += 1
            if self.current_section_index < len(self.sections):
                self.section_label.config(text=f"Section: {self.sections[self.current_section_index]['name']}")
                self.display_question()
            else:
                messagebox.showinfo("End of Test", f"You have completed the test!\nYour score is: {self.score}/{sum(len(section['questions']) for section in self.sections)}")
                self.master.destroy()

def main():
    root = tk.Tk()
    app = MCQTestApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()