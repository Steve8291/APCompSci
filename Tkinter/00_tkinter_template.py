"""
A simple demo of the basic Tkinter widgets. This can be used as a skeleton for a simple GUI applications.
"""
import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter.messagebox import showinfo


root = tk.Tk()
root.title("Tkinter Widget Demo")

# Frame widget container
window = ttk.Frame()
window.grid(padx=20, pady=20)

# Label widget
label = ttk.Label(window, text="This is my Label!")

# Entry widget
entry_var = tk.StringVar()
entry = ttk.Entry(window, textvariable=entry_var)
entry.focus()  # Puts the cursor into the entry field

# Button widget
def on_button():
    print("You Clicked the Button!")
    print(entry_var.get())

button = ttk.Button(window, text="My Button", command=on_button)


# Messagebox showinfo widget
def combobox_showinfo(event):
    showinfo(title="Combobox Selected!", message=f"You selected {combobox_var.get()}")
    
    print(combobox_var.get())

# Combobox widget:
def combobox_changed(event):
    print(event)

combobox_list = ('value 1', 'value 2', 'value 3')
combobox_var = tk.StringVar()
combobox = ttk.Combobox(window, textvariable=combobox_var)
combobox['values'] = combobox_list
combobox.bind('<<ComboboxSelected>>', combobox_changed)





# Grid Widgets into Frame
label.grid(row=0, column=0)
entry.grid(row=1, column=0)
button.grid(row=5, column=1)
combobox.grid(row=2, column=1)

root.mainloop()
