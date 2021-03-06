import tkinter as tk
from tkinter.filedialog import *
from ErrorCatcher import CatchFloatError as cfe
from math import ceil
from triangle_affiliation import main as ta
from itertools import combinations
from math import sqrt, trunc
import copy


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
        self.center_x = (self.x2-self.x1)//2+self.x1
        self.center_y = (self.y2-self.y1)//2+self.y1

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
        self.add_entry.bind('<Return>', self.getter)
        self.add_entry.place(x=450, y=50)
        # self.add_entry.bind('<Return>', lambda e: self.getter)

        self.show_button = tk.Button(self.canvas, text = 'Show graph')
        self.show_button.bind('<Button-1>', self.point_drawer)
        self.show_button.place(x = 450, y = 110)

        self.clear_button = tk.Button(self.canvas, text = 'Clear all')
        self.clear_button.bind('<Button-1>', self.clear_all)
        self.clear_button.place(x = 450, y = 640)

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
        x_max = abs(self.normal_coords[0][0])
        y_max = abs(self.normal_coords[0][1])
        for i in range(len(self.normal_coords)):
            if abs(self.normal_coords[i][0]) > x_max:
                x_max = abs(self.normal_coords[i][0])
            if abs(self.normal_coords[i][1]) > y_max:
                y_max = abs(self.normal_coords[i][1])
        self.l_x = self.center_x - self.x1
        self.l_y = self.center_y - self.y1
        if x_max >= 1:
            x_max += 1
        else:
            x_max += 0.1
        if y_max >= 1:
            y_max += 1
        else:
            y_max += 0.1
        kf_x = self.l_x/x_max
        kf_y = self.l_y/y_max
        self.kf = min(kf_x, kf_y)
        self.kf = round(self.kf, 6)
        for i in range(len(self.normal_coords)):
            x = self.normal_coords[i][0]
            if abs(x) > self.l_x:
                x = ceil(x*self.kf)

            else:
                if self.kf != 0:
                    x = ceil(x*self.kf)
            #x += self.x1

            y = self.normal_coords[i][1]
            if abs(y) > self.l_y:
                y = ceil(y*self.kf)
            else:
                if self.kf != 0:
                    y = ceil(y*self.kf)
            
            x += self.center_x
            if y > 0:
                y = self.center_y - y
            else:
                y = self.center_y + abs(y)
            #y += self.y1
            self.canvas.create_line(x-5, y,
                                    x+5, y,
                                    width=1)
            self.canvas.create_line(x, y-5,
                                    x, y+5,
                                    width=1)

        if len(self.normal_coords) >= 3:
            self.choose_points(self)
        

    def coords_ch(self, st):
        if st[0] > self.l_x:
            st[0] = ceil(st[0]*self.kf)
        else:
            if self.kf != 0:
                st[0] = ceil(st[0]*self.kf)


        if st[1] > self.l_y:
            st[1] = ceil(st[1]*self.kf)
        else:
            if self.kf != 0:
                st[1] = ceil(st[1]*self.kf)


        st[0] += self.center_x
        if st[1] > 0:
            st[1] = self.center_y - st[1]
        else:
            st[1] = self.center_y + abs(st[1])
        return st
            
                
    def triangle_drawer(self, event):
        p1 = copy.deepcopy(self.min_coords[0])
        p2 = copy.deepcopy(self.min_coords[1])
        p3 = copy.deepcopy(self.min_coords[2])
        p1 = self.coords_ch(p1)
        p2 = self.coords_ch(p2)
        p3 = self.coords_ch(p3)
        self.canvas.create_line(p1[0], p1[1],
                                p2[0], p2[1],
                                width = 1)
        self.canvas.create_line(p1[0], p1[1],
                                p3[0], p3[1],
                                width=1)
        self.canvas.create_line(p2[0], p2[1],
                                p3[0], p3[1],
                                width=1)


    def choose_points(self, event):
        #ищем комбинацию из трех точек, где разница минимальна
        coords_comb = list(combinations(self.normal_coords, 3))
        self.min_coords = coords_comb[0]
        min_dif = -1  #обственно, та самая разница
        f = 0  #флаг, чтобы не сравнивать первую вычисленную разницу с -1
        fd = 0 #флаг на ошибку, если точки лежат на одной прямой
        current_dif = -1 #разница для текущей тройки точек
        for set in coords_comb:
            a = sqrt((set[0][0]-set[1][0])**2+(set[0][1]-set[1][1])**2)
            b = sqrt((set[1][0]-set[2][0])**2+(set[1][1]-set[2][1])**2)
            c = sqrt((set[2][0]-set[0][0])**2+(set[2][1]-set[0][1])**2)
            if a + b > c and \
               a + c > b and \
               b + c > a:
                fd = 1  #можно построить хотя бы один треугольник при заданнолм наборе точек
                points_in = 0
                points_out = 0
                for point in self.normal_coords:
                    if point != set[0] and point != set[1] and point != set[2]:
                        flag = ta(point[0], point[1], set)
                        if flag == 1:
                            points_in += 1
                        elif flag == 0:
                            points_out += 1

                
                if f == 0:
                    min_dif = abs(points_out - points_in)
                    #current_dif = abs(points_out - points_in)
                    f = 1
                else:
                    #print(abs(points_out - points_in), min_dif)
                    if abs(points_out - points_in) <= min_dif:
                        min_dif = abs(points_out - points_in)
                        self.min_coords = set
        
            
            


        if fd:
            self.triangle_drawer(self)
        else:
            self.canvas.create_rectangle(450, 80, 600, 100, fill='pink',
                                         outline='pink')
            self.canvas.create_text(450, 90, text='Это прямая', anchor='w')
        


root = tk.Tk()
graph = graph(root)
root.mainloop()
