# sera un text editor
# import
import tkinter
from tkinter import Button, PanedWindow, Tk
import webbrowser

window = Tk()
window.state('zoomed')
window.configure(bg="#212121")

# Los defs
def LoginInWebSite(): #Login
    webbrowser.open("https://theshadowtech.wixsite.com/website")
def ExitBtn():
    window.destroy

login = Button(window, background="white", border=5, width=10, text="Login", font=8, command=LoginInWebSite)
login.grid(row=15, column=15)
login.place(x=5, y=3)

Exit = Button(window, width=10, background="white", border=5, text="Exit", font=8, command=window.destroy)
Exit.place(x=1810, y=3)

pn0 = PanedWindow(window,
    width=1, height=1
)

pn1 = PanedWindow(window, 
    width=300, height=300, background="white"
)

window.mainloop()
