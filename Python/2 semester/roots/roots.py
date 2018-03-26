import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
from math import sin

# CONST
CANVAS_HEIGHT = 500
CANVAS_WIDTH = 840
ERROR_ENTRY_BG = 'pink'
DEFAULT_ENTRY_BG = 'dark grey'


def f(x):
    return sin(x)


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

    code1 = tk.Label(text='00 - без ошибок')
    code1.place(x=460, y=40)

    code1 = tk.Label(text='01 - превышение количества итераций')
    code1.place(x=460, y=60)

    code1 = tk.Label(text='10 - выход за пределы интервала')
    code1.place(x=460, y=80)

    code1 = tk.Label(text='11 - производная равна нулю')
    code1.place(x=460, y=100)


def create_chart(canvas):
    pass


def create_entry(canvas, y, x, width):
    entry = tk.Entry(canvas, width=width, bg=DEFAULT_ENTRY_BG)
    entry.place(x=x, y=y)
    return entry


def create_listbox(canvas, x, y, width=20, height=12):
    listbox = tk.Listbox(canvas, width=width, height=height,
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


def get_values(entry_start, entry_end, entry_epsilon, entry_step, button):
    flag = 0
    a = entry_start.get()
    b = entry_end.get()
    eps = entry_epsilon.get()
    h = entry_step.get()
    a = checker(a, entry_start)
    b = checker(b, entry_end)
    eps = checker(eps, entry_epsilon)
    h = checker(h, entry_step)

    if type(a) is float and type(b) is float:
        if a >= b:
            print('R')
            entry_start['bg'] = ERROR_ENTRY_BG
            entry_end['bg'] = ERROR_ENTRY_BG
            entry_start.delete(0, len(entry_start.get()))
            entry_end.delete(0, len(entry_end.get()))
            open_warning_window('Начальное значение отрезка больше или равно конечного!')
            flag = 1

    if type(h) is float:
        if h <= 0:
            entry_step.delete(0, len(entry_step.get()))
            entry_step['bg'] = ERROR_ENTRY_BG
            open_warning_window('Задан шаг меньший или равный нулю!')
            flag = 1
    if type(eps) is float:
        if eps <= 0:
            entry_epsilon.delete(0, len(entry_epsilon.get()))
            open_warning_window('Неправильно указана точность!')
            entry_epsilon['bg'] = DEFAULT_ENTRY_BG
            flag = 1
        if eps <= 1e-323:
            entry_epsilon.delete(0, len(entry_epsilon.get()))
            open_warning_window('Слишком высокая точность!')
            entry_epsilon['bg'] = DEFAULT_ENTRY_BG
            flag = 1
    if flag:
        if button == 'roots':
            find_roots()
        else:
            create_chart()


def find_roots():
    pass


def main():
    root = tk.Tk()
    root.title('Roots')
    root.resizable(width=False, height=False)

    canvas = canvas_creator(root)

    create_static_labels()

    entry_epsilon = create_entry(canvas, 10, 80, 20)
    entry_start = create_entry(canvas, 50, 80, 20)
    entry_end = create_entry(canvas, 90, 80, 20)
    entry_step = create_entry(canvas, 130, 80, 20)

    listbox_n = create_listbox(canvas, 5, 240)
    listbox_interval = create_listbox(canvas, 145, 240)
    listbox_root = create_listbox(canvas, 285, 240)
    listbox_func = create_listbox(canvas, 425, 240)
    listbox_iter = create_listbox(canvas, 565, 240)
    listbox_error = create_listbox(canvas, 705, 240)

    result_button = tk.Button(canvas, text='Найти корни')
    result_button.bind('<Button-1>',
                       lambda x: get_values(entry_start,
                                            entry_end,
                                            entry_epsilon,
                                            entry_step,
                                            'roots'))
    result_button.place(x=300, y=90)
    chart_button = tk.Button(canvas, text='Показать график')
    chart_button.bind('<Button-1>',
                      lambda x: get_values(entry_start,
                                           entry_end,
                                           entry_epsilon,
                                           entry_step,
                                           'chart'))
    chart_button.place(x=300, y=50)

    '''frame_error = tk.LabelFrame(canvas, width=350, height=180,
                           bg='RosyBrown1', text='Коды ошибок')
    frame_error.place(x=450, y=10)'''

    root.mainloop()


main()
