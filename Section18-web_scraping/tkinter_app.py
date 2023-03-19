import tkinter
from tkinter import ttk
root = tkinter.Tk()
frm = tkinter.Frame(root, padx=10)
frm.grid()
ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
root.mainloop()
