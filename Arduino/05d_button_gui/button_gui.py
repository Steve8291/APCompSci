#!/usr/bin/env python3

import tkinter
import serial
import threading


# Requires tkinter and pyserial
# sudo pip3 install pyserial
# sudo pip3 install types-pyserial
# sudo apt install python3-tk

com_port = '/dev/cu.usbmodem141224301'

led_on = False


def quit():
    ser.write(bytes('L', 'UTF-8'))
    window.quit()


def switch_led():
    if led_on:
        ser.write(bytes('L', 'UTF-8'))
    else:
        ser.write(bytes('H', 'UTF-8'))


def read_from_port():
    global led_on  # Avoid using global by creating a class here!
    while (ser.is_open):
        # Check if incoming bytes are waiting to be read from the serial input buffer.
        if (ser.in_waiting > 0):
            # Read the bytes and convert from binary array to UTF-8
            incoming_byte = ser.read().decode('utf-8')  # Read one byte
            # print(incoming_byte)
            if incoming_byte == 'L':
                led_on = False
                led_button.config(image=off_image)
            if incoming_byte == 'H':
                led_on = True
                led_button.config(image=on_image)


window = tkinter.Tk()
window.eval('tk::PlaceWindow . center')  # Center the window
window.geometry("210x180")  # set starting size of window
window.configure(bg='#323232')  # set color of window background
window.resizable(None, None)
window.title("Arduino Python GUI")

led_label = tkinter.Label(window, text="LED", font=("Helvetica", 20))
led_label.grid(row=0, column=0, pady=20, padx=20)

ser = serial.Serial(com_port, 9600, timeout=0)  # Ensures non-blocking reads

# Define button images:
on_image = tkinter.PhotoImage(file="toggle_on.png")
off_image = tkinter.PhotoImage(file="toggle_off.png")
led_button = tkinter.Button(window, image=off_image, width=96, height=36, command=switch_led)
led_button.grid(row=0, column=1)
quit_button = tkinter.Button(window, text="Quit", command=quit)
quit_button.grid(row=1, column=1)

thread = threading.Thread(target=read_from_port, daemon=True)
thread.start()
window.mainloop()
