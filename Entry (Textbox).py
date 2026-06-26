from tkinter import *
root=Tk()
root.title("GUI")
root.geometry("400x500")
def show():
    print(entry.get())
entry=Entry(root)
entry.pack()
btn=Button(root,text="Click",command=show)
btn.pack()
root.mainloop()
