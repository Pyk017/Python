from tkinter import *
from PIL import ImageTk, ImageTk

root = Tk()
root.title("This is Frame")

frame = LabelFrame(root, text="This is my Frame.", padx=100, pady=100) # here text attribute is optional so that no heading is involved in it.
frame.pack(padx=100, pady=100)

button = Button(frame, text="Click Me")
button.grid(row=0, column=0)
button2 = Button(frame, text="Dont Click Me")
button2.grid(row=1,column=0)


root.mainloop()
