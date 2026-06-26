from tkinter import *
root=Tk()
root.title("GUI")
root.geometry("400x500")
def open_window():
    win=Toplevel(root)
    win.title("Second Window")
    win.geometry("500x600")
    Label(win,text="New window").pack()
Button(root,text="Open",command=open_window).pack()
root.mainloop()