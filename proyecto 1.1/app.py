import tkinter
from tkinter import *
from tkinter import Tk
from tkinter import filedialog

window = Tk()
window.title("ShadowNotes")
window.geometry("500x500")
window.state('zoomed')
window.configure(background='white')

txt_writer = Text(window, width=50, height=10)
txt_writer.pack()

# los defs
def open_file(): # open a txt file
    window.filename = filedialog.askopenfilename(initialdir="/", title="Select file", filetypes=(("Text files", "*.txt"), ("All files", "*.*")))
    print(window.filename)
# save txt file
def save_file():
    window.filename = filedialog.asksaveasfilename(initialdir="/", title="Select file", filetypes=(("Text files", "*.txt"), ("All files", "*.*")))
    print(window.filename)
# create txt file
def create_file():
    window.filename = filedialog.asksaveasfilename(initialdir="/", title="Select file", filetypes=(("Text files", "*.txt"), ("All files", "*.*")))
    print(window.filename)


menubar = Menu(window)
filemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New", command=create_file)
filemenu.add_command(label="save as", command=save_file)
filemenu.add_command(label="open", command=open_file)

filemenu.add_separator()

window.config(menu=menubar)
window.mainloop()