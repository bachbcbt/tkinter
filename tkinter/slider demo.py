import tkinter as tk
from tkinter import ttk
from tkinter.constants import CENTER, EW, N, NS, SEPARATOR, W
from tkinter.messagebox import showinfo
import tkinter as tk
from typing import Container

root=tk.Tk()
# root.resizable(0,0)
root.geometry('300x200')
root.title('Slider demo')

root.columnconfigure(0,weight=1)
root.columnconfigure(1,weight=3)

current=tk.DoubleVar()

def get_current():
    return '{: .1f}'.format(current.get())

def slider_changed(event):
    value_label.configure(text=get_current())

slider_label=ttk.Label(
    root,
    text='Slider:'
)

slider_label.grid(
    column=0,
    row=0,
    sticky=W
)

slider=ttk.Scale(
    root,
    from_=0,
    _TakeFocusValue=10,
    to=100,
    orient='horizontal',
    command=slider_changed,
    variable=current
)

slider.grid(
    column=1,
    row=0,
    sticky=EW
)

current_label=ttk.Label(
    root,
    text='Current value:'
)

current_label.grid(
    row=1,
    columnspan=2,
    sticky=N,
    ipadx=10,
    ipady=10
)

value_label=ttk.Label(
    root,
    text=get_current()
)

value_label.grid(
    row=2,
    columnspan=2,
    sticky=N
)

root.mainloop()
