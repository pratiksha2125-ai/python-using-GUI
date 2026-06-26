
from tkinter import *
root=Tk()
root.title("GUI")
root.geometry("400x500")
gender=StringVar()
Radiobutton(root,text="Male",variable=gender,value="Male").pack()
Radiobutton(root,text="Female",variable=gender,value="Female").pack()
root.mainloop()