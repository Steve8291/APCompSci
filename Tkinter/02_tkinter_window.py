import tkinter as tk
from tkinter import ttk

root = tk.Tk()

# Add a Window Title:
root.title("This is My Window Title")

# Set the window size:
root.geometry('600x400')
# Change the location of the window:
# root.geometry('600x400+100+100')

# Create a Label:
message = ttk.Label(root, text="Hello, World!")
message.grid()


root.mainloop()
