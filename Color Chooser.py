from tkinter import *
from tkinter import colorchooser

root = Tk()

def choose():
    color = colorchooser.askcolor()
    print(color)

Button(root, text="Choose Color", command=choose).pack()

root.mainloop()