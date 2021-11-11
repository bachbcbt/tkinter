import tkinter as tk
from tkinter import ttk
from tkinter.constants import CENTER, EW, N, NS, NSEW, SEPARATOR, W
from tkinter.messagebox import showinfo
import tkinter as tk
from typing import Container

root=tk.Tk()
root.resizable(0,0)
root.geometry('400x200')
root.title('Treeview')

root.columnconfigure(0,weight=1)
root.rowconfigure(0,weight=1)

tree=ttk.Treeview(root)

tree.heading('#0',text='PC',anchor=W)

tree.insert('',tk.END,text='C',iid='tm1',open=False)
tree.insert('',tk.END,text='D',iid=1,open=False)
tree.insert('',tk.END,text='E',iid=2,open=False)
tree.insert('',tk.END,text='F',iid=3,open=False)
tree.insert('',tk.END,text='G',iid=4,open=False)

tree.insert('',tk.END,text='User',iid=5,open=False)
tree.insert('',tk.END,text='Program file',iid=6,open=False)
tree.insert('',tk.END,text='Program data',iid=8,open=False)

tree.move(5,'tm1',0)
tree.move(6,'tm1',0)
tree.move(8,5,1)

tree.grid(column=0,row=0,sticky=NSEW)

root.mainloop()
