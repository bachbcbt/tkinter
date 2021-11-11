import tkinter as tk
from tkinter import ttk
from tkinter.constants import EW, NS, SEPARATOR
from tkinter.messagebox import showinfo

root=tk.Tk()
root.resizable(0,0)
root.geometry('400x200')
root.title('Separator')

ttk.Label(root,text='Dong 1').pack()

separator=ttk.Separator(root,orient='horizontal')
separator.pack(fill='x')
ttk.Label(root,text='Dong 2').pack()

root.mainloop()
