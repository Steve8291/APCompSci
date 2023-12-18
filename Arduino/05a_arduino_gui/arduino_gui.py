#!/usr/bin/env python3

import tkinter
import serial

# Requires tkinter and pyserial
# sudo pip3 install pyserial
# sudo pip3 install types-pyserial
# sudo apt install python3-tk

com_port = '/dev/cu.usbmodem141224301'  # Check Arduino IDE for port


def led_off():
    ser.write(bytes('L', 'UTF-8'))     # Send serial data to Arduino
    status_var.set("Status: LED OFF")  # Change status_var (immediately updates in window)


def led_on():
    ser.write(bytes('H', 'UTF-8'))
    status_var.set("Status: LED ON")


# `window` will be the parent window to hold all our widgets
window = tkinter.Tk()                    # Constructor to create an object `window` from Tkinter's `Tk` class
window.eval('tk::PlaceWindow . center')  # Center the window
window.geometry("210x180")               # Size of window
window.title("Arduino Python GUI")       # Set window title


# Create a tkinter.StringVar that can be used in `window`
status_var = tkinter.StringVar()
# A tkinter.StringVar can't be added directly to our window. It needs to be part of a Label
# Create a Label attached to `window` with your StringVar in it
status_label = tkinter.Label(window, textvariable=status_var)
status_label.pack()  # Add status_label to window

ser = serial.Serial(com_port, 9600)  # Create a serial object on com_port with baud rate 9600

led_off()  # Call the `led_off()` function to initially turn led off

# Create a colored Button with text attached to `window`
# Set Button to trigger the `led_off()` function: `command=led_off`
on_button = tkinter.Button(
    window, text="ON",
    command=led_on, background='green').pack()  # Pack Button into `window`

off_button = tkinter.Button(
    window, text="OFF",
    command=led_off, background='red').pack()

window.mainloop()  # Starts your applications main loop to wait for mouse and keyboard events.
