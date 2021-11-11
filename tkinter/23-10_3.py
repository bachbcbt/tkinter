from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo

# cua so dang nhap
root=Tk()
root.geometry('400x400')
root.resizable(False,False)
root.title('Sign in')

# cac gia tri
mail=StringVar()
mail.set('sample mail')
pw=StringVar()

# thong bao dang nhap
def login_check():
    msg=f'Ban nhap mail: {mail.get()} va mat khau: {pw.get()}'
    showinfo(
        title='Thong tin',
        message=msg
    )

# khung dang nhap
signin=ttk.Frame(root)
signin.pack(padx=10,pady=10,fill='x',expand=True)

# dong nhap mail
mail_label=ttk.Label(signin,text='Dia chi mail:')
mail_label.pack(fill='x',expand=True)

mail_entry=ttk.Entry(signin,textvariable=mail,state=DISABLED)
mail_entry.pack(fill='x',expand=True)
mail_entry.focus()

# dong nhap pw
pw_label=ttk.Label(signin,text='Mat khau:')
pw_label.pack(fill='x',expand=True)

pw_entry=ttk.Entry(signin,textvariable=pw)
pw_entry.pack(fill='x',expand=True)

# nut dang nhap
login_bt=ttk.Button(signin,text='Dang nhap',command=login_check)
login_bt.pack(fill='x',expand=True,pady=10)

# chay chuong trinh

root.mainloop()
