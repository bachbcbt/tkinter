# app login
import tkinter as tk
from tkinter import ttk

# root window
root=tk.Tk()
root.geometry('240x100')
root.title('Dang nhap')


# cai grid
root.columnconfigure(0,weight=1)
root.columnconfigure(1,weight=3)

# uname
username_label=tk.Label(root,text='Ten dang nhap:', background='red')
username_label.grid(column=0,row=0,sticky=tk.EW,padx=5,pady=5)

username_entry=tk.Entry(root,background='green')
username_entry.grid(column=1,row=0,sticky=tk.EW,padx=5,pady=5)

# pass
pw_label=ttk.Label(root,text='Mat khau:')
pw_label.grid(column=0,row=1,sticky=tk.EW,padx=5,pady=5)

pw_entry=ttk.Entry(root,show='*')
pw_entry.grid(column=1,row=1,sticky=tk.EW,padx=5,pady=5)

# nut dang nhap
login_button=ttk.Button(root,text='Dang nhap')
login_button.grid(column=1,row=3,sticky=tk.E,padx=5,pady=5)

root.mainloop()