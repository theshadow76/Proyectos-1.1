import tkinter
from tkinter import Button, Tk


window = Tk()
window.title("solve ecuations")
window.geometry("1000x1000")
window.state('zoomed')
window.configure(bg="white")

# los defs
def login_page():
    import login

btn1 = Button(window, text="login", width=15, height=3, font=("Arial"), command=login_page)
btn1.grid(column=3, row=0)

window.mainloop()