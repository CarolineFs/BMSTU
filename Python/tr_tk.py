import tkinter as tk
from tkinter.filedialog import *
from ErrorCatcher import CatchFloatError as cfe
from math import ceil
from triangle affiliation import main as ta


class graph:
    def __init__(self, parent):
        self.parent = parent
        parent.title('Triangle')
        self.canv_width = 200
        self.canv_height = 200
        self.width = 600
        self.height = 700
        self.x1 = 10
        self.x2 = 410
        self.y1 = 10
        self.y2 = 660

        self.parent.resizable(width = False, height = False) #запрет на изменение размера

        self.canvas = tk.Canvas(root, height = self.height,
                                width = self.width, bg = 'light grey')
        self.canvas.grid(row = 0, column = 0)
        self.canvas.create_rectangle(self.x1 - 10, self.y1 - 10,
                                     self.x2 + 10, self.y2 + 10,
                                     fill = 'white',
                                     outline = 'white')

        self.canvas.create_text(450, 25, text='Введите координаты \n через пробел:',
                                anchor='w')
        # self.canvas.create_rectangle(450, 150, 590, 600,
        # fill = 'white',
        # outline = 'white')

        self.add_button = tk.Button(self.canvas, text = 'Add')
        self.add_button.bind('<Button-1>', self.getter)
        self.add_button.place(x=550, y=50)

        self.add_entry = tk.Entry(self.canvas, width=10, bd=3)
        self.add_entry.place(x=450, y=50)
        # self.add_entry.bind('<Return>', lambda e: self.getter)

        self.show_button = tk.Button(self.canvas, text = 'Show graph')
        self.show_button.bind('<Button-1>', self.point_drawer)
        self.show_button.place(x = 450, y = 110)

        self.clear_button = tk.Button(self.canvas, text = 'Clear all')
        self.clear_button.bind('<Button-1>', self.clear_all)
        self.clear_button.place(x = 450, y = 630)

        self.text = tk.Text(root, width = 15, height = 30)
        self.text.place(x = 450, y = 150)
        self.text.config(takefocus=0)

        self.canvas.create_rectangle(450, 80, 600, 100, fill='light green',
                                     outline='light green')

        self.coords_str = ''
        self.normal_coords = []


    def getter(self, event):
        self.canvas.create_rectangle(450, 80, 600, 100, fill='light green',
                                     outline='light green')
        new_coords = self.add_entry.get()
        f = 0
        new_coords = new_coords.strip()
        for i in range(len(new_coords)):
            if new_coords[i] == ' ':
                if f != 0:
                    f = 1
                else:
                    f = 2
        if f != 2:
            self.canvas.create_rectangle(450, 80, 600, 100, fill='pink',
                                     outline='pink')
            self.canvas.create_text(450, 90, text = 'Некорректный ввод', anchor='w')
        else:
            x, y = new_coords.split()
            x = cfe(x)
            y = cfe(y)
            if type(x) != float or type(y) != float:
                self.canvas.create_rectangle(450, 80, 600, 100, fill='pink',
                                             outline='pink')
                self.canvas.create_text(450, 90, text='Некорректный ввод', anchor='w')
            else:
                self.coords_str += new_coords + '\n'
                self.normal_coords.append([x, y])
                '''if len(self.normal_coords) >= 3:
                    self.drawer(self.coords_str)'''
        self.add_entry.delete(0, END)
        self.shower(self)


    def shower(self, event):
        self.text.delete('1.0', END)
        self.text.insert(END, self.coords_str)


    def clear_all(self, event):
        self.point_drawer(self.normal_coords)
        self.coords_str = ''
        self.normal_coords = []
        self.shower(self.coords_str)
        self.canvas.create_rectangle(self.x1 - 10, self.y1 - 10,
                                     self.x2 + 10, self.y2 + 10,
                                     fill='white',
                                     outline='white')


    def point_drawer(self, event):
        self.canvas.create_rectangle(self.x1 - 10, self.y1 - 10,
                                     self.x2 + 10, self.y2 + 10,
                                     fill='white',
                                     outline='white')
        x_max = self.normal_coords[0][0]
        y_max = self.normal_coords[0][1]
        for i in range(len(self.normal_coords)):
            if self.normal_coords[i][0] > x_max:
                x_max = self.normal_coords[i][0]
            if self.normal_coords[i][1] > y_max:
                y_max = self.normal_coords[i][1]
        l_x = self.x2 - self.x1
        l_y = self.y2 - self.y1
        kf = max(ceil(x_max/l_x), ceil(y_max/l_y)) -1

        for i in range(len(self.normal_coords)):
            x = self.normal_coords[i][0]
            if x > l_x:
                x = x - kf*l_x
            else:
                if kf != 0:
                    x = ceil(x/kf)
            x += self.x1 - 1
            y = self.normal_coords[i][1]
            if y > l_y:
                y = y - kf*l_y
            else:
                if kf != 0:
                    y = ceil(y/kf)
            y += self.y1 - 1
            self.canvas.create_line(x-5, y,
                                    x+5, y,
                                    width =1)
            self.canvas.create_line(x, y-5,
                                    x, y+5,
                                    width=1)

    def triangle_drawer(self, event):
        pass


    def choose_points(self, event):






root = tk.Tk()
graph = graph(root)

root.mainloop()
