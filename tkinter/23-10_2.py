from tkinter import *
from tkinter.ttk import *

top=Tk()

photo=PhotoImage(file = r"Logo2.png")
photoimage=photo.subsample(10)

button=Button(top,text='button',image=photo)
button.place(relheight=0.5,relwidth=0.5)

top.mainloop()