""" Importing time and Tkinter """
import time
import tkinter as tk
""" Showing message windows """
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

def show_message(_message):
    messagebox.showerror("Error", _message)

# Third row
start_button = Button(root, text="Start", command=start_timer)
start_button.grid(row=4, columnspan=2, padx=5, pady=5)

if __name__ == "__main__":
    root.mainloop()
