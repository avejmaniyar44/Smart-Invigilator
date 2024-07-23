import tkinter as tk

class CountdownTimer:
    def __init__(self, label, total_seconds):
        self.label = label
        self.total_seconds = total_seconds
        self.remaining_seconds = total_seconds
        self.update_display()

    def update_display(self):
        hours, remainder = divmod(self.remaining_seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        self.label.config(text="Time Remaining: {:02d}:{:02d}:{:02d}".format(hours, minutes, seconds))
        if self.remaining_seconds > 0:
            self.remaining_seconds -= 1
            self.label.after(1000, self.update_display)
        else:
            self.label.config(text="Time's up!")

def create_countdown_timer(label, total_seconds):
    return CountdownTimer(label, total_seconds)