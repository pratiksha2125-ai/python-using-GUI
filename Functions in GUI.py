from tkinter import *

root = Tk()

def greet():
    print("Hello Student")

Button(root, text="Click", command=greet).pack()

root.mainloop()