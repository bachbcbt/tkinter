from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo

root=Tk()
root.title('Pack demo')
root.geometry('500x500')

pane=Frame(root)
pane.pack(fill=BOTH, expand=True)

pane1=Frame(pane)
pane1.pack(side=TOP,fill=BOTH, expand=True)

b1=Button(pane1,text='Box 1',foreground='white',background='red',bd=0)
b1.pack(side=TOP,expand=True,fill=BOTH)

b2=Button(pane1,text='Box 2',foreground='white',background='green',bd=0)
b2.pack(side=TOP,expand=True,fill=BOTH)

b3=Button(pane1,text='Box 3',foreground='white',background='blue',bd=0)
b3.pack(side=TOP,expand=True,fill=BOTH)

pane2=Frame(pane)
pane2.pack(side=TOP,fill=BOTH, expand=True)

b4=Button(pane2,text='Left',background='cyan',bd=0)
b4.pack(side=LEFT,expand=True,fill=BOTH)

b5=Button(pane2,text='Center',background='#ff33ff',bd=0)
b5.pack(side=LEFT,expand=True,fill=BOTH)

b6=Button(pane2,text='Right',background='yellow',bd=0)
b6.pack(side=LEFT,expand=True,fill=BOTH)

root.mainloop()

