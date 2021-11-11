import tkinter as tk
from tkinter import ttk
from tkinter.constants import EW, NS
from tkinter.messagebox import showinfo

root=tk.Tk()
root.resizable(0,0)
root.geometry('400x200')
root.title('Scroll widget example')

root.grid_columnconfigure(0,weight=1)
root.grid_rowconfigure(0,weight=1)

text=tk.Text(root,height=10,wrap='none')
text.grid(row=0,column=0,sticky=EW)

scrollbar1=tk.Scrollbar(root,orient='vertical',command=text.yview)
scrollbar1.grid(row=0,column=1,sticky=NS)
text['yscrollcommand']=scrollbar1.set

scrollbar2=tk.Scrollbar(root,orient='horizontal',command=text.xview)
scrollbar2.grid(row=1,column=0,sticky=EW)
text['xscrollcommand']=scrollbar2.set

root.mainloop()


