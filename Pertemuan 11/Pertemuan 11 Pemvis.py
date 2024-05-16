# Creating Gui Using Tkinter

import tkinter as tk

root = tk.Tk()
# 1
FrameKu = tk.Frame(root, bg = 'pink')
FrameKu.place(relwidth = 0.8, relheight = 0.8)
# 2
MaButton = tk.Button(root, text = 'Hello World', bg = 'blue', fg = 'yellow')
MaButton.pack()

EntryWoy = tk.Entry(FrameKu, bg = 'yellow')
EntryWoy.pack()
# 3


root.mainloop()