import tkinter
from tkinter import Button, Tk

window = Tk()
window.geometry("1600x800")
window.configure(bg="#212121")

def close():
    window.quit()

btn1 = Button(text="X", background="#212121", command=close())
btn1.pack(padx=100, pady=7)

window.mainloop()