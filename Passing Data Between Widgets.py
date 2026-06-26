from tkinter import *

root = Tk()

entry = Entry(root)
entry.pack()

def show():
    label.config(text=entry.get())

Button(root, text="Show", command=show).pack()

label = Label(root, text=" hiiii")
label.pack()

root.mainloop()