

from tkinter import *
root=Tk()
root.title("Layout")
root.geometry("400x500")
Label(root,text="Name").grid(row=0,column=0)
Entry(root).grid(row=0,column=1)
Label(root,text="Age").grid(row=1,column=0)
Entry(root).grid(row=1,column=1)
root.mainloop()