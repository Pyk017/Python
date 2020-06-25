from tkinter import *
from PIL import ImageTk, Image

root = Tk()

# Title
root.title("GUI")

# Icon
root.iconbitmap('G:\\Tkinter\\unnamed.png')

# Image
my_image = ImageTk.PhotoImage(Image.open('G:\\Tkinter\\Monogram-PY-Logo-Design-by-Greenlines-Studios-580x386.jpg'))
my_label = Label(image=my_image)
my_label.pack()

# Exit Button
button_quit = Button(root, text="Exit!", command = root.quit)
button_quit.pack()

root.mainloop() 
