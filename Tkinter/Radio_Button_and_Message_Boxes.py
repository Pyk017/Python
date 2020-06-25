from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Tkinter")
root.iconbitmap("G:\Tkinter\Images\MyIcon.ico")


mylabel1 = Label(root, text="This is a Radio Button and Message Box Combo.").pack()

option = StringVar()
option.set("showinfo")

def clickable(val):
    if val == "showinfo":
        temp = messagebox.showinfo("Box", "Information Box")
        Label(root, text="This is a showinfo Message Box!").pack()
    elif val == "showwarning":
        temp = messagebox.showwarning("Box", "Warning Box")
        Label(root, text="This is showwarning Message Box!").pack()
    elif val == "showerror":
        temp = messagebox.showerror("Box", "Error Box")
        Label(root, text="This is a showerror Message Box!").pack()
    elif val == "askquestion":
        temp = messagebox.askquestion("Box", "Question Box")
        Label(root, text="This is a askquestion Message Box!").pack()
        if temp == "yes":
            Label(root, text="You have clicked Yes!").pack()
        else:
            Label(root, text="You have clicked No!").pack()
    elif val == "askokcancel":
        temp = messagebox.askquestion("Box", "Ok-Cancel Box")
        # print(temp)
        Label(root, text="This is a askokcancel Message Box!").pack()
        if temp == "yes":
            Label(root, text="You have clicked Yes!").pack()
        else:
            Label(root, text="You have clicked No!").pack()
    elif val == "askyesno":
        temp = messagebox.askquestion("Box", "Yes-No Box")
        # print(temp)
        Label(root, text="This is a askyesno Message Box!").pack()
        if temp == "yes":
            Label(root, text="You have clicked Yes!").pack()
        else:
            Label(root, text="You have clicked No!").pack()


Radiobutton(root, text="showinfo", variable=option, value="showinfo").pack(anchor=W)
Radiobutton(root, text="showwarning", variable=option, value="showwarning").pack(anchor=W)
Radiobutton(root, text="showerror", variable=option, value="showerror").pack(anchor=W)
Radiobutton(root, text="askquestion", variable=option, value="askquestion").pack(anchor=W)
Radiobutton(root, text="askokcancel", variable=option, value="askokcancel").pack(anchor=W)
Radiobutton(root, text="askyesno", variable=option, value="askyesno").pack(anchor=W)

button = Button(root, text="Click Me!", command=lambda : clickable(option.get())).pack()

root.mainloop()