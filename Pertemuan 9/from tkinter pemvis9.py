from tkinter import *
from tkinter import messagebox

top = Tk()
CheckVar1 = IntVar()
top.geometry("100x100")
def helloCallBack():
   msg=messagebox.showinfo( "Hello Python", "Hello World")
B = Button(top, text ="Hello", command = helloCallBack)
B.place(x=50,y=50)



C1 = Checkbutton(top, text = "Music", variable = CheckVar1, \
   onvalue = 1, offvalue = 0, height=5, \
   width = 20, )
C1.pack()
top.mainloop()