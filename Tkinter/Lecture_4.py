from tkinter import *

root = Tk()

label1 = Label(root, text="Enter Your Name = ")
label1.grid(row=0, column=0)
# label1.pack()

entry = Entry(root, width=25, borderwidth=5)
entry.grid(row=0, column=1)
# entry.pack()
i = 0
def my_click():
    global i
    label = Label(root, text="Hello " + entry.get())
    i += 2
    label.grid(row=i, column=0)

button = Button(root, text="Click Me!", command=my_click)
button.grid(row=1, column=0)

root.mainloop()