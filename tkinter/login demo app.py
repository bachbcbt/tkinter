# app login
import tkinter as tk
from tkinter import ttk
from tkinter.constants import ROUND

# root window

class login():
    def __init__(self,name,size):
        self.name=name
        self.size=size
        self.root=tk.Tk()
    def createApp(self):
        self.root.geometry(self.size)
        self.root.title(self.name)
    def createLabel(self,col,ro,label,color):
        self.label=tk.Label(self.root,text=label,background=color)
        self.label.grid(column=col,row=ro,sticky=tk.EW,padx=5,pady=5)
    def createEntry(self,col,ro,color):
        self.entry=tk.Entry(self.root,background=color)
        self.entry.grid(column=col,row=ro,sticky=tk.EW,padx=5,pady=5)
    def run(self):
        self.root.mainloop()

test=login('dang nhap','240x100')
test.createApp()
test.createLabel(0,0,'Ten dang nhap','red')
test.createEntry(1,0,'red')
test.createLabel(0,1,'Mat khau','green')
test.createEntry(1,1,'green')
test.run()
# root=tk.Tk()
# root.geometry('240x100')
# root.title('Dang nhap')


# # cai grid
# root.columnconfigure(0,weight=1)
# root.columnconfigure(1,weight=2)

# # uname
# username_label=tk.Label(root,text='Ten dang nhap:', background='red')
# username_label.grid(column=0,row=0,sticky=tk.EW,padx=5,pady=5)

# username_entry=tk.Entry(root,background='green')
# username_entry.grid(column=1,row=0,sticky=tk.EW,padx=5,pady=5)

# # pass
# pw_label=ttk.Label(root,text='Mat khau:')
# pw_label.grid(column=0,row=1,sticky=tk.EW,padx=5,pady=5)

# pw_entry=ttk.Entry(root,show='*')
# pw_entry.grid(column=1,row=1,sticky=tk.EW,padx=5,pady=5)

# # nut dang nhap
# login_button=ttk.Button(root,text='Dang nhap')
# login_button.grid(column=1,row=3,sticky=tk.E,padx=5,pady=5)

# root.mainloop()