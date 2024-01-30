import tkinter as tk
from tkinter import ttk


root = tk.Tk()
root.title("Tabbed Notebook Example")
notebook = ttk.Notebook(root)
notebook.grid(column=0, row=0, sticky='N')
tab1 = ttk.Frame(notebook)
tab2 = ttk.Frame(notebook)

notebook.add(tab1, text='Tab 1')
notebook.add(tab2, text='Tab 2')


root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)


# mainframe = ttk.Frame(root, padding=(3, 3, 12, 12))  # padding= W, N, E, S
# mainframe.grid(column=0, row=0, sticky='N,W,E,S')



# root.columnconfigure(0, weight=1)
# root.rowconfigure(0, weight=1)

# feet = tk.StringVar()
# feet_entry = ttk.Entry(mainframe, width=7, textvariable=feet)
# feet_entry.grid(column=2, row=1, sticky='W,E')

# meters = tk.StringVar()
# ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky='W,E')

# ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=3, sticky='W')

# ttk.Label(mainframe, text="feet").grid(column=3, row=1, sticky='W')
# ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky='E')
# ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky='W')

# # Add padding to all children of mainframe:
# for child in mainframe.winfo_children():
#     child.grid_configure(padx=5, pady=5)

# feet_entry.focus()

# root.bind("<Return>", calculate)


root.mainloop()
