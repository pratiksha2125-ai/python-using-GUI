
from tkinter import *

root=Tk()
root.title("GUI")
root.geometry("400x500")

menu=Menu(root)
root.config(menu=menu)
file_menu=Menu(menu)
menu.add_cascade(label="File",menu=file_menu)
file_menu.add_command(label="New")
file_menu.add_command(label="Open")
file_menu.add_command(label="Exit")
root.mainloop()
