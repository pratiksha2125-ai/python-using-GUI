from tkinter import *

root = Tk()

def message():
    print("5 Seconds Completed")

root.after(5000, message)

root.mainloop()