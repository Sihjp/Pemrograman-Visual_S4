from tkinter import *

root = Tk()
text = Text(root)
text.insert(INSERT, "Hello....")
text.insert(END, "Bye Bye....")
text.pack()
text.pack()
text.tag_add("here", "1.0", "1.4")
text.tag_add("there", "1.8", "1.14")
text.tag_config("here", background="yellow", foreground="red")
text.tag_config("there", background="blue", foreground="white")
root.mainloop()