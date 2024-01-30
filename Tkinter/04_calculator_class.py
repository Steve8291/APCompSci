import tkinter as tk
from tkinter import ttk


class FeetToMeters:
    def __init__(self, root):
        root.title("Feet to Meters")
        mainframe = ttk.Frame(root, padding=(3, 3, 12, 12))  # padding= W, N, E, S
        mainframe.grid(column=0, row=0, sticky='N,W,E,S')
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

        self.feet = tk.StringVar()
        feet_entry = ttk.Entry(mainframe, width=7, textvariable=self.feet)
        feet_entry.grid(column=2, row=1, sticky='W,E')

        self.meters = tk.StringVar()
        ttk.Label(mainframe, textvariable=self.meters).grid(column=2, row=2, sticky='W,E')

        ttk.Button(mainframe, text="Calculate", command=self.calculate).grid(column=3, row=3, sticky='W')
        ttk.Label(mainframe, text="feet").grid(column=3, row=1, sticky='W')
        ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky='E')
        ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky='W')

        # Add padding to all children of mainframe:
        for child in mainframe.winfo_children():
            child.grid_configure(padx=5, pady=5)

        feet_entry.focus()
        root.bind("<Return>", self.calculate)

    def calculate(self, *args):
        print("You are in function")
        for i in args:
            print(i)
        try:
            value = float(self.feet.get())
            self.meters.set(int(0.3048 * value * 10000.0 + 0.5) / 10000.0)
        except ValueError:
            pass


root = tk.Tk()
FeetToMeters(root)
root.mainloop()
