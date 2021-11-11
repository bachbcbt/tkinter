import tkinter as tk
from tkinter import ttk
from tkinter.constants import EW, NS, SEPARATOR
from tkinter.messagebox import showinfo
import tkinter as tk
from typing import Container

root=tk.Tk()
root.resizable(0,0)
root.geometry('300x200')
root.title('Combo box')

def month_select(event):
    msg=f'Ban chon thang {month_cb.get()}!'
    showinfo(
        title='Ket qua',
        message=msg
    )

def month_select2():
    msg=f'Ban chon thang {month_cb.get()}!'
    showinfo(
        title='Ket qua',
        message=msg
    )

months=(1,2,3,4,5,6,7,8,9,10,11,12)

label=ttk.Label(text='Hay chon 1 thang:').pack(fill='x',padx=5,pady=5)

selected_month=tk.StringVar()

month_cb=ttk.Combobox(
    root,
    textvariable=selected_month,
    validate='focusout',
    validatecommand=month_select2
)
month_cb['values']=months
# month_cb['state']='readonly'
month_cb.pack(fill='x',padx=5,pady=5)

month_cb.bind('<<ComboboxSelected>>',month_select)

b1=ttk.Button(
    root,
    text='Get!',
    command=month_select2
).pack(fill='x',padx=5,pady=5)



root.mainloop()
