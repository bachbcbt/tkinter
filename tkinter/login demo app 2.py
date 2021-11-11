# app login
import tkinter as tk
from tkinter import ttk
from tkinter.constants import ROUND

# root window

class App(tk.Tk):
    def __init__(self,name,size):
        super().__init__()
        self.name=name
        self.size=size
    def createApp(self):
        self.geometry(self.size)
        self.title(self.name)
    def createLabel(self,col,ro,label,color):
        self.label=tk.Label(self,text=label,background=color)
        self.label.grid(column=col,row=ro,sticky=tk.EW,padx=5,pady=5)
    def createEntry(self,col,ro,color):
        self.entry=tk.Entry(self,background=color)
        self.entry.grid(column=col,row=ro,sticky=tk.EW,padx=5,pady=5)

if __name__=='__main__':
    test=App('dang nhap','240x100')
    test.createApp()
    test.createLabel(0,0,'Ten dang nhap','yellow')
    test.createEntry(1,0,'red')
    test.createLabel(0,1,'Mat khau','green')
    test.createEntry(1,1,'purple')
    test.mainloop()

