'''
Составление таблицы замеров времени сортировки методом расчески
массивов трех различных размерностей.
Для каждой размерности массива исследуется случайный массив,
упорядоченный массив и отсортированный в обратном порядке массив.
Автор: Овчинникова Анастасия
'''

import tkinter as tk
import random
import time
from tkinter import messagebox

# CONST
CANVAS_HEIGHT = 500
CANVAS_WIDTH = 510
FLOOR_FOR_ARRAYS = -50
CEIL_FOR_ARRAYS = 50
STEP_FOR_ARRAYS = 1
FLOOR_FOR_ADDING = 0
CEIL_FOR_ADDING = 25
STEP_FOR_ADDING = 1
DEFAULT_MIN_ARRAY_LEN = 10
DEFAULT_MIDDLE_ARRAY_LEN = 100
DEFAULT_MAX_ARRAY_LEN = 1000
ERROR_ENTRY_BG = 'deep pink'
DEFAULT_BG = '#2d2d2d'


def create_button(canvas, text):
    ''' Создание кнопок '''

    button = tk.Button(canvas, text=text)
    return button


def comb_sort(array):
    '''
    Сортировка методом расчески
    :param array: массив
    :return: отсортированный массив
    '''

    time_begin = time.time()
    alen = len(array)
    gap = (alen*10//13) if alen > 1 else 0
    while gap:
        if 8 < gap < 11:
            gap = 11
        swapped = 0
        for i in range(alen - gap):
            if array[i+gap] < array[i]:
                array[i], array[i+gap] = array[i+gap], array[i]
                swapped = 1
        gap = (gap * 10 // 13) or swapped
    time_end = time.time()
    return (time_end-time_begin)*1000, array


def create_labels():
    '''
    Создает надписи
    :return: ничего
    '''

    label_min = tk.Label(text='Размер малого массива')
    label_min.place(x=60, y=150)
    label_medium = tk.Label(text='Размер среднего массива')
    label_medium.place(x=60, y=190)
    label_max = tk.Label(text='Размер большого массива')
    label_max.place(x=60, y=230)
    label_size = tk.Label(text='{:^30}'.format('Тип/Размер'))
    label_size.place(x=5, y=270)
    label_straight_sorted = tk.Label(text='{:^20}'.format('Сортированный\n') +
                                          '{:^20}'.format('в прямом подядке'))
    label_straight_sorted.place(x=5, y=310)
    label_reversed = tk.Label(text='{:^20}'.format('Сортированный\n') +
                                   '{:^20}'.format('в обратном подядке'))
    label_reversed.place(x=5, y=350)
    label_random = tk.Label(text='{:^30}'.format('Случайный'))
    label_random.place(x=5, y=390)
    label_units = tk.Label(text='{:^80}'.format('Время указано в миллисекундах'))
    label_units.place(x=60, y=430)
    label_rand_array = tk.Label(text='Случайный массив')
    label_rand_array.place(x=10, y=10)
    label_sorted_rand_array = tk.Label(text='Сортировка методом расчески')
    label_sorted_rand_array.place(x=10, y=50)


def create_changeable_labels_text(sizes):
    '''
    Выводит header таблицы (размер массивов)
    :param sizes:
    :return:
    '''
    label_min_size = tk.Label(text='{:^30}'.format(str(sizes[0])))
    label_min_size.place(x=135, y=270)
    label_middle_size = tk.Label(text='{:^30}'.format(str(sizes[1])))
    label_middle_size.place(x=260, y=270)
    label_max_size = tk.Label(text='{:^30}'.format(str(sizes[2])))
    label_max_size.place(x=385, y=270)


def create_changeable_label_time(time, x, y):
    '''
    Создает лейблы со временем (таблицу)
    :param time: время, за которое отсортировался какой-либо массив
    :param x: координата x, где разместить лэйбл со временем
    :param y: координата y, где разместить лэйбл со временем
    :return: ничего
    '''

    label = tk.Label(text='{:^30.7f}'.format(time))
    label.place(x=x, y=y)


def create_random_array(size):
    '''
    Генерирует случайный масиив заданной длины
    :param size: размер массива
    :return: случайно сгенерированный массив
    '''

    array = []
    for i in range(size):
        array.append(random.randrange(FLOOR_FOR_ARRAYS, CEIL_FOR_ARRAYS,
                                      STEP_FOR_ARRAYS))
    return array


def create_straight_sorted_array(size):
    '''
    Генерирует случайный отсортированный массив
    :param size: размер массива
    :return: случайно сгенерированный отсортированный массив
    '''

    array = [0]
    for i in range(1, size):
        array.append(array[i-1]+random.randrange(FLOOR_FOR_ADDING,
                                                 CEIL_FOR_ADDING,
                                                 STEP_FOR_ADDING))
    array = array[1:]
    return array


def create_reversed_array(size):
    '''
    Генерирует обратно отсортированный случайный массив
    :param size: размер массива
    :return: случайно сгенерированный обратно отсортированный массив
    '''

    array = [0]
    for i in range(1, size):
        array.append(array[i - 1] - random.randrange(FLOOR_FOR_ADDING,
                                                     CEIL_FOR_ADDING,
                                                     STEP_FOR_ADDING))
    array = array[1:]
    return array


def checker(value, entry):
    try:
        value = int(value)
    except ValueError:
        entry.delete(0, len(entry.get()))
        entry['bg'] = ERROR_ENTRY_BG
    else:
        entry['bg'] = DEFAULT_BG
    return value


def open_warning_window(message):
    messagebox.showwarning('Warning', message)


def get_size(entry_min, entry_middle, entry_max):
    '''
    Считывает введенные в поля ввода данные
    :param entry_min: поле ввода для размера малого массива
    :param entry_middle: поле ввода для размера среднего массива
    :param entry_max: поле ввода для размера большого массива
    :return:
    '''

    sizes = [0, 0, 0]
    sizes[0] = entry_min.get()
    sizes[1] = entry_middle.get()
    sizes[2] = entry_max.get()

    sizes[0] = checker(sizes[0], entry_min)
    sizes[1] = checker(sizes[1], entry_middle)
    sizes[2] = checker(sizes[2], entry_max)
    if type(sizes[0]) is int and \
        type(sizes[1]) is int and \
        type(sizes[2]) is int:
        if not (sizes[0] < sizes[1] < sizes[2]):
            open_warning_window('Размеры массивов указаны неточно! ')
        create_changeable_labels_text(sizes)
        x = 135  # Как у вертикальных хэдэров таблицы с длиной массива
        for i in sizes:
            y = 310  # Как у горизонтальных хэдэров таблицы с типом массива
            min_array = create_straight_sorted_array(i)
            middle_array = create_reversed_array(i)
            max_array = create_random_array(i)

            time_for_min, a = comb_sort(min_array)
            time_for_middle, a = comb_sort(middle_array)
            time_for_max, a = comb_sort(max_array)

            create_changeable_label_time(time_for_min, x, y)
            y += 40
            create_changeable_label_time(time_for_middle, x, y)
            y += 40
            create_changeable_label_time(time_for_max, x, y)

            x += 125


def create_entry(canvas, y, size, x=250):
    '''
    Создает поля ввода
    :param canvas: холст
    :param y: координата y поля ввода
    :param size: размер массива по умолчанию выводится в поле ввода при первом
    запуске программы
    :param x: координата x поля ввода
    :return: поле ввода
    '''

    entry = tk.Entry(canvas, width=30)
    entry.insert(0, size)
    entry.place(x=x, y=y)
    return entry


def convert_array_to_string(array):
    str_array = ''
    for i in array:
        str_array += str(i) + ','
    str_array = str_array[:-1]
    return str_array


def new_example_array(canvas):
    rand_array = create_random_array(10)
    print_rand_array = convert_array_to_string(rand_array)
    a, sorted_rand_array = comb_sort(rand_array)
    rand_array = convert_array_to_string(rand_array)
    sorted_rand_array = convert_array_to_string(sorted_rand_array)
    entry_rand_array = create_entry(canvas, 10, print_rand_array)
    entry_sorted_rand_array = create_entry(canvas, 50, sorted_rand_array)


def main():
    root = tk.Tk()
    root.title("Comb sorting")
    root.resizable(width=False, height=False)
    canvas = tk.Canvas(root, height=CANVAS_HEIGHT,
                       width=CANVAS_WIDTH)
    canvas.grid(row=1, column=0)

    create_labels()

    entry_min = create_entry(canvas, 150, DEFAULT_MIN_ARRAY_LEN)
    entry_middle = create_entry(canvas, 190, DEFAULT_MIDDLE_ARRAY_LEN)
    entry_max = create_entry(canvas, 230, DEFAULT_MAX_ARRAY_LEN)

    new_example_array(canvas)

    get_size(entry_min, entry_middle, entry_max)

    button_sort = create_button(canvas, 'Пересчитать')
    button_sort.bind('<Button-1>', lambda x: get_size(entry_min, entry_middle, entry_max))
    button_sort.place(x=200, y=460)

    button_new_array = create_button(canvas, 'Другой массив')
    button_new_array.bind('<Button-1>', lambda x: new_example_array(canvas))
    button_new_array.place(x=220, y=90)

    root.mainloop()


main()
