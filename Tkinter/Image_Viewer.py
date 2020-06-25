from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Image Viewer")
root.iconbitmap("G:\\Tkinter\\unnamed.png")

image1 = ImageTk.PhotoImage(Image.open("G:\\Tkinter\\Images\\1__T_tWFGY29J6MEKek1vBaw.png"))
image2 = ImageTk.PhotoImage(Image.open("G:\\Tkinter\\Images\\adobee.png"))
image3 = ImageTk.PhotoImage(Image.open("G:\\Tkinter\\Images\\Apple.png"))

image_list = [image1, image2, image3]

my_label = Label(image=image1)
my_label.grid(row=0, column=0, columnspan=3)


def forward(number):
    global my_label
    global button_for
    global button_bac
    
    my_label.grid_forget()
    my_label = Label(image=image_list[number-1])
    
    button_for = Button(root, text=">>", command=lambda: forward(number+1))
    button_bac = Button(root, text="<<", command=lambda: back(number-1))

    if number == len(image_list):
       button_for = Button(root, text=">>", state=DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    button_bac.grid(row=1, column=0)
    button_for.grid(row=1, column=2)


def back(number):
    global my_label
    global button_for
    global button_bac

    my_label.grid_forget()
    my_label = Label(image=image_list[number-1])
    button_for = Button(root, text=">>", command=lambda: forward(number+1))
    button_bac = Button(root, text="<<", command=lambda: back(number-1))

    if number == 1:
        button_bac = Button(root, text="<<", state=DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    button_bac.grid(row=1, column=0)
    button_for.grid(row=1, column=2)



button_back = Button(root, text="<<", command=lambda: back(2))
button_quit = Button(root, text="Exit!", command=root.quit)
button_forward = Button(root, text=">>", command=lambda: forward(2))

button_back.grid(row=1, column=0)
button_forward.grid(row=1, column=2)
button_quit.grid(row=1, column=1)

root.mainloop()