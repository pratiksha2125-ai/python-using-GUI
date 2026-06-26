from tkinter import *

root=Tk()
root.title("GUI")
root.geometry("400x500")

Label(root,text="Password").pack()
Entry(root,show="*").pack()
root.mainloop()