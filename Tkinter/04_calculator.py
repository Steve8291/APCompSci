import tkinter as tk
from tkinter import ttk


def calculate(*args):
    print("You are in function")
    for i in args:
        print(i)
    try:
        value = float(feet.get())
        meters.set(int(0.3048 * value * 10000.0 + 0.5) / 10000.0)
    except ValueError:
        pass


root = tk.Tk()
root.title("Convert Feet to Meters")

# Using a themed ttk frame widget inside the root window.
# The root window is unthemed and would display incorrectly.

# mainframe = ttk.Frame(root, padding=(100))  # padding all 12
# mainframe = ttk.Frame(root, padding='3 3 12 12')
mainframe = ttk.Frame(root, padding=(3, 3, 12, 12))  # padding= W, N, E, S
mainframe.grid(column=0, row=0, sticky='N,W,E,S')


# Allows mainframe to stretch to fill root window if resized.
# Also useful if you want different sized columns and rows.
# root.configure(background='red')  # To test
# weight is relative size: weight=2 is twice as wide as weight=1
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

feet = tk.StringVar()
feet_entry = ttk.Entry(mainframe, width=7, textvariable=feet)
feet_entry.grid(column=2, row=1, sticky='W,E')

meters = tk.StringVar()
ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky='W,E')

ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=3, sticky='W')

ttk.Label(mainframe, text="feet").grid(column=3, row=1, sticky='W')
ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky='E')
ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky='W')

# Add padding to all children of mainframe:
for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

# Place the cursor in the feet_entry box:
feet_entry.focus()

# Find the 'return' key to root window with the command 'calculate'
# When hitting 'return' will send an argument to calculate() like:
# <KeyPress event keysym=Return keycode=603979789 x=201 y=328>
root.bind("<Return>", calculate)
# Could also bind it to feet_entry like:
# feet_entry.bind("<Return>", calculate)

root.mainloop()
