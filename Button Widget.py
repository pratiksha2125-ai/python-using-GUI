
from tkinter import *
root=Tk()
root.title("My first gui")
root.geometry("400x500")
def hello():
    print("Button clicked!")
# root=Tk()
btn=Button(root,text="Submit",command=hello)
btn.pack()
root.mainloop()