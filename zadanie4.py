#!/usr/bin/env python3
# -*- config: utf-8 -*-

from tkinter import *
from random import random


def move():
    b.place(relx=random(), rely=random())


root = Tk()
root['bg'] = 'white'
root.geometry('1000x800')
img = PhotoImage(file='s.gif')
b = Button(image=img, command=move)
b.place(relx=0.1, rely=0.1, anchor=CENTER)

root.mainloop()
