from tkinter import *

print('=================================')
print('Mencetak data dari entry widget dengan button')
print('=================================')

root = Tk()
root.geometry('400x200')

def CetakMeh():
    teks = entry1.get()
    print(teks)
    return None

entry1 = Entry(root, width = 20)
entry1.pack()
Button(root, text = 'Cetak', command = CetakMeh).pack()

root.mainloop()