from tkinter import *
from tkinter import messagebox

root = Tk()

def divide():
    try:
        result = 10 / int(entry.get())
        messagebox.showinfo("Result", result)
    except:
        messagebox.showerror("Error", "Invalid Input")

entry = Entry(root)
entry.pack()

Button(root, text="Divide", command=divide).pack()

root.mainloop()