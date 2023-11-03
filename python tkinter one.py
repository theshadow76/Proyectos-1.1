import tkinter
import subprocess
from tkinter import Tk
from tkinter import Button
from subprocess import call

def searcher():
    call("python", "E:\\coding\\python\\python tkinter one_searcher.py")

window = Tk()
window.geometry("800x800")

btn_one = Button(window, text='google searcher',command=searcher)
btn_one.pack()

window.mainloop()