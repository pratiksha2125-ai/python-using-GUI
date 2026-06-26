
# used to display all items

from tkinter import *
root=Tk()
root.title("GUI")
root.geometry("400x500")
listbox=Listbox(root)
listbox.pack()
listbox.insert(1,"Python")
listbox.insert(2,"Java")
listbox.insert(3,"C++")
root.mainloop()
