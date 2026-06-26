
from tkinter import *
root=Tk()
root.title("GUI")
root.geometry("400x500")
def clicked(event):
    print("Mouse Clicked")
label=Label(root,text="click Here")
label.pack()
label.bind("<Button-1>",clicked)
root.mainloop()

# <Button-1>Left mouse click
# <Button-3> right mouse click
# <Enter> Mouse enters widget
# <Leave> Mouse leaves widget
