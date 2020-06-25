from tkinter import *
from tkinter import Scrollbar

root = Tk()
root.title("ScrollBar")
root.geometry("400x400")
sb_vertical = Scrollbar(root, orient=VERTICAL, jump=0)
sb_vertical.pack(side=RIGHT, fill=Y)

sb_horizontal = Scrollbar(root, orient=HORIZONTAL)
sb_horizontal.pack(side=BOTTOM, fill=X)

label = Listbox(root, yscrollcommand=sb_vertical.set, width=400)

for i in range(30):
    label.insert(END, str(i + 1) + " Hello World")    

label.pack(side=LEFT, fill=BOTH)
sb_vertical.config(command=label.yview)

root.mainloop()