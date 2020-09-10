from functools import total_ordering
import tkinter as tk
""" Showing message windows """
from tkinter.messagebox import showerror
from tkinter import Button, Entry, Label, messagebox

# Main window
root = tk.Tk()
root.title("Timer")

# First row
minutes_label = Label(root, text="Minutes:")
minutes_entry = Entry(root)

minutes_label.grid(row=0, column=0, padx=5, pady=5)
minutes_entry.grid(row=0, column=1, pady=5, padx=5)

# Second row
seconds_label = Label(root, text="Seconds:")
seconds_entry = Entry(root)

seconds_label.grid(row=1, column=0, padx=5, pady=5)
seconds_entry.grid(row=1, column=1, pady=5, padx=5)

# Time label
time_label = Label(root, text="", font=("Arial", 44))

def show_message(_message):
    """ Displays an error message """
    messagebox.showerror("Error", _message)

def start_timer():
    """ Gets the total amount of seconds """
    if seconds_entry.get() == "" and minutes_entry.get() == "":
        show_message("You haven't entered the time!")
    else:
        try:
            minutes = int(minutes_entry.get())
            seconds = int(seconds_entry.get())
        except ValueError:
            show_message("You haven't entered a number!")
            clear_entry()
            return
        
        minutes = int(minutes_entry.get())  
        seconds = int(seconds_entry.get())

        total_seconds = minutes * 60 + seconds

        if seconds > 60:
            show_message("Seconds cannot be larger than 60!")
            clear_entry()
            return

        time_label.grid(row=2, columnspan=2, padx=5, pady=5)

        update_time(total_seconds)

def clear_entry():
    minutes_entry.delete(0, "end")
    seconds_entry.delete(0, "end")

def update_time(total_seconds):
    """ Updates time """
    # Minutes and seconds 
    minutes_ = total_seconds // 60
    seconds_ = total_seconds % 60

    # String representation
    if seconds_ < 10:
        _time = f"{minutes_}:0{seconds_}"
    else:
        _time = f"{minutes_}:{seconds_}"

    time_label.configure(text=_time)

    if total_seconds >= 0:
        total_seconds -= 1
        root.after(1000, lambda: update_time(total_seconds))

# Third row
start_button = Button(root, text="Start", command=start_timer)
start_button.grid(row=3, columnspan=2, padx=5, pady=5)

if __name__ == "__main__":
    root.mainloop()
