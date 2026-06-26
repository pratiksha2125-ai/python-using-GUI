
from tkinter import *
root=Tk()
root.title("GUI")
root.geometry("400x500")
label=Label(root,text="Hello")
label.pack()

def change():
    label.config(text="Welcome")
Button(root,text="Change",command=change).pack()
root.mainloop()