import tkinter as tk
from tkinter import ttk

def create_input_frame(parent):
    frame = tk.Frame(parent, bg = "violet")
    # frame['borderwidth'] = 3
    frame.columnconfigure(0, weight = 0)
    frame.columnconfigure(1, weight= 1)
    for i in range(0, 4):
        frame.rowconfigure(i, weight= 1, uniform='Test')
    
    labelFind = ttk.Label(frame, text = "Find what: ")
    labelFind.grid(column=0, row = 0)
    keyworkFind = ttk.Entry(frame, width = 30)
    keyworkFind.grid(column= 1, row = 0, sticky= tk.EW)


    labelReplace = ttk.Label(frame, text = "Replace with: ")
    labelReplace.grid(column=0, row = 1)
    keyworkReplace = ttk.Entry(frame, width = 30)
    keyworkReplace.grid(column= 1, row = 1, sticky= tk.EW)
    

    mathCase = tk.StringVar()
    mathCaseCheck = ttk.Button(frame, text = "mathcase", command= lambda: print(mathCase.get()))
    mathCaseCheck.grid(column=0, row = 2)

    for widgets in frame.winfo_children():
        widgets.grid(padx = 5, pady = 5)

    return frame


def create_button_frame(parent):
    frame = tk.Frame(parent, bg = "pink")
    frame.columnconfigure(0, weight=1)

    buttonList = ["Find Next", "Replace", "Replace All", "Cancel"]
    
    for button in buttonList:
        ttk.Button(frame, text = button).grid(column= 0, row = buttonList.index(button))

    for widgets in frame.winfo_children():
        widgets.grid(padx = 5, pady = 5)    

    return frame


def main_window():
    root = tk.Tk()
    root.title("Replace")
    root.geometry("600x300")
    root.resizable(0, 0)

    root.columnconfigure(0, weight= 5)
    root.columnconfigure(1, weight= 1)

    button_frame = create_button_frame(root)
    input_frame = create_input_frame(root)

    button_frame.grid(column = 1, row = 0, sticky=tk.NSEW)
    input_frame.grid(column = 0, row = 0, sticky=tk.NSEW)

    root.mainloop()


if __name__ == "__main__":
    main_window()