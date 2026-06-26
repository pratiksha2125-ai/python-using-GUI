from tkinter import *
from tkinter import ttk
root=Tk()
root.title("NOTEBOOK")
root.geometry("400x500")
notebook=ttk.Notebook(root)
notebook.pack()
tab1=Frame(notebook)
tab2=Frame(notebook)
notebook.add(tab1,text="Home")
notebook.add(tab2,text="About")
Label(tab1,text="Welcome").pack()
Label(tab2,text="About Page").pack()
root.mainloop()