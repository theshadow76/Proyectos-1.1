import tkinter
from tkinter import Button, Tk, Text

# variables
bg="white"

class Login():
    window = Tk()
    window.title("Login")
    window.geometry("500x500")
    window.configure(background=bg)

    txt_login = Text(window, width=20, height=1, font=("Arial", 12), bg="white")
    txt_login.grid(column=10, row=20)

    window.mainloop()