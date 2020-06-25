from tkinter import *

root = Tk()

def myClick():
    myLabel = Label(root, text="This is the Button that i have clicked!").grid(row=2, column=0)
    # myLabel.pack()

my_button1 = Button(root, text="Click Me!", padx=50, pady=20, command=myClick, fg="red", bg="yellow")
my_button2 = Button(root, text="Click Me!", padx=50, pady=20, command=myClick, fg="red", bg="yellow")
my_button3 = Button(root, text="Click Me!", padx=50, pady=20, command=myClick, fg="red", bg="yellow")
my_button4 = Button(root, text="Click Me!", padx=50, pady=20, command=myClick, fg="red", bg="yellow")


my_button1.grid(row=0, column=0)
my_button2.grid(row=0, column=1)
my_button3.grid(row=1, column=0)
my_button4.grid(row=1, column=1)



root.mainloop()