import tkinter
from tkinter import Tk
from tkinter import Button, Image

folder_selected = None

window = Tk()
window.title("title")
window.state("zoomed")
window.configure(background="white")

# los defs
# selecte folder
def select_folder():
    import tkinter.filedialog
    folder_selected = tkinter.filedialog.askdirectory()
    print(folder_selected)
    label1 = tkinter.Label(window, text=folder_selected, fg="black", width="15")
    label1.place(x=150, y=10)
    def image_selected():
        img_ = tkinter.filedialog.askopenfilename(initialdir="/", title="Select file", filetypes=(("photo files", "*.png"), ("photo files", "*.png*")))
    img = Image(image_selected())

btn1 = Button(window, text="Select Folder", fg="black", width="15", command=select_folder)
btn1.place(x=30, y=10)

window.mainloop() 