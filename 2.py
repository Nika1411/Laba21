#!/usr/bin/env python3
# -*- config: utf-8 -*-

from tkinter import *

root = Tk()

Label(text="Имя:").grid(row=0, column=0, sticky=W, pady=10, padx=10)
table_name = Entry()
table_name.grid(row=0, column=1, columnspan=3, sticky=W+E, padx=10)
Label(text="Столбцов:").grid( row=1, column=0, sticky=W, padx=10, pady=10)
Spinbox(width=7, from_=1, to=50)\
    .grid(row=1, column=1, padx=10)
Label(text="Строк:")\
    .grid(row=1, column=2, sticky=E)
Spinbox(width=7, from_=1, to=100)\
    .grid(row=1, column=3, sticky=E, padx=10)
Button(text="Справка")\
    .grid(row=2, column=0, pady=10, padx=10)
Button(text="Вставить")\
    .grid(row=2, column=2)
Button(text="Отменить")\
    .grid(row=2, column=3, padx=10)
root.mainloop()