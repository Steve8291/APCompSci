import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("My Application Title")
root.geometry("300x200")
root.eval('tk::PlaceWindow . center')  # centers window on screen


# Tkinter variable clases.
# Allow connecting directly to tkinter widgets
# When the variable value changes the widget automatically updates
school_name_var = tk.StringVar()
mascot_var = tk.StringVar()
display_var = tk.StringVar()


# Function to attach to button
# Runs when button is clicked
def on_enter(event='none'):
    # Method for accessing tkinter variables
    name = school_name_var.get()
    mascot = mascot_var.get()
    print(f"Name: {name}")
    print(f"Mascot: {mascot}")
    # Method for setting tkinter variables
    school_name_var.set("")
    mascot_var.set("")

    display_text = f"{name} {mascot}"
    display_var.set(display_text)


# Tkinter Labels to display in root window
school_name_label = ttk.Label(root, text="School Name:")
mascot_label = ttk.Label(root, text="Mascot:")
display_label = ttk.Label(root, textvariable=display_var)

# Tkinter Entry Boxes
school_name_entry = ttk.Entry(root, textvariable=school_name_var)
# mascot_entry = ttk.Entry(root, textvariable=mascot_var)
mascot_entry = ttk.Entry(root, textvariable=mascot_var, show='*')  # Hide user submission

# Button
enter_button = ttk.Button(root, text="Enter", command=on_enter)
mascot_entry.bind('<Return>', on_enter)

# Placing items into root window with .grid()
# school_name_label.grid(row=0, column=0, sticky='e')
school_name_label.grid(row=0, column=0, sticky='e', pady=20)
mascot_label.grid(row=1, column=0, sticky='e')
school_name_entry.grid(row=0, column=1)
mascot_entry.grid(row=1, column=1)
enter_button.grid(row=2, column=1, sticky='e')
# columnspan is the number of columns the widget occupies, default is 1
display_label.grid(row=3, column=0, columnspan=2, sticky='w')

# Infinite Loop to keep gui running
root.mainloop()
