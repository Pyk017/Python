from tkinter import *
from PIL import ImageTk, Image
import os

root = Tk()

dir_label = Label(root, text='Enter Directory : ')
dir_label.grid(row=0, column=0)

dir_entry = Entry(root, width=40, borderwidth=6)
dir_entry.grid(row=0, column=1)

def get_image_list(direc):
    files = os.listdir(direc)
    return files


global image_list
image_list = []
def Enter():
    global image_list
    global label
    global button_back
    global button_for
    d = dir_entry.get()
    image_list = get_image_list(d)
    i = 0
    while i < len(image_list):
        if '.png' not in image_list[i] and '.jpg' not in image_list[i]:
            image_list.pop(i)
        else:
            image_list[i] = ImageTk.PhotoImage(Image.open(d + '\\' + image_list[i]))
        i += 1


    # label = None
    label = Label(image=image_list[0])
    label.grid(row=2, column=0, columnspan=3)

    status = Label(root, text="Image 1 of  " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=4, column=0, columnspan=3, sticky=W + E)
    
    def forward(image_number):
        global label
        global button_for
        global button_back    
        # print(label)
        print(label)
        label.grid_forget()
        label = Label(image=image_list[image_number])
        label.grid(row=2, column=0, columnspan=3)
        # print(label)

        button_for = Button(root, text='>>', command=lambda: forward(image_number + 1))
        if image_number == len(image_list) - 1:
            button_for = Button(root, text='>>', state=DISABLED)

        button_back = Button(root, text='<<', command=lambda: back(image_number - 1)).grid(row=3, column=0)
        button_for.grid(row=3, column=2)
        button_exit.grid(row=3, column=1)

        status = Label(root, text="Image {} of  {}".format(str(image_number + 1), str(len(image_list))), bd=1, relief=SUNKEN, anchor=E)
        status.grid(row=4, column=0, columnspan=3, sticky=W + E)


    def back(image_number):
        global label
        global button_for
        global button_back

        label.grid_forget()
        label = Label(image=image_list[image_number])
        label.grid(row=2, column=0, columnspan=3)

        button_for = Button(root, text='>>', command=lambda: forward(image_number + 1))
        button_back = Button(root, text='<<', command=lambda: back(image_number - 1))
        if image_number == 0:
            button_back = Button(root, text='<<', state=DISABLED)

        status = Label(root, text="Image {} of  {}".format(str(image_number + 1), str(len(image_list))), bd=1, relief=SUNKEN, anchor=E)
        status.grid(row=4, column=0, columnspan=3, sticky=W + E)

        button_for.grid(row=3, column=2)
        button_back.grid(row=3, column=0)
        button_exit.grid(row=3, column=1)

    
    

    button_back = Button(root, text='<<', state=DISABLED)
    button_exit = Button(root, text='EXIT', command=root.quit)
    button_for = Button(root, text='>>', command=lambda: forward(1))

    button_back.grid(row=3, column=0)
    button_exit.grid(row=3, column=1)
    button_for.grid(row=3, column=2)


button_enter = Button(root, text='Enter', padx=20, pady=10, command=Enter)
button_enter.grid(row=1, column=0, columnspan=2)


root.mainloop()