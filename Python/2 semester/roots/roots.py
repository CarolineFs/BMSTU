# Нахождение корней функции методом касателных (Ньютона)
# Овчинникова Анастасия

import tkinter as tk
from tkinter import LEFT, END
from tkinter import messagebox
from math import sin, cos, log, trunc
import matplotlib.pyplot as plt
import numpy as np

def Newton(a, b, eps, N, num):
    err = 0
    x0 = a
    count = 1
    x = x0 - f(x0) / f1(x0) if f1(x0) != 0 else x0 + eps / 10
    while count < N:
        x = x0 - f(x0) / f1(x0) if f1(x0) != 0 else x + eps / 10
        if abs(x - x0) < eps:
            break
        x0 = x
        count += 1
    if x < a or x > b:
        x0 = b
        count = 0
        x = x0 - f(x0) / f1(x0) if f1(x0) != 0 else x0 - eps / 10
        while count < N:
            x = x0 - f(x0) / f1(x0) if f1(x0) != 0 else x - eps / 10
            if abs(x - x0) < eps: break
            x0 = x
            count += 1

    if x >= a and x <= b and (f(a) >= 0 and f(b) <= 0 or f(b) >= 0 and f(a) <= 0):
        x, a, b = round(x, 9), round(a, 2), round(b, 2)
        if count == N:
            err = 2
            x = 9 * '-'
        elif f(x) > 1 or f(x) < -1:
            err = 1
            x = 9 * '-'
    # ввод данных в словарь
    if a != b and ((f(a) >= 0 and f(b) <= 0) or (f(b) >= 0 and f(a) <= 0) or \
                   round(f(x), 2) == 0 and a <= x <= b):
        table['n'].append(num)
        table['ab'].append([(round(a, 8)), (round(b, 8))])

        if x != 9 * '-':
            if a <= x <= b and num == 0 or a < x <= b and num != 0:
                if str(x) == '-0.0': x = 0
                table['fx'].append(f(x))
                table['x'].append(x)
            else:
                err = 3
                table['x'].append(9 * '-')
                table['fx'].append(9 * '-')
        else:
            table['x'].append(9 * '-')
            table['fx'].append(9 * '-')
        table['N'].append(count)
        if type(x) == float:
            if x < a or x > b: err = 3
        table['err'].append(err)

def main(a, b, h, eps, n):
    table['n'] = []
    table['ab'] = []
    table['x'] = []
    table['fx'] = []
    table['N'] = []
    table['err'] =[]

    # Заполняем таблицу
    a1, b1 = a, b
    num = 0
    while a < b:
        if f(a) == 0 and num != 0:
            num -= 1
        else:
            Newton(a, a + h, eps, n, num)
        a += h
        num += 1

    listbox_n.delete(0, END)
    listbox_interval.delete(0, END)
    listbox_root.delete(0, END)
    listbox_func.delete(0, END)
    listbox_iter.delete(0, END)
    listbox_error.delete(0, END)

    if table['n'] == []:
        messagebox.showerror("Error", 'На заданном интервале [' + str(a1) + ', ' + \
                             str(b1) + '] нет корней')

    # вывод таблицы
    i = 0
    num = 1
    for i in range(len(table['n'])):
        listbox_n.insert(END, ''.join(str(num)).center(3))
        num += 1
        listbox_interval.insert(END, '{:30}'.format(str(table['ab'][i])))
        try:
            if str(table['x'][i])[0] == '-':
                listbox_root.insert(END, ''.join \
                    ('{:g}'.format(table['x'][i]).center(12)))
            else:
                listbox_root.insert(END, ''.join('{:g}'.format(table['x'][i]).center(13)))
            if str(table['fx'][i])[0] == '-':
                listbox_func.insert(END, ''.join \
                    ('{:2.2e}'.format(table['fx'][i]).center(12)))
            else:
                listbox_func.insert(END, ''.join('{:2.2e}'.format \
                                              (table['fx'][i]).center(13)))
        except:
            listbox_root.insert(END, ''.join(table['x'][i]).center(14))
            listbox_func.insert(END, ''.join(table['fx'][i]).center(14))

        listbox_iter.insert(END, '{:10}'.format(str(table['N'][i])))
        listbox_error.insert(END, '{:10}'.format(str(table['err'][i])))

    # Строим график
    x = []
    y = []
    x_e = []
    y_e = []
    x_ox = [a1, b1]
    y_ox = [0, 0]
    x0 = []
    y0 = []
    a2 = a1
    while a1 < b1:            # нахождение экстремумов
        if f(a1 - 0.001) < f(a1) and f(a1 + 0.001) < f(a1) or f(a1 - 0.001) > f(a1) \
                and f(a1 + 0.001) > f(a1):
            x_e.append(a1)
            y_e.append(f(a1))
        # нахождения корней функции
        if f(a1 - 0.001) < 0 and f(a1 + 0.001) > 0 or f(a1 - 0.001) > 0 \
                and f(a1 + 0.001) < 0:
            x0.append(a1)
            y0.append(f(a1))
            a += 0.01
        elif abs(round(float('{:g}'.format(f(a1))), 6)) == 0:
            x0.append(a1)
            y0.append(f(a1))
            a += 0.01

        x.append(a1)
        y.append(f(a1))
        a1 += 0.001
    y_oy = [0, 0]
    if min(y) < 0:
        y_oy[0] = min(y)
    else:
        y_oy[0] = -0.5
    if max(y) > 0:
        y_oy[1] = max(y)
    else:
        y_oy[1] = 0.5
    x_oy = [0, 0]

    plt.clf()
    if a2 <= 0 <= b1: plt.plot(x_oy, y_oy, color='black')
    plt.plot(x, y)
    plt.plot(x_ox, y_ox, color='black')
    plt.scatter(x_e, y_e, label='экстремумы', color='blue')
    plt.scatter(x0, y0, label='корни', color='red')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.legend()
    plt.grid(True)
    plt.show()

def f(x):
    return sin(x)*x

def f1(x):
    return cos(x) * x + sin(x)

def checker(a, b, h, eps, n):
    if a >= b:
        messagebox.showerror('Error', 'Неправильно задан интервал!')
    if h < 0 or h > abs(b-a):
        messagebox.showerror('Error', 'Неправильно задан шаг!')
    if eps <= 0:
        messagebox.showerror('Error', 'Неправильно задана точноть!')
    if n <= 0 or n - trunc(n) > 0:
        messagebox.showerror('Error', 'Неправильно задано количество итераций!')
    else:
        main(a, b, h, eps, n)

def get_values(event):
    a = entry_start.get()
    b = entry_end.get()
    h = entry_step.get()
    eps = entry_eps.get()
    n = entry_iters.get()
    try:
        a = float(a)
        b = float(b)
        h = float(h)
        eps = float(eps)
        n = float(n)
    except ValueError:
        messagebox.showerror('Error', 'Внимание, некорректный ввод!')
    else:
        checker(a, b, h, eps, n)

# Прокручивание
def scroll(*args):
    listbox_n.yview(*args)
    listbox_interval.yview(*args)
    listbox_root.yview(*args)
    listbox_func.yview(*args)
    listbox_iter.yview(*args)
    listbox_error.yview(*args)

table = {'n': [], 'ab': [], 'x': [], 'fx': [], 'N': [], 'err': []}

# Создаем окно
root = tk.Tk()
root.title('Нахождение корней функции.')
root.geometry('720x400')
root.resizable(width=False, height=False)

# Создаем виджеты
sb = tk.Scrollbar(root, command=scroll)

label_start = tk.Label(text='Начало')
label_end = tk.Label(text='Конец')
label_step = tk.Label(text='Шаг')
label_eps = tk.Label(text='Точность')
label_iters = tk.Label(text='Количество итераций')

label_n = tk.Label(text='N')
label_interval = tk.Label(text='[a, b]')
label_root = tk.Label(text='x')
label_f_root = tk.Label(text='f(x)')
label_iter = tk.Label(text='№ итерации')
label_error = tk.Label(text='Код ошибки')

entry_start = tk.Entry(root, width=20)
entry_end = tk.Entry(root, width=20)
entry_step = tk.Entry(root, width=20)
entry_eps = tk.Entry(root, width=20)
entry_iters = tk.Entry(root, width=20)

listbox_n = tk.Listbox(root, width=10, height=12,
                       yscrollcommand=sb.set)
listbox_interval = tk.Listbox(root, width=20, height=12,
                              yscrollcommand=sb.set)
listbox_root = tk.Listbox(root, width=20, height=12,
                          yscrollcommand=sb.set)
listbox_func = tk.Listbox(root, width=20, height=12,
                          yscrollcommand=sb.set)
listbox_iter = tk.Listbox(root, width=20, height=12,
                          yscrollcommand=sb.set)
listbox_error = tk.Listbox(root, width=10, height=12,
                           yscrollcommand=sb.set)

err_codes = tk.Label(root, text='Ошибки:\n0 - корень найден\n'+
                                '1 - производная равна нулю\n'+
                                '2 - превышено количество итераций\n'+
                                '3 - выход за пределы интервала',
                     justify=LEFT)

button_roots = tk.Button(root, text='Найти корни')

# Bindings
button_roots.bind('<Button-1>', get_values)
root.bind('<Return>', get_values)

# Размещаем виджеты
sb.place(x=700, y=150, height=165)

button_roots.grid(row=2, column=2)

label_start.grid(row=0, column=0, sticky='w')
label_end.grid(row=1, column=0, sticky='w')
label_step.grid(row=2, column=0, sticky='w')
label_eps.grid(row=3, column=0, sticky='w')
label_iters.grid(row=4, column=0, sticky='w')

entry_start.grid(row=0, column=1, columnspan=1)
entry_end.grid(row=1, column=1, columnspan=1)
entry_step.grid(row=2, column=1, columnspan=1)
entry_eps.grid(row=3, column=1, columnspan=1)
entry_iters.grid(row=4, column=1, columnspan=1)

err_codes.grid(row=0, column=3, rowspan=4, columnspan=2)

label_n.grid(row=7, column=0, columnspan=1)
label_interval.grid(row=7, column=1, columnspan=1)
label_root.grid(row=7, column=2, columnspan=1)
label_f_root.grid(row=7, column=3, columnspan=1)
label_iter.grid(row=7, column=4, columnspan=1)
label_error.grid(row=7, column=5, columnspan=1)

listbox_n.grid(row=9, column=0)
listbox_interval.grid(row=9, column=1)
listbox_root.grid(row=9, column=2)
listbox_func.grid(row=9, column=3)
listbox_iter.grid(row=9, column=4)
listbox_error.grid(row=9, column=5)

root.mainloop()
