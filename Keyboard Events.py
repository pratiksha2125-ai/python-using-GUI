from tkinter import *

root = Tk()

def key(event):
    print("Key Pressed:", event.char)

root.bind("<Key>", key)

root.mainloop()