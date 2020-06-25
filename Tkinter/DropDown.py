from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("DropDown")

clicked = StringVar()
clicked.set("Sunday")


def show():
    label = Label(root, text=clicked.get())
    label.pack()

options = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

drop = OptionMenu(root, clicked, *options)
drop.pack()

button = Button(root, text="Show Selection", command=show)
button.pack()


root.mainloop()
