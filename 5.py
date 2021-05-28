#!/usr/bin/env python3
# -*- config: utf-8 -*-

from tkinter import *
from tkinter import messagebox as mb


def check():
    s = entry.get()
    if not s.isdigit():
        mb.showerror(
            "Ошибка",
            "Должно быть введено число")
    else:
        entry.delete(0, END)
        label['text'] = s


root = Tk()

entry = Entry()
entry.pack(pady=10)
Button(text='Передать', command=check).pack()
label = Label(height=3)
label.pack()

root.mainloop()
