import tkinter as tk
from math import trunc

# CONST
BASE8 = 16
BASE10 = 10
CANVAS_HEIGHT = 200
CANVAS_WIDTH = 300


def clear_all(entry_8, entry_10):
    entry_8.delete(0, len(entry_8.get()))
    entry_10.delete(0, len(entry_10.get()))


def clear_one_entry(entry):
    entry.delete(0, len(entry.get()))


def show_result(entry, result):
    clear_one_entry(entry)
    entry.insert(0, result)


def get_10(entry_8, entry_10):
    flag = False
    number_10 = float(entry_10.get())
    if number_10 < 0:
        flag = True
        number_10 *= -1

    integer, fraction = str(number_10).split('.')
    integer, fraction = int(integer), int(fraction)
    fraction = fraction/(10**len(str(fraction)))

    res = ''
    num16 = ['A', 'B', 'C', 'D', 'E', 'F']
    num10 = [10, 11, 12, 13, 14, 15]
    while integer >= BASE8:
        div = int(integer // BASE8)
        mod = int(integer % BASE8)
        if div == 0:
            if mod in num10:
                mod = num16[num10.index(mod)]
            res = str(mod) + res
            break
        else:
            if mod in num10:
                mod = num16[num10.index(mod)]
            res = str(mod) + res
        integer //= BASE8

    if integer in num10:
        integer = num16[num10.index(integer)]
    res = str(integer) + res
    if fraction > 0:
        res += '.'
        k = 0
        while (fraction > 0) and (k < 9):
            fraction *= BASE8
            ins = trunc(fraction)
            if ins in num10:
                ins = num16[num10.index(ins)]
            res += str(ins)
            fraction = round(float('0.' + str(fraction).split('.')[1]), 10)
            k += 1
    else:
        res += '.0'

    if flag:
        res = '-' + res
    show_result(entry_8, res)


def create_button(canvas, text):
    button = tk.Button(canvas, text=text)
    return button


def draw_canvas(root):
    canvas = tk.Canvas(root, height=CANVAS_HEIGHT,
                       width=CANVAS_WIDTH)
    canvas.grid(row=0, column=0)

    entry_10 = tk.Entry(canvas, width=18)
    entry_10.place(x=150, y=50)
    entry_10.focus()

    label_10 = tk.Label(text='Число в 10-ой с/с: ')
    label_10.place(x=10, y=50)

    entry_8 = tk.Entry(canvas, width=18)
    entry_8.place(x=150, y=100)

    label_8 = tk.Label(text='Число в 16-ой с/с: ')
    label_8.place(x=10, y=100)

    button_10_to_8 = create_button(canvas, '10 to 16')
    button_10_to_8.bind('<Button-1>', lambda x: get_10(entry_8, entry_10))
    button_10_to_8.place(x=125, y=160)

    button_delete = create_button(canvas, 'Clear all')
    button_delete.bind('<Button-1>', lambda x1: clear_all(entry_8, entry_10))
    button_delete.place(x=200, y=160)


def main():
    root = tk.Tk()
    root.title('Calculator')
    root.resizable(width=False, height=False)

    draw_canvas(root)

    root.mainloop()


main()
