#!/usr/bin/env python3
# -*- config: utf-8 -*-

from tkinter import *


def about():
    a = Toplevel()
    a.geometry('200x150')
    a['bg'] = 'grey'
    a.overrideredirect(True)
    Label(a, text="About this")\
        .pack(expand=1)
    a.after(5000, lambda: a.destroy())


root = Tk()
root.title("Главное окно")

root.title("Главное окно")
Button(text="Button", width=20).pack()
Label(text="Label", width=20, height=3)\
    .pack()
Button(text="About", width=20, command=about)\
    .pack()

root.mainloop()

