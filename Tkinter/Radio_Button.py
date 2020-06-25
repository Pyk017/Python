from tkinter  import *
from PIL import ImageTk, Image

root = Tk()
root.title("This is a Button Tutorial.")
root.iconbitmap("G:\Tkinter\Images\MyIcon.ico")


op = IntVar()
op.set("2")     # default set of data.


def clicked(val):
    # global myLabel
    # myLabel.forget()   # uncomment to see the changes as values overwrite.
    myLabel = Label(root, text=val)
    myLabel.pack()


Radiobutton(root, text="Option 1.", variable=op, value=1).pack()    # if value is integer then it is IntVar(), if it is String then it is StrVar().
Radiobutton(root, text="Option 2.", variable=op, value=2).pack()

myButton = Button(root, text="Click Me!", command=lambda: clicked(op.get()))
myButton.pack()

myLabel = Label(root, text=op.get())
myLabel.pack()

root.mainloop()
