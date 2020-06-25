from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Image Viewer")
root.iconbitmap("G:\Tkinter\Images\MyIcon.ico")


image1 = ImageTk.PhotoImage(Image.open("G:\\Tkinter\\Images\\1__T_tWFGY29J6MEKek1vBaw.png"))
image2 = ImageTk.PhotoImage(Image.open("G:\\Tkinter\\Images\\adobee.png"))
image3 = ImageTk.PhotoImage(Image.open("G:\\Tkinter\\Images\\Apple.png"))

image_list = [image1, image2, image3]

# Status bar
status = Label(root, text='Image 1 of ' + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)


def forward(image_number):
    global my_label
    global button_for
    global button_back

    my_label.grid_forget()
    my_label = Label(image=image_list[image_number])
    button_for = Button(root, text='>>', command=lambda: forward(image_number + 1))
    if image_number == len(image_list) - 1:
        button_for = Button(root, text='>>', state=DISABLED)
    
    button_back = Button(root, text='<<', command=lambda: back(image_number - 1))
    print(image_number)
    status = Label(root, text='Image {} of {}'.format(str(image_number + 1), str(len(image_list))), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W + E)    
    button_back.grid(row=1, column=0)
    button_exit.grid(row=1, column=1)
    button_for.grid(row=1, column=2)

    my_label.grid(row=0, column=0, columnspan=3)


def back(image_number):
    global my_label
    global button_for
    global button_back

    my_label.grid_forget()
    my_label = Label(image=image_list[image_number])
    button_for = Button(root, text='>>', command=lambda: forward(image_number + 1))
    button_back = Button(root, text='<<', command=lambda: back(image_number - 1))
    
    if image_number == 0:
        button_back = Button(root, text='<<', state=DISABLED)
    print(image_number)

    status = Label(root, text='Image {} of {}'.format(str(image_number + 1), str(len(image_list))), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W + E)    
    button_back.grid(row=1, column=0)
    button_exit.grid(row=1, column=1)
    button_for.grid(row=1, column=2)

    my_label.grid(row=0, column=0, columnspan=3)



# my_label = Label(image=image1)
# my_label.grid(row=0, column=0, columnspan=3)

sb_v = Scrollbar(root)
sb_v.grid(row=0, column=0, sticky=E)

sb_h = Scrollbar(root)
sb_h.grid(row=0, column=0, sticky=S)


my_label = Listbox(root, yscrollcommand=sb_v, xscrollcommand=sb_h)
my_label.grid(row=0, column=0, columnspan=3)

sb_v.config(command=my_label.yview)
sb_h.config(command=my_label.xview)


button_back = Button(root, text='<<', command=back, state=DISABLED)
button_exit = Button(root, text='Exit Program', command=root.quit)
button_for = Button(root, text='>>', command=lambda: forward(1))

button_back.grid(row=1, column=0)
button_exit.grid(row=1, column=1)
button_for.grid(row=1, column=2, pady=10)
status.grid(row=2, column=0, columnspan=3, sticky=W + E)

root.mainloop()