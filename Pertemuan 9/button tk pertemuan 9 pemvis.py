import tkinter as tk

root = tk.Tk()

Framewoy = tk.Frame(root, bg = 'blue')

Framewoy.place(relwidth = 0.8, relheight = 0.8)

Tombolweh = tk.Button(Framewoy, text = "Anjay ada tombol", bg = 'gray', fg = 'green')
Tombolweh.pack()

Entryjir = tk.Entry(Framewoy, bg = 'green')
Entryjir.pack()

root.mainloop()