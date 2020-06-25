from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("CheckBoxes")
root.iconbitmap("G:\Tkinter\Images\MyIcon.ico")
root.geometry("400x400")
root.geometry("400x400")

def clickable():
    label = Label(root, text=var.get()).pack()
    

var = IntVar()      # It can be StringVar().
c = Checkbutton(root, text="Check this Box!", variable=var, onvalue=1, offvalue=0)
# c = Checkbutton(root, text="Check this Box!", variable=var, onvalue="Yes", offvalue="No")
c.deselect()        # Its Deselects .
c.pack()


button = Button(root, text="Click Me!", command=clickable)
button.pack()

root.mainloop()