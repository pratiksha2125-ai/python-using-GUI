
from tkinter import *
from tkinter import filedialog

root = Tk()

def open_file():
    file = filedialog.askopenfilename()
    print(file)

Button(root, text="Open File", command=open_file).pack()

root.mainloop()