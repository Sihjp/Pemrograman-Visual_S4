import tkinter as tk
import tkinter.ttk as ttk
from tkinter import simpledialog

root = tk.Tk()
data = [
    ["Darrell", 26, 20000],
    ["Vino", 31, 23000],
    ["Widi", 18, 19000],
    ["Zega", 22, 20500],
    ["Louis Beton", 97, 10000],
    ["Pessi Coy", 33, 8000],
    ["Valentinaldo", 140, 500],
]
index = 0
def read_data():
    for index, line in enumerate(data):
        tree.insert('', tk.END, iid = index, text = line[0], values = line[1:])
columns = ("age", "salary")

tree = ttk.Treeview(root, columns = columns, height = 20)
tree.pack(padx = 5, pady = 5)

tree.heading('#0', text = 'Name')
tree.heading('age', text = 'Age')
tree.heading('salary', text = 'Salary')

read_data()
root.mainloop()