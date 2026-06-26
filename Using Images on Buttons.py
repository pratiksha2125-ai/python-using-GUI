from tkinter import *

root = Tk()

photo = PhotoImage(file="image.png")

Button(root, image=photo).pack()

root.mainloop()