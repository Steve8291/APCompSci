import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("My Application Title")
root.eval('tk::PlaceWindow . center')  # centers window

file_path = './11_assets/random.txt'


def on_enter(event=None):
    # Create a new tk.Toplevel to add widgets to
    file_window = tk.Toplevel()
    file_window.geometry("1000x800")
    # Creating a new tk.Text widget
    textbox = tk.Text(file_window, wrap=tk.WORD, padx=20, pady=20, font=('Courier', 20))
    textbox.pack(expand=True, fill='both')

    # Using `with open` will automatically close the file when program exits
    with open(file_path, 'r') as f:
        textbox.insert(tk.INSERT, f.read())

    # Don't allow editing after inserting text
    textbox.configure(state=tk.DISABLED)


# Create widgets
msg_label = ttk.Label(root, text="Would you like to see my file contents?")
enter_button = ttk.Button(root, text="Enter", command=on_enter)

# Place widgets in root window
msg_label.grid(row=0, column=0, padx=20, pady=20)
enter_button.grid(row=2, column=1, sticky='e', padx=10, pady=10)

root.mainloop()
