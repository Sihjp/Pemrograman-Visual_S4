from tkinter import *
from tkinter.simpledialog import askstring

top = Tk()

top.geometry("100x100")
def show():
    name = askstring("input", "enter your name")
    print(name)
    
B = Button(top, text ="Click", command = show)
B.place(x = 50, y = 50)

top.mainloop()