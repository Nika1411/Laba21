#!/usr/bin/env python3
# -*- config: utf-8 -*-

from tkinter import *


def add():
    a = Toplevel()
    a.geometry('120x130')
    a.resizable(0, 0)

    Label(a, text="x1").grid(row=0, column=0)
    ent1 = Entry(a, width=5)
    ent1.grid(row=0, column=1)

    Label(a, text="x2").grid(row=1, column=0)
    ent2 = Entry(a, width=5)
    ent2.grid(row=1, column=1)

    Label(a, text="y1").grid(row=0, column=2)
    ent3 = Entry(a, width=5)
    ent3.grid(row=0, column=3)

    Label(a, text="y2").grid(row=1, column=2)
    ent4 = Entry(a, width=5)
    ent4.grid(row=1, column=3)

    var = IntVar()
    var.set(1)
    r1 = Radiobutton(a, text="Прямоугольник", value=1, variable=var)
    r1.grid(row=3, column=0, columnspan=4)
    r2 = Radiobutton(a, text="Овал", value=0, variable=var)
    r2.grid(row=4, column=0, columnspan=4)

    def Paint():
        x1 = int(ent1.get())
        y1 = int(ent3.get())
        x2 = int(ent2.get())
        y2 = int(ent4.get())
        if var.get == 0:
            c.create_oval(x1, y1, x2, y2, width=3)
        elif var.get() == 1:
            c.create_rectangle(x1, y1, x2, y2, width=3)
        a.destroy()

    but = Button(a, text='Нарисовать', command=Paint)
    but.grid(row=5, column=0, columnspan=4)


root = Tk()

c = Canvas(width=300, height=300, bg='white')
c.grid(row=0, column=0)
Button(bg='lightgrey', text='Добавить фигуру', command=add).grid(row=2, column=0)

root.mainloop()
