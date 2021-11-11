from functools import wraps
import tkinter as tk
from tkinter import ttk
from tkinter.constants import CENTER, EW, N, NS, NSEW, SEPARATOR, W
from tkinter.messagebox import showinfo
from typing import Container

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Replace')
        self.geometry('400x180')
        self.columnconfigure(0,weight=4)
        self.columnconfigure(1,weight=1)
        self.__create_widget()

    def __create_widget(self):
        input=InputFrame(self)
        input.grid(column=0,row=0)
        bt=ButtonFrame(self)
        bt.grid(column=1,row=0)

class InputFrame(ttk.Frame):
    def __init__(self,container):
        super().__init__(container)
        self.columnconfigure(0,weight=1)
        self.columnconfigure(1,weight=3)
        self.__create_widget()

    def __create_widget(self):
        # find what
        l1=ttk.Label(self,text='Find what:')
        l1.grid(column=0,row=0,sticky=W)
        keyword1=ttk.Entry(self,width=30)
        keyword1.focus()
        keyword1.grid(column=1, row=0, sticky=W)

        # replace with
        l2=ttk.Label(self,text='Replace with:')
        l2.grid(column=0,row=1,sticky=W)
        keyword2=ttk.Entry(self,width=30)
        keyword2.focus()
        keyword2.grid(column=1, row=1, sticky=W)

        # match case
        match=tk.StringVar()
        match_check=ttk.Checkbutton(
            self,
            text='Match case',
            variable=match,
            command=lambda:print(match.get())
        )
        match_check.grid(column=0,row=2,sticky=W)

        # wraps
        wrap=tk.StringVar()
        wrap_check=ttk.Checkbutton(
            self,
            text='Wrap around',
            variable=wrap,
            command=lambda:print(wrap.get())
        )
        wrap_check.grid(column=0,row=3,sticky=W)

        for widget in self.winfo_children():
            widget.grid(padx=0,pady=5)

        return match,wrap

class ButtonFrame(ttk.Frame):
    def __init__(self,container):
        super().__init__(container)
        self.columnconfigure(0,weight=1)
        self.__create_widget()

    def __create_widget(self):
        
        buttons=['Find next','Replace','Replace all','Cancel']
        
        b1=ttk.Button(self,text=buttons[0])
        b1.grid(column=0, row=0)

        b2=ttk.Button(self,text=buttons[1])
        b2.grid(column=0, row=1)

        b3=ttk.Button(self,text=buttons[2])
        b3.grid(column=0, row=2)

        b4=ttk.Button(self,text=buttons[3])
        b4.grid(column=0, row=3)

        for widget in self.winfo_children():
            widget.grid(padx=5,pady=5)

if __name__=='__main__':
    app=App()
    app.mainloop()