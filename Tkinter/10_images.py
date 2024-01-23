import tkinter as tk
from tkinter import ttk

# This will only allow you to use an image once.
# If you want to be able to display the same image twice you will need to create classes for each image.
# class Pig(tk.Frame):

# Then in MainApplication you would create a Pig object with:
# self.pig = Pig()
# self.pig.grid(...)


class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        # Create a text label
        self.message_var = tk.StringVar()
        self.message_var.set('Welcome to the Animal Game.\nClick "Play" to begin.')
        message_label = ttk.Label(self, textvariable=self.message_var, justify='center', font=('Arial', 25))
        message_label.grid(row=0, column=1, columnspan=2, padx=5, pady=20)

        # ### Pig
        # Must attach image to `self` or it will be garbage collected outside of class or function
        self.pig_image = tk.PhotoImage(file='./10_assets/pig128.png')
        # Size of canvas and also size of image
        self.pig_canvas = tk.Canvas(self, width=128, height=128)
        # Place pig_image into pig_canvas. Must be half of canvas size to fit perfectly: 128/2 = 64
        self.pig_canvas.create_image(64, 64, image=self.pig_image, anchor='center')
        # Attach image canvas to MainApplication Frame
        self.pig_canvas.grid(row=1, column=1, pady=15, padx=80)

        # ### Octopus
        self.octopus_image = tk.PhotoImage(file='./10_assets/octopus128.png')
        self.octopus_canvas = tk.Canvas(self, width=128, height=128)
        self.octopus_canvas.create_image(64, 64, image=self.octopus_image, anchor='center')
        self.octopus_canvas.grid(row=1, column=2, pady=15, padx=80)

        # ### T-rex
        self.trex_image = tk.PhotoImage(file='./10_assets/trex128.png')
        self.trex_canvas = tk.Canvas(self, width=128, height=128)
        self.trex_canvas.create_image(64, 64, image=self.trex_image, anchor='center')

        # Button
        play_button = ttk.Button(self, text='Play', command=self.change_image)
        play_button.grid(row=2, column=1, columnspan=2, pady=20)

    # Button Command Methods
    def change_image(self):
        self.trex_canvas.grid(row=1, column=2, pady=15, padx=80)
        self.message_var.set("Winner is Tyrannosaurus Rex!")

    def game_reset(self):
        self.message_var.set('Welcome to the Animal Game.\nClick "Play" to begin.')
        self.pig_canvas.grid_forget()
        self.octopus_canvas.grid_forget()
        self.trex_canvas.grid_forget()

    def rotate_images_left(self):
        # Adding a delay before displaying image
        self.after(1000, self.trex_canvas.grid(row=1, column=1, pady=15, padx=80))


root = tk.Tk()
root.title("My Cool Photo Display Thing")
# Allow root window to stretch
root.columnconfigure(0, weight=1)
root.columnconfigure(2, weight=1)

app = MainApplication(root)
app.grid(column=1, sticky='n,s,e,w')

root.mainloop()
