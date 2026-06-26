from tkinter import *

class App:
    def __init__(self, root):
        self.label = Label(root, text="Welcome")
        self.label.pack()

root = Tk()
app = App(root)
root.mainloop()

