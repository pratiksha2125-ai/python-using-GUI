
from tkinter import *
import time
root=Tk()
root.title("GUI")
root.geometry("400x500")
label=Label(root,font=("Arial",20))
label.pack()
def clock():
    label.config(text=time.strftime("%H:%M:%S"))
    label.after(100,clock)
clock()
root.mainloop()