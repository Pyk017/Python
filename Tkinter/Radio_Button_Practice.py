from tkinter import  *

root = Tk()
root.title("Radio Button")
root.iconbitmap("G:\Tkinter\Images\MyIcon.ico")


MODES = [
    ("Pepperoni", 250),
    ("Cheese", 550),
    ("Mushroom", 350),
    ("Onion", 400)
]

opt = StringVar()
opt.set("Cheese")

counter = 0
for i in MODES:
    Radiobutton(root, text=i[0], variable=opt, value=i[1]).grid(row=counter, column=0, sticky=W)
    counter += 1

def clicked(val):
    global myLabel
    global counter
    myLabel = Label(root, text="The Price of Your Pizza is :- {}".format(val))
    myLabel.grid(row=counter + 2, column=0)    


myButton = Button(root, text="Click Me!", command=lambda: clicked(opt.get()))
myButton.grid(row=counter + 1, column=0)

myLabel = Label(root, text="The Price of Your Pizza is :- {}".format(00))
myLabel.grid(row=counter + 2, column=0)

root.mainloop()
