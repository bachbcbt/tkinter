import tkinter as tk
from tkinter import ttk
from tkinter.constants import EW, NS, SEPARATOR
from tkinter.messagebox import showinfo
import tkinter as tk
from typing import Container

root=tk.Tk()
# root.resizable(0,0)
root.geometry('300x200')
root.title('Label frame')

lf=ttk.LabelFrame(
    root,
    text='Alignment'
)

lf.grid(column=0,row=0,padx=20,pady=20)

alignment=tk.StringVar()

left_radio=ttk.Radiobutton(
        lf,
        text='Trai',
        value='Left',
        variable=alignment
    ).grid(column=0,row=0,ipadx=10,ipady=10)

center_radio=ttk.Radiobutton(
        lf,
        text='Giua',
        value='Center',
        variable=alignment
    ).grid(column=1,row=0,ipadx=10,ipady=10)

right_radio=ttk.Radiobutton(
        lf,
        text='Phai',
        value='Right',
        variable=alignment
    ).grid(column=2,row=0,ipadx=10,ipady=10)

def show_selected():
    showinfo(
        title='Lua chon',
        message=alignment.get()
    )

b1=ttk.Button(
    lf,
    text='Get!',
    command=show_selected
).grid(column=1,row=1,ipadx=10,ipady=10),

root.mainloop()
