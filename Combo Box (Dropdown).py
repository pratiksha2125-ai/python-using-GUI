
from tkinter import *
from tkinter import ttk

root=Tk()
root.title("GUI")
root.geometry("400x500")
combo=ttk.Combobox(root,values=["python","Java","c++"])
combo.pack()
root.mainloop()