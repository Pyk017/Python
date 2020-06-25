from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from PIL import ImageTk, Image

root = Tk()
root.title()
root.iconbitmap("G:\Tkinter\Images\MyIcon.ico")

def clickable():
    global my_image
    global button
    button.forget()
    root.filename = filedialog.askopenfilename(initialdir="G:/Tkinter/Images", title="Select a File", filetypes=(("PNG files", "*.png"), ("JPEG files", "*.jpg"), ("All files", "*.*")))
    print(root.filename)
    label = Label(root, text=root.filename).pack()
    my_image = ImageTk.PhotoImage(Image.open(root.filename))
    label2 = Label(root, image=my_image).pack()
 

button = Button(root, text="Click Me!", command=clickable)
button.pack()

root.mainloop()