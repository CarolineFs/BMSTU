# Нахождение приближенных коней функции методом касательных
# На графике точками отмечаются экстремумы
# Овчинникова А.П.

import tkinter as tk
from tkinter import END
from tkinter import messagebox
import matplotlib.pyplot as plt
from math import sin, cos
import numpy as np

# CONST
CANVAS_HEIGHT = 500
CANVAS_WIDTH = 840
ERROR_ENTRY_BG = 'pink'
DEFAULT_ENTRY_BG = 'dark grey'


def F(x, n):
    if n == 0: return sin(2 * x)
    if n == 1:
        return 2 * cos(2 * x)
    else:
        return -4 * sin(2 * x)


def Newton(a, b, eps, n):
    try:
        xn = (a + b) / 2
        xn1 = xn - F(xn, n) / F(xn, n + 1)
        i = 0
        while abs(xn1 - xn) > eps:
            i += 1
            if i > 3: return xn1, i, 1
            xn = xn1
            xn1 = xn - F(xn, n) / F(xn, n + 1)
            if xn < a or xn > b: return 0, i, 2
        return xn1, i, 0
    except ValueError:
        return 0, i, 3


def open_warning_window(message):
    messagebox.showwarning('Warning', message)


def create_static_labels():
    label_epsilon = tk.Label(text='Точность')
    label_epsilon.place(x=10, y=10)

    label_start = tk.Label(text='Начало')
    label_start.place(x=10, y=50)

    label_end = tk.Label(text='Конец')
    label_end.place(x=10, y=90)

    label_step = tk.Label(text='Шаг')
    label_step.place(x=10, y=130)

    label_n = tk.Label(text='{:^35}'.format('№'))
    label_n.place(x=0, y=210)

    label_interval = tk.Label(text='{:^35}'.format('Интервал'))
    label_interval.place(x=140, y=210)

    label_root_value = tk.Label(text='{:^35}'.format('Значение корня'))
    label_root_value.place(x=280, y=210)

    label_f_root = tk.Label(text='{:^35}'.format('Значение функции'))
    label_f_root.place(x=420, y=210)

    label_iters = tk.Label(text='{:^35}'.format('№ итерации'))
    label_iters.place(x=560, y=210)

    label_error = tk.Label(text='{:^35}'.format('Код ошибки'))
    label_error.place(x=700, y=210)
    codes_labels = tk.Label(text='Код ошибки')
    codes_labels.place(x=460, y=20)

    code1 = tk.Label(text='0 - корень найдет')
    code1.place(x=460, y=40)

    code1 = tk.Label(text='1 - превышение количества итераций')
    code1.place(x=460, y=60)

    code1 = tk.Label(text='2 - выход за пределы интервала')
    code1.place(x=460, y=80)

    code1 = tk.Label(text='3 - производная равна нулю')
    code1.place(x=460, y=100)


def create_entry(canvas, y, x, width):
    entry = tk.Entry(canvas, width=width, bg=DEFAULT_ENTRY_BG)
    entry.place(x=x, y=y)
    return entry


def create_listbox(canvas, x, y, sb, width=20, height=12):
    listbox = tk.Listbox(canvas, width=width, height=height, yscrollcommand=sb.set,
                         bg=DEFAULT_ENTRY_BG)
    listbox.place(x=x, y=y)
    return listbox


def canvas_creator(root):
    canvas = tk.Canvas(root,
                       height=CANVAS_HEIGHT,
                       width=CANVAS_WIDTH)
    canvas.grid(row=0, column=0)
    return canvas


def checker(value, entry):
    try:
        value = float(value)
    except ValueError:
        entry.delete(0, len(entry.get()))
        entry['bg'] = ERROR_ENTRY_BG
    else:
        entry['bg'] = DEFAULT_ENTRY_BG
    return value


def get_values(canvas, entry_start, entry_end, entry_epsilon, entry_step, button):
    flag = 0
    a = entry_start.get()
    b = entry_end.get()
    eps = entry_epsilon.get()
    h = entry_step.get()
    a = checker(a, entry_start)
    b = checker(b, entry_end)
    eps = checker(eps, entry_epsilon)
    h = checker(h, entry_step)
    if type(a) is float and type(b) is float and \
        type(eps) is float and type(h) is float:
        flag = 1

    if type(a) is float and type(b) is float:
        if a >= b:
            entry_start['bg'] = ERROR_ENTRY_BG
            entry_end['bg'] = ERROR_ENTRY_BG
            entry_start.delete(0, len(entry_start.get()))
            entry_end.delete(0, len(entry_end.get()))
            open_warning_window('Начальное значение отрезка больше или равно конечного!')
            flag = 0
    if type(h) is float:
        if h <= 0:
            entry_step.delete(0, len(entry_step.get()))
            entry_step['bg'] = ERROR_ENTRY_BG
            open_warning_window('Задан шаг меньший или равный нулю!')
            flag = 0
    if type(eps) is float:
        '''if eps == 0:
            entry_epsilon.delete(0, len(entry_epsilon.get()))
            open_warning_window('Неправильно указана точность!')
            entry_epsilon['bg'] = DEFAULT_ENTRY_BG
            flag = 0'''
        if eps <= 1e-323:
            entry_epsilon.delete(0, len(entry_epsilon.get()))
            open_warning_window('Слишком высокая точность!')
            entry_epsilon['bg'] = ERROR_ENTRY_BG
            flag = 0
    if type(h) is float and type(a) is float and type(b) is float and (h > b-a):
        entry_start.delete(0, len(entry_epsilon.get()))
        entry_step.delete(0, len(entry_epsilon.get()))
        entry_end.delete(0, len(entry_epsilon.get()))
        open_warning_window('Шаг больше длины отрезка!')
        entry_step['bg'] = ERROR_ENTRY_BG
        entry_start['bg'] = ERROR_ENTRY_BG
        entry_end['bg'] = ERROR_ENTRY_BG
        flag = 0
    if flag:
        n = int((b - a) // h)
        find_roots(a, b, eps, n, h)


def find_roots(a, b, eps, n, h):
    xkor = []
    ykor = []
    xextmas = []
    yextmas = []
    for i in range(n+1):
        a1, b1 = a + i * h, a + (i + 1) * h
        x, j, code = Newton(a1, b1, eps, 0)
        xext, jj, codeext = Newton(a1, b1, eps, 1)
        # print(xext, codeext)

        listbox_n.insert(END, '{:g}'.format(i) + '\n')
        listbox_interval.insert(END, '[' + '{:g}'.format(a1) + ' ,' + '{:g}'.format(b1) + ']'  '\n')
        listbox_iter.insert(END, '{:g}'.format(j) + '\n')
        listbox_error.insert(END, '{:g}'.format(code) + '\n')
        if not code:
            xkor.append(x)
            ykor.append(F(x, n))
            listbox_root.insert(END, '{:g}'.format(x) + '\n')
            listbox_func.insert(END, '{:g}'.format(F(x, 0)) + '\n')
        else:
            listbox_root.insert(END, '\n')
            listbox_func.insert(END, '\n')

        if not codeext and F(xext - eps, 1) * F(xext + eps, 1) < 0:
            xextmas.append(xext)
            yextmas.append(F(xext, 0))

    # Создание графика matplotlib
    xplot = np.arange(a, b, h)
    yplot = [F(x, 0) for x in xplot]

    fig = plt.figure()
    plt.plot(xplot, yplot)

    plt.title('Plot')
    plt.ylabel('sin(2x)')
    plt.xlabel('X')
    for i in range(len(xkor)):
        plt.scatter(xkor[i], ykor[i])
    for i in range(len(xextmas)):
        plt.scatter(xextmas[i], yextmas[i])
    plt.grid(True)

    plt.show()


root = tk.Tk()
root.title('Roots')
root.resizable(width=False, height=False)

canvas = canvas_creator(root)

create_static_labels()

entry_epsilon = create_entry(canvas, 10, 80, 20)
entry_start = create_entry(canvas, 50, 80, 20)
entry_end = create_entry(canvas, 90, 80, 20)
entry_step = create_entry(canvas, 130, 80, 20)

def scroll(*args):
    listbox_n.yview(*args)
    listbox_interval.yview(*args)
    listbox_root.yview(*args)
    listbox_func.yview(*args)
    listbox_iter.yview(*args)
    listbox_error.yview(*args)

sb = tk.Scrollbar(root, command=scroll)
sb.place(x=830, y=240)

listbox_n = create_listbox(canvas, 5, 240, sb)
listbox_interval = create_listbox(canvas, 145, 240, sb)
listbox_root = create_listbox(canvas, 285, 240, sb)
listbox_func = create_listbox(canvas, 425, 240, sb)
listbox_iter = create_listbox(canvas, 565, 240, sb)
listbox_error = create_listbox(canvas, 705, 240, sb)

result_button = tk.Button(canvas, text='Найти корни')
result_button.bind('<Button-1>',
                    lambda x: get_values(canvas,
                                        entry_start,
                                        entry_end,
                                        entry_epsilon,
                                        entry_step,
                                        'roots'))
result_button.place(x=300, y=90)


root.mainloop()
