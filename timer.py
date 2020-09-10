""" Importing time and Tkinter """
import time
import tkinter as tk
""" Showing message windows """
from tkinter import Entry, Label, messagebox

# Main window
root = tk.Tk()
root.title("Timer")

# First row
minutes_label = Label(root, text="Minutes:")
minutes_entry = Entry(root)

minutes_label.grid(row=0, column=0, padx=5, pady=5)
minutes_entry.grid(row=0, column=1, pady=5, padx=5)

if __name__ == "__main__":
    root.mainloop()
