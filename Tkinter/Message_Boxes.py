from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Message Box")
# root.iconbitmap("G:\Tkinter\Images\MyIcon.ico")

#    Types of message boxes.
# showinfo = returns "ok" when clicked ok,
# showwarning = returns "ok" when clicked ok,
# showerror = returns "ok" when clicked ok,
# askquestion = returns "yes" when click yes and "no" when click no,
# askokcancel = returns 1 when click yes and 0 when click no,
# askyesno = returns 1 when click yes and 0 when click no


def clickable():
    temp = messagebox.showerror("Message Box", "This is a showinfo Message Box!")
    print(type(temp), temp)
    myLabel = Label(root, text=temp).pack()


myLabel = Label(root, text="This is a Message Box!").pack()
myButton = Button(root, text="Click Me!", command=clickable).pack()


root.mainloop()