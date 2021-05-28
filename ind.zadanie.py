#!/usr/bin/env python3
# -*- config: utf-8 -*-


from tkinter import *
from tkinter import messagebox as mb
import modul


def add_window():
    def add():
        time = en3.get()
        name = en1.get()
        num = en2.get()

        staff.add(name, num, time)

    add_w = Toplevel()
    add_w.title('Добавить')
    add_w.resizable(False, False)
    add_w.geometry('225x100')
    en1 = Entry(add_w)
    en2 = Entry(add_w)
    en3 = Entry(add_w)
    lb1 = Label(add_w, text="Название пункта назначения")
    lb2 = Label(add_w, text="Номер поезда")
    lb3 = Label(add_w, text="Время отправления")
    bt1 = Button(add_w, text="Добавить", command=add)

    lb1.grid(row=0, column=0)
    lb2.grid(row=1, column=0)
    lb3.grid(row=2, column=0)
    en1.grid(row=0, column=1)
    en2.grid(row=1, column=1)
    en3.grid(row=2, column=1)
    bt1.grid(row=3, column=0, columnspan=2)


def load_window():
    def load_f():
        staff.load(en4.get())
        load_w.destroy()

    load_w = Toplevel()
    load_w.title('Открыть')
    load_w.resizable(False, False)
    load_w.geometry('225x100')
    lb4 = Label(load_w, text="Введите название файла")
    en4 = Entry(load_w)
    bt3 = Button(load_w, text="Загрузить", command=load_f)
    lb4.pack(padx=2, pady=2)
    en4.pack(padx=2, pady=2)
    bt3.pack(padx=2, pady=2)


def save_window():
    def save_f():
        staff.save(en4.get())
        save_w.destroy()

    save_w = Toplevel()
    save_w.title('Сохранение')
    save_w.resizable(False, False)
    save_w.geometry('225x100')
    lb4 = Label(save_w, text="Введите название файла")
    en4 = Entry(save_w)
    bt3 = Button(save_w, text="Сохранить", command=save_f)
    lb4.pack(padx=2, pady=2)
    en4.pack(padx=2, pady=2)
    bt3.pack(padx=2, pady=2)


def select_window():
    def choice():
        try:
            choice_en = en4.get()
            res = staff.select(choice_en)
            if res:
                for idx, train in enumerate(res, 1):
                    text.delete(0.0, END)
                    text.insert(0.0, '| {:>4} | {:<10} | {:<30} |'.format(idx, train.num, train.name))
            else:
                text.delete(0.0, END)
                text.insert(0.0, 'Таких поездов нет!')
        except(ValueError, TypeError):
            mb.showinfo("Выбор поезда",
                        "Введите время отправления")

    sel_w = Toplevel()
    sel_w.title('Выбрать')
    sel_w.resizable(False, False)
    sel_w.geometry('225x100')
    lb4 = Label(sel_w, text="Введите время отправления")
    en4 = Entry(sel_w)
    bt3 = Button(sel_w, text="Подтвердить", command=choice)
    lb4.pack(padx=2, pady=2)
    en4.pack(padx=2, pady=2)
    bt3.pack(padx=2, pady=2)


def show():
    text.delete(0.0, END)
    text.insert(0.0, staff)


if __name__ == '__main__':
    staff = modul.Staff()

    root = Tk()
    root.geometry('800x450')
    root.title('Главное окно')
    root.resizable(False, False)

    main_menu = Menu(root)
    root.config(menu=main_menu)

    file_menu = Menu(main_menu, tearoff=0)
    file_menu.add_command(label="Открыть", command=load_window)
    file_menu.add_command(label="Добавить", command=add_window)
    file_menu.add_command(label="Сохранить", command=save_window)

    main_menu.add_cascade(label="Файл", menu=file_menu)
    main_menu.add_command(label="Показать", command=show)
    main_menu.add_command(label="Выбрать", command=select_window)
    main_menu.add_command(label="Выход", command=lambda: root.destroy())

    text = Text(bg='white', width=97, height=100)
    text.pack(side=LEFT)
    scroll = Scrollbar(command=text.yview)
    scroll.pack(side=LEFT, fill=Y)
    text.config(yscrollcommand=scroll.set)

    root.mainloop()
