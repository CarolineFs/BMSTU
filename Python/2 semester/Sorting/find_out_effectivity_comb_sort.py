import tkinter as tk
import random
import time

# CONST
CANVAS_HEIGHT = 300
CANVAS_WIDTH = 300


array1 = [2, 4, 1, 5, 2, 10, 3, 54, 4, 4]


def create_button(canvas, text):
    button = tk.Button(canvas, text=text)
    return button


def comb_sort(array):
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
    return array


def main():
    root = tk.Tk()
    root.title("Comb sorting")
    canvas = tk.Canvas(root, height=CANVAS_HEIGHT,
                       width=CANVAS_WIDTH)
    canvas.grid(row=1, column=0)

    button_sort = create_button(canvas, 'Sort')
    button_sort.bind('<Button-1>')
    button_sort.place(x=100, y=100)


    root.mainloop()


main()
