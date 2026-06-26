from tkinter import *
from tkinter .ttk import Progressbar

root=Tk()
root.title("GUI")
root.geometry("400x500")

progress=Progressbar(root,orient=HORIZONTAL,length=200,mode='determinate')
progress.pack(pady=20)
progress['value']=90
root.mainloop()