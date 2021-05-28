#!/usr/bin/env python3
# -*- config: utf-8 -*-


from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox as mb


def insert_text():
    file_name = fd.askopenfilename()
    try:
        f = open(file_name)
    except(FileNotFoundError, TypeError):
        mb.showinfo("Открытие файла",
                    "Файл не выбран!")
    else:
        s = f.read()
        text.insert(1.0, s)
        f.close()


def extract_text():
    file_name = fd.asksaveasfilename()
    try:
        f = open(file_name, 'w')
    except(FileNotFoundError, TypeError):
        mb.showinfo("Сохранение файла",
                    "Фаил не сохранен!")
    else:
        s = text.get(1.0, END)
        f.write(s)
        f.close()


def delete_text():
    answer = mb.askyesno("Удаление", "Удалить данные?")
    if answer:
        text.delete(1.0, END)


root = Tk()
text = Text(width=50, height=25)
text.grid(columnspan=3)
b1 = Button(text="Открыть", command=insert_text)
b1.grid(row=1, sticky=E)
b2 = Button(text="Сохранить", command=extract_text)
b2.grid(row=1, column=1, sticky=W)
b3 = Button(text="Отчистить", command=delete_text)
b3.grid(row=1, column=2, sticky=E)

root.mainloop()
