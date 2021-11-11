import tkinter as tk
from tkinter import ttk
from tkinter.constants import EW, NS, SEPARATOR
from tkinter.messagebox import showinfo
import tkinter as tk
from typing import Container

root=tk.Tk()
root.resizable(0,0)
root.geometry('400x200')
root.title('Check box')

check=tk.StringVar()

def check_change():
    tk.messagebox.showinfo(
        title='Ket qua',
        message=check.get()
    )

checkbox=ttk.Checkbutton(
    root,
    text='Say to the World',
    variable=check,
    command=check_change
    # onvalue='Hello world',
    # offvalue='Bye world'
    )
checkbox.pack()

root.mainloop()
