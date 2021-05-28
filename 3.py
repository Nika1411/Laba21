#!/usr/bin/env python3
# -*- config: utf-8 -*-

from tkinter import *


def rem():
    global l1_flag
    if l1_flag == 1:
        l1.grid_remove()
        l1_flag = 0
    else:
        l1.grid()
        l1_flag = 1


def forg():
    global l2_flag
    if l2_flag == 1:
        l2.grid_forget()
        l2_flag = 0
    else:
        l2.grid(row=1)
        l2_flag = 1


root = Tk()

l1_flag = 1
l2_flag = 1
l1 = Label(width=5, height=3, bg='blue')
l2 = Label(width=5, height=3, bg='green')
b1 = Button(bg='lightblue', command=rem)
b2 = Button(bg='lightgreen', command=forg)

l1.grid(row=0)
l2.grid(row=1)
b1.grid(row=2)
b2.grid(row=3)

root.mainloop()