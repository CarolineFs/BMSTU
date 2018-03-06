import tkinter as tk
import random
import time

# CONST
CANVAS_HEIGHT = 400
CANVAS_WIDTH = 500
FLOOR_FOR_ARRAYS = -50
CEIL_FOR_ARRAYS = 50
STEP_FOR_ARRAYS = 1
FLOOR_FOR_ADDING = 0
CEIL_FOR_ADDING = 25
STEP_FOR_ADDING = 1


def create_button(canvas, text):
    button = tk.Button(canvas, text=text)
    return button


def comb_sort(array):
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
    # print('Me', time_begin, time_end)
    # print(time_end-time_begin)
    return array, time_end-time_begin


def create_labels():
    '''
    Создает надписи
    :return: ничего
    '''

    label_min = tk.Label(text='Размер малого массива')
    label_min.place(x=60, y=10)
    label_medium = tk.Label(text='Размер среднего массива')
    label_medium.place(x=60, y=50)
    label_max = tk.Label(text='Размер большого массива')
    label_max.place(x=60, y=90)
    label_size = tk.Label(text='{:^30}'.format('Тип/Размер'))
    label_size.place(x=5, y=130)
    label_straight_sorted = tk.Label(text='{:^20}'.format('Сортированный\n') +
                                          '{:^20}'.format('в прямом подядке'))
    label_straight_sorted.place(x=5, y=170)
    label_reversed = tk.Label(text='{:^20}'.format('Сортированный\n') +
                                   '{:^20}'.format('в обратном подядке'))
    label_reversed.place(x=5, y=210)
    label_random = tk.Label(text='{:^30}'.format('Случайный'))
    label_random.place(x=5, y=250)


def create_changeable_labels_text(sizes):
    label_min_size = tk.Label(text='{:^30}'.format(str(sizes[0])))
    label_min_size.place(x=135, y=130)
    label_middle_size = tk.Label(text='{:^30}'.format(str(sizes[1])))
    label_middle_size.place(x=260, y=130)
    label_max_size = tk.Label(text='{:^30}'.format(str(sizes[2])))
    label_max_size.place(x=385, y=130)


def create_changeable_label_time(time, x, y):
    label = tk.Label(text=':^30.10f'.format(time))
    label.place(x=x, y=y)


def create_random_array(size):
    array = []
    for i in range(size):
        array.append(random.randrange(FLOOR_FOR_ARRAYS, CEIL_FOR_ARRAYS,
                                      STEP_FOR_ARRAYS))
    return array


def create_straight_sorted_array(size):
    array = [0]
    for i in range(1, size):
        array.append(array[i-1]+random.randrange(FLOOR_FOR_ADDING,
                                                 CEIL_FOR_ADDING,
                                                 STEP_FOR_ADDING))
    array = array[1:]
    return array


def create_reversed_array(size):
    array = [0]
    for i in range(1, size):
        array.append(array[i - 1] - random.randrange(FLOOR_FOR_ADDING,
                                                     CEIL_FOR_ADDING,
                                                     STEP_FOR_ADDING))
    array = array[1:]
    return array


def get_size(entry_min, entry_middle, entry_max):
    sizes = [0, 0, 0]
    sizes[0] = int(entry_min.get())
    sizes[1] = int(entry_middle.get())
    sizes[2] = int(entry_max.get())
    create_changeable_labels_text(sizes)
    for i in sizes:
        min_array = create_straight_sorted_array(i)
        middle_array = create_reversed_array(i)
        max_array = create_random_array(i)

        min_array, time_for_min = comb_sort(min_array)
        middle_array, time_for_middle = comb_sort(min_array)
        max_array, time_for_max = comb_sort(min_array)
        # ДОДЕЛАТЬ, ВЫВОД ПОДСЧИТАНОГО ВРЕМЕНИ
        # ПРИДУМАТЬ, КАК ПЕРЕДАТЬ ФУНКЦИИ ВЫВОДА КООРДИНАТЫ





def create_entry(canvas, y, size, x=250):
    entry = tk.Entry(canvas, width=30)
    entry.insert(0, size)
    entry.place(x=x, y=y)
    return entry


def main():
    root = tk.Tk()
    root.title("Comb sorting")
    root.resizable(width=False, height=False)
    canvas = tk.Canvas(root, height=CANVAS_HEIGHT,
                       width=CANVAS_WIDTH)
    canvas.grid(row=1, column=0)

    create_labels()

    entry_min = create_entry(canvas, 10, 10)
    entry_middle = create_entry(canvas, 50, 100)
    entry_max = create_entry(canvas, 90, 1000)

    get_size(entry_min, entry_middle, entry_max)

    button_sort = create_button(canvas, 'Go')
    button_sort.bind('<Button-1>', lambda x: get_size(entry_min, entry_middle, entry_max))
    button_sort.place(x=240, y=360)


    root.mainloop()


main()
