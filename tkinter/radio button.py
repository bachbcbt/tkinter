import tkinter as tk
from tkinter import ttk
from tkinter.constants import EW, NS, SEPARATOR
from tkinter.messagebox import showinfo
import tkinter as tk
from typing import Container

root=tk.Tk()
root.resizable(0,0)
root.geometry('300x220')
root.title('Radio button')

selected=tk.StringVar()

sizes=(
    ('Nho','S'),
    ('Vua','M'),
    ('Lon','L'),
    ('Sieu to','XL'),
    ('Sieu to khong lo','XXL'),
)

def show_selected():
    showinfo(
        title='Lua chon',
        message=selected.get()
    )

l1=ttk.Label(text='What is your size?')
l1.pack(fill='x',padx=5,pady=5)

for size in sizes:
    r=ttk.Radiobutton(
        root,
        text=size[0],
        value=size[1],
        variable=selected
    ).pack(fill='x',padx=5,pady=5)

b1=ttk.Button(
    root,
    text='Get!',
    command=show_selected
).pack(fill='x',padx=5,pady=5),

root.mainloop()
