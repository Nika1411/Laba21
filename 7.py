#!/usr/bin/env python3
# -*- config: utf-8 -*-

from tkinter import *
root = Tk()

mainmenu = Menu(root)
root.config(menu=mainmenu)

filemenu = Menu(mainmenu, tearoff=0)
filemenu.add_command(label="Открыть...")
filemenu.add_command(label="Новый")
filemenu.add_command(label="Сохранить...")
filemenu.add_command(label="Выход")

helpmenu = Menu(mainmenu, tearoff=0)
helpmenu2 = Menu(helpmenu, tearoff=0)
helpmenu2.add_command(label="Локальная справка")
helpmenu2.add_command(label="На сайте")
helpmenu.add_cascade(label="Помощь", menu=helpmenu2)
helpmenu.add_command(label="О программе")

mainmenu.add_cascade(label="Файл", menu=filemenu)
mainmenu.add_cascade(label="Справка", menu=helpmenu)

root.mainloop()
