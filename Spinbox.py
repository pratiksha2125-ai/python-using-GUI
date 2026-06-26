from tkinter import *
root=Tk()
root.title("GUI")
root.geometry("400x500")
spin=Spinbox(root,from_=1,to=10)
spin.pack()
root.mainloop()