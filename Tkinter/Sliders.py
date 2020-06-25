from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from tkinter import filedialog

root = Tk()
root.title("Sliders")
root.iconbitmap()
root.geometry("400x400")

vertical = Scale(root, from_=0, to=100)
vertical.pack()

horizontal = Scale(root, from_=0, to=200, orient=HORIZONTAL)
horizontal.pack()

my_label = Label(root, text=horizontal.get()).pack()

def clickable():
    my_label = Label(root, text=horizontal.get()).pack()

button = Button(root, text="Click Me!", command=clickable).pack()



root.mainloop()