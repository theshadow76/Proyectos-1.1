from tkinter import Tk
import tkinter

window = Tk()

window.configure(background='grey')
window.geometry("500x500")
window.title("REMINI")

btn_one = tkinter.Button(window, text="Run bot")
btn_one.pack(padx=50, pady=50)

window.mainloop()