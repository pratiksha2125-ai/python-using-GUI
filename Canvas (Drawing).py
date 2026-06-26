from tkinter import *

root = Tk()

canvas = Canvas(root, width=300, height=200)
canvas.pack()

canvas.create_line(10, 10, 200, 100)
canvas.create_rectangle(50, 50, 150, 120)
canvas.create_oval(170, 50, 250, 120)

root.mainloop()