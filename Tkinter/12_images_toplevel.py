import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image

# sudo apt install python3-pil python3-pil.imagetk
# sudo pip3 install Pillow
# sudo pip3 install types-Pillow

# Create an instance of tkinter window
root = tk.Tk()

# Define the geometry of the window
# You will want to adjust this to fit your images and other widgets
root.geometry("1024x1024")
root.title("Main Root Window")

top = tk.Toplevel()
top.title("TopLevel Window")
top.geometry("1024x1024")
top.columnconfigure(0, weight=1)
top.columnconfigure(3, weight=1)
top.rowconfigure(0, weight=1)
top.rowconfigure(3, weight=1)

frame = ttk.Frame(root, width=600, height=400)
frame.grid()

# Create an object of tkinter ImageTk
# You will need to resize your image using an app like Gimp
# to make it the size you want.
img = ImageTk.PhotoImage(Image.open("./12_assets/AppetizerWreath.jpg"))
img2 = ImageTk.PhotoImage(Image.open("./12_assets/forest.jpg"))
img3 = ImageTk.PhotoImage(Image.open("./12_assets/BaconAppetizers.jpg"))

# Create a Label Widget to display the Image
label = ttk.Label(top, image=img)
label2 = ttk.Label(top, image=img2)
label3 = ttk.Label(top, image=img3)

# Grid the label containing the image where you want it
label.grid(row=1, column=1)
label2.grid(row=2, column=3)
label3.grid(row=1, column=2)

root.mainloop()
