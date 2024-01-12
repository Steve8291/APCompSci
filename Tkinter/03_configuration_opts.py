import tkinter as tk
from tkinter import ttk


def button_info():
    print(button['text'])
    button['text'] = 'goodby'
    print(button['text'])
    button.configure(text='HI')
    print(button['text'])
    print('\n')
    print(button.configure())


root = tk.Tk()

button = ttk.Button(root, text='Hello', command=button_info)
button.grid()

root.mainloop()
