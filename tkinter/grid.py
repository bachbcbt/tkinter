# app login
import tkinter as tk
from tkinter import ttk

# root window
root=tk.Tk()
root.geometry('400x180')
root.title('Replace')

l1=tk.Label(root,text='Find what:')
l1.grid(column=0,row=0,sticky=tk.W,padx=5,pady=5)

l2=tk.Label(root,text='Replace with:')
l2.grid(column=0,row=1,sticky=tk.W,padx=5,pady=5)

b1=tk.Button(root,text='Match case')
b1.grid(column=0,row=2,sticky=tk.EW,padx=5,pady=5)

b2=tk.Button(root,text='Wrap around')
b2.grid(column=0,row=3,sticky=tk.EW,padx=5,pady=5)

e1=tk.Entry(root)
e1.grid(column=1,row=0,sticky=tk.EW,padx=5,pady=5)
e1.focus()

e2=tk.Entry(root)
e2.grid(column=1,row=1,sticky=tk.EW,padx=5,pady=5)

b3=tk.Button(root,text='Find next')
b3.grid(column=2,row=0,sticky=tk.EW,padx=5,pady=5)

b4=tk.Button(root,text='Replace')
b4.grid(column=2,row=1,sticky=tk.EW,padx=5,pady=5)

b5=tk.Button(root,text='Replace all')
b5.grid(column=2,row=2,sticky=tk.EW,padx=5,pady=5)

b6=tk.Button(root,text='Cancel')
b6.grid(column=2,row=3,sticky=tk.EW,padx=5,pady=5)

root.columnconfigure(0,weight=1)
root.columnconfigure(1,weight=2)
root.columnconfigure(2,weight=1)

root.mainloop()
