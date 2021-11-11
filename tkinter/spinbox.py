import tkinter as tk
from tkinter import ttk
from tkinter.constants import CENTER, EW, N, NS, SEPARATOR, W
from tkinter.messagebox import showinfo
import tkinter as tk
from typing import Container

root=tk.Tk()
root.resizable(0,0)
root.geometry('300x200')
root.title('Slider demo')

root.columnconfigure(0,weight=1)
root.rowconfigure(0,weight=1)

current=tk.DoubleVar()

def value_changed(event):
    print(current.get())

spin_box=ttk.Spinbox(
    root,
    from_=0,
    to=50,
    textvariable=current,
    values=(0,10,20,30,40,50),
    wrap=False,
    command=value_changed
)

spin_box.grid(column=0,row=0,sticky=N)

root.mainloop()
