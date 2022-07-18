from tkinter import Tk
from tkinter import Label
import time
import sys

master = Tk()
master.title("Digital Clock")


def get_time():
    timevar = time.strftime("%I:%M:%S %p")
    clock.config(text=timevar)
    clock.after(200, get_time)


Label(master, font=("Arial", 30), text="Digital Clock",
      fg="white", bg="green").pack()
clock = Label(master, font=("Calibre", 90), bg="gray", fg="white")
clock.pack()

get_time()

master.mainloop()
