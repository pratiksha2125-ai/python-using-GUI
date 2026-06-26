from tkinter import *

root = Tk()
root.title("GUI")
root.geometry("400x500")

photo = PhotoImage(file=r"C:\Users\Pratiksha\OneDrive\Pictures.jpg")

Label(root, image=photo).pack()

root.mainloop()