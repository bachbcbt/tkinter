import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

root=tk.Tk()
root.geometry('400x200')

def getText():
    text=textBox.get('2.0','2.end')
    print(text)

textBox=tk.Text(root,height=8)
textBox.pack()
btRead=tk.Button(root,height=1,width=10,text='read',command=getText)

btRead.pack()

root.mainloop()


