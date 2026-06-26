
from tkinter import *
root=Tk()
root.title("GUI")
root.geometry("400x500")
name=StringVar()
Entry(root,textvariable=name).pack()
def show():
    print(name.get())

Button(root,text="show",command=show).pack()
root.mainloop()