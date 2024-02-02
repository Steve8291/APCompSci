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
label = ttk.Label(window, text="This is my Label. It spans 2 columns!")


# Entry widget
entry_var = tk.StringVar()
entry = ttk.Entry(window, textvariable=entry_var)
entry.focus()  # Puts the cursor into the entry field


# Button widget
def on_button():
    print("You Clicked the Button!")
    print(entry_var.get())

button = ttk.Button(window, text="My Button", command=on_button)


# Button widget with lambda function
# Allows you to pass parameters to a function
def on_lambutton(event):
    print(event)
    print(f"The combobox is: {combobox_var.get()}")

event_type = "My specialevent"
lambutton = ttk.Button(window, text="LamButton", command=lambda: on_lambutton(event_type))


# Combobox showinfo widget
# This is triggered by changing the combobox widget below
def combobox_changed(event):
    print(combobox_var.get())
    showinfo(title="Combobox Selected!", message=f"You selected {combobox_var.get()}")


# Combobox widget
combobox_list = ('value 1', 'value 2', 'value 3')
combobox_var = tk.StringVar()
combobox = ttk.Combobox(window, textvariable=combobox_var, justify='center', width=10, state='readonly')
combobox['values'] = combobox_list
combobox.current(0)  # Index number of list to set default to
combobox.bind('<<ComboboxSelected>>', combobox_changed)


# Labelframe container
labelframe = ttk.Labelframe(window, text="My Frame")


# Radiobutton widget
def radio_selection():
    selection = f"You selected: {radio_var.get()}"
    print(radio_var.get())
    mess_var.set(selection)


radio_var = tk.StringVar()
mess_var = tk.StringVar()
radio_labels = ('Selection A', 'Selection B', 'Selection C', 'Selection D')
for i in radio_labels:
    ttk.Radiobutton(labelframe, text=i, variable=radio_var, value=i, command=radio_selection).grid(ipadx=10, ipady=10, sticky='ew')

radio_message = ttk.Label(labelframe, textvariable=mess_var).grid(ipadx=10, ipady=10, sticky='ew')
mess_var.set("Please make a selection")


# Grid Widgets into Frame
label.grid(row=0, column=0, columnspan=2)
entry.grid(row=1, column=0)
button.grid(row=2, column=0)
combobox.grid(row=1, column=1)
lambutton.grid(row=2, column=1)
labelframe.grid(row=3, column=0, padx=15, pady=15)


root.mainloop()
