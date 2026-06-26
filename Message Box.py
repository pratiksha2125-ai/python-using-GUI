from tkinter import *
from tkinter import messagebox

def show():
    messagebox.showinfo("Message","Hello Student!!")

root=Tk()
root.title("GUI")
root.geometry("400x500")

Button(root,text="Show Message",command=show).pack()
root.mainloop()