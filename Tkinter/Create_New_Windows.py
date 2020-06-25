from tkinter import *
from PIL import ImageTk, Image


root = Tk()
root.title("Root Title")
root.iconbitmap("G:\Tkinter\Images\MyIcon.ico")
label_root = Label(root, text="Hello World in Root window").grid(row=0, column=0)

def opens():
    global my_img2
    top = Toplevel()
    top.title("New Window Title")
    label_top = Label(top, text="Hello World in New Window").pack()
    my_img2 = ImageTk.PhotoImage(Image.open("G:\\Tkinter\\Images\\another\\adobee.png"))
    label_top_img = Label(top, image=my_img2).pack()
    button_top = Button(top, text="Click to close this window", command=top.destroy).pack()

my_img1 = ImageTk.PhotoImage(Image.open("G:\\Tkinter\\Images\\another\\Apple.png"))
label_root_img = Label(root, image=my_img1).grid(row=1, column=0)
button_root = Button(root, text="Jump to Second Window", command=opens)
button_root.grid(row=2, column=0)
button_close = Button(root, text="Close!", command=quit)
button_close.grid(row=2, column=1, sticky=W)
root.mainloop()
