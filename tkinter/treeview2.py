import tkinter as tk
from tkinter import ttk
from tkinter.constants import CENTER, EW, N, NS, NSEW, SEPARATOR, W
from tkinter.messagebox import showinfo
from typing import Container

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Treeview demo')
        self.geometry('620x200')

        self.tree=self.create_tree_widget()

    def create_tree_widget(self):
        cols=('#0','#1','#2')
        tree=ttk.Treeview(self,columns=cols,show='headings')

        tree.heading('#0',text='First name')
        tree.heading('#1',text='Last name')
        tree.heading('#2',text='Mail')

        tree.bind('<<TreeviewSelect>>',self.item_selected)
        tree.grid(row=0,column=0,sticky=NSEW)

        scrollbar=ttk.Scrollbar(self,orient='vertical',command=tree.yview)
        tree.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=0,column=1,sticky=NS)

        contacts=[]
        for n in range(1,100):
            contacts.append((f'first{n}',f'last{n}',f'email{n}@example.com'))

        for contact in contacts:
            tree.insert('',tk.END,values=contact)

        return tree
    
    def item_selected(self,event):
        for selected_item in self.tree.selection():
            item=self.tree.item(selected_item)
            record=item['values']

            showinfo(title='Information',message=','.join(record))

if __name__=='__main__':
    app=App()
    app.mainloop()