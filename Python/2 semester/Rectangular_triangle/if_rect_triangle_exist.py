'''Программа программа проверяет, можно ли построить прямоугольный треугольник со сторонами заданных длин.
ПРОВЕРОК НЕТ
'''

import tkinter as tk
from math import sqrt


def create_entry(canvas, x, y=10, width=15):
    entry = tk.Entry(canvas, width=width)
    entry.place(x=x, y=y)
    return entry


def create_label():
    label_x = tk.Label(text='x')
    label_x.place(x=150, y=10)
    label_y = tk.Label(text='y')
    label_y.place(x=350, y=10)
    label_z = tk.Label(text='z')
    label_z.place(x=560, y=10)
    label_result = tk.Label(text='Результат')
    label_result.place(x=10, y=100)


def error(entry_result):
    entry_result.insert(0, 'Невозможно построить прямоугольный треугольник')


def getter(entry_x, entry_y, entry_z, entry_result):
    entry_result.delete(0, len(entry_result.get()))
    x = int(entry_x.get())
    y = int(entry_y.get())
    z = int(entry_z.get())
    if (x+y > z) and (x+z > y) and (y+z > z):
        if (x*x == y*y + z*z) or (
                y*y == x*x + z*z) or (
                z*z == x*x + y*y):
            p = (x+y+z)/2
            s = sqrt(p*(p-x)*(p-y)*(p-z))
            entry_result.delete(0, len(entry_result.get()))
            entry_result.insert(0, 'S = ' + str(s))
        else:
            error(entry_result)
    else:
        error(entry_result)


def main():
    root = tk.Tk()
    root.title("Triangle")
    root.resizable(height=False, width=False)

    canvas = tk.Canvas(root, height=200, width=600)
    canvas.grid(row=0, column=0)

    create_label()

    entry_x = create_entry(canvas, 10)
    entry_y = create_entry(canvas, 210)
    entry_z = create_entry(canvas, 410)
    entry_result = create_entry(canvas, x=100, y=100, width=50)

    button = tk.Button(canvas, text='Площадь')
    button.bind('<Button-1>', lambda x: getter(entry_x, entry_y, entry_z, entry_result))
    button.place(x=280, y=160)

    root.mainloop()


main()
