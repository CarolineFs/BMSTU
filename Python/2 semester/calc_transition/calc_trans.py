import tkinter as tk
from math import trunc

# CONST
BASE = 8


def clear_all(entry_8, entry_10):
    entry_8.delete(0, len(entry_8.get()))
    entry_10.delete(0, len(entry_10.get()))


def clear_one_entry(entry):
    entry.delete(0, len(entry.get()))


def get_8(entry_8, entry_10):
    flag = False
    number_8 = float(entry_8.get())
    if number_8 < 0:
        flag = True
        number_8 *= -1

    integer, fraction = str(number_8).split('.')
    integer, fraction = integer, fraction
    res = 0

    for i in range(len(integer)):
        res += (int(integer[i]) * (BASE ** i))

    ind = -1
    for i in fraction:
        res += int(i)*(BASE**ind)
        print(len(fraction)*-1, ind)
        '''if ind == -1*len(fraction):
            print('YES')
            break'''
        ind -= 1
    if flag:
        res *= -1
    show_result(entry_10, res)


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
    while integer >= BASE:
        div = int(integer // BASE)
        mod = int(integer % BASE)
        if div == 0:
            res = str(mod) + res
            break
        else:
            res = str(mod) + res
        integer //= BASE
    res = str(int(integer)) + res
    if fraction > 0:
        res += '.'
        k = 0
        while (fraction > 0) and (k <= 10):
            fraction *= BASE
            res += str(trunc(fraction))
            fraction = round(float('0.' + str(fraction).split('.')[1]), 10)
            print(fraction)
            k += 1
    else:
        res += '.0'

    if flag:
        res = '-' + res
    show_result(entry_8, res)


def create_button(canvas, text):
    button = tk.Button(canvas, text=text)
    return button


def draw_canwas(root):
    # CONST
    CANVAS_HEIGHT = 200
    CANVAS_WIDTH = 300

    canvas = tk.Canvas(root, height=CANVAS_HEIGHT,
                       width=CANVAS_WIDTH)
    canvas.grid(row=0, column=0)

    entry_10 = tk.Entry(canvas, width=20)
    entry_10.place(x=150, y=50)
    entry_10.focus()

    label_10 = tk.Label(text='Число в 10-ой с/с: ')
    label_10.place(x=10, y=50)

    entry_8 = tk.Entry(canvas, width=20)
    entry_8.place(x=150, y=100)

    label_8 = tk.Label(text='Число в 8-ой с/с: ')
    label_8.place(x=10, y=100)

    button_8_to_10 = create_button(canvas, '8 to 10')
    button_8_to_10.bind('<Button-1>', lambda x: get_8(entry_8, entry_10))
    button_8_to_10.place(x=50, y=160)

    button_10_to_8 = create_button(canvas, '10 to 8')
    button_10_to_8.bind('<Button-1>', lambda x: get_10(entry_8, entry_10))
    button_10_to_8.place(x=125, y=160)

    button_delete = create_button(canvas, 'Clear all')
    button_delete.bind('<Button-1>', lambda x: clear_all(entry_8, entry_10))
    button_delete.place(x=200, y=160)


def main():
    root = tk.Tk()
    root.title('Calculator')
    root.resizable(width=False, height=False)

    draw_canwas(root)

    root.mainloop()


main()
