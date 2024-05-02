from tkinter import *


def update_text():
    input_text = left.get()
    m1.insert(END,"\n" + input_text)

def nah_delete():
    m1.delete('1.0', END)

root = Tk()

m1 = Text(root)
m1.insert(INSERT, "Vote for Amogus...")
m1.pack(fill=BOTH, expand=1)

left = Entry(root, bd=5)
left.pack()

m2 = PanedWindow(root, orient=VERTICAL)
m2.pack()


top = Spinbox(m2, from_=0, to=10)
m2.add(top)

middle = Button(m2, text="OK", command=update_text)
m2.add(middle)

bottom = Button(m2, text="Delete", command=nah_delete)
m2.add(bottom)

root.mainloop()