import tkinter as tk
from tkinter import messagebox
import matplotlib
from math import sin

# CONST
CANVAS_HEIGHT = 500
CANVAS_WIDTH = 500
DEFAULT_CANVAS_BG = 'misty rose'
DEFAULT_ENTRY_BG = 'lavender blush'
DEFAULT_LABEL_BG = 'misty rose'
DEFAULT_BUTTON_BG = 'lavender blush'
ERROR_ENTRY_BG = 'pink'


def f(x):
    return sin(x)


def open_warning_window(message):
    messagebox.showwarning('Warning', message)


def create_labels(bg='misty rose'):
    label_epsilon = tk.Label(text='Точность', bg=bg)
    label_epsilon.place(x=10, y=10)

    label_start = tk.Label(text='Начало', bg=bg)
    label_start.place(x=10, y=50)

    label_end = tk.Label(text='Конец', bg=bg)
    label_end.place(x=10, y=90)

    label_step = tk.Label(text='Шаг', bg=bg)
    label_step.place(x=10, y=130)


def create_chart():
    pass


def create_entry(canvas, y, x, width):
    entry = tk.Entry(canvas, width=width, bg=DEFAULT_ENTRY_BG)
    entry.place(x=x, y=y)
    return entry


def canvas_creator(root):
    canvas = tk.Canvas(root,
                       height=CANVAS_HEIGHT,
                       width=CANVAS_WIDTH,
                       bg=DEFAULT_CANVAS_BG)
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


def get_values(entry_start, entry_end, entry_epsilon, entry_step):
    a = entry_start.get()
    b = entry_end.get()
    eps = entry_epsilon.get()
    h = entry_step.get()
    a = checker(a, entry_start)
    b = checker(b, entry_end)
    eps = checker(eps, entry_epsilon)
    h = checker(h, entry_step)
    if type(a) is float and\
        type(b) is float and\
        type(eps) is float and\
        type(h) is float:
        if a >= b or h <= 0:
            entry_start['bg'] = ERROR_ENTRY_BG
            entry_end['bg'] = ERROR_ENTRY_BG
            open_warning_window('Начальное значение отрезка больше или равно конечного. ')
        else:
            pass


def main():
    root = tk.Tk()
    root.title('Roots')
    root.resizable(width=False, height=False)

    canvas = canvas_creator(root)

    create_labels()

    entry_epsilon = create_entry(canvas, 10, 80, 20)
    entry_start = create_entry(canvas, 50, 80, 20)
    entry_end = create_entry(canvas, 90, 80, 20)
    entry_step = create_entry(canvas, 130, 80, 20)

    result_button = tk.Button(canvas, text='Найти корни',
                              bg=DEFAULT_BUTTON_BG)
    result_button.bind('<Button-1>',
                       lambda x: get_values(entry_start,
                                            entry_end,
                                            entry_epsilon,
                                            entry_step))
    result_button.place(x=230, y=460)

    root.mainloop()


main()
