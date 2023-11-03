import tkinter
from tkinter import Tk

window = Tk()

window.geometry("600x600")

theme = window.configure(bg="white")
v1 = 0

def btn1click():
    window.configure(bg="#212121")

btn1 = tkinter.Button(window, text="Change Theme", command=btn1click())
btn1.pack()



window.state('zoomed')

# lo mas arriba
window.title('Shadow PDF Reader')

# menustrip


window.mainloop()