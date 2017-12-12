import tkinter as tk
from tkinter.filedialog import *
from ErrorCatcher import CatchIntError as cie
from ErrorCatcher import CatchFloatError as cfe






class graph:
    def __init__(self, parent):
        self.parent = parent
        parent.title('Triangle')
        self.canv_width = 200
        self.canv_height = 200
        self.width = 600
        self.height = 700
        self.parent.resizable(width = False, height = False) #запрет на изменение размера

        self.canvas = tk.Canvas(root, height = self.height,
                                width = self.width, bg = 'light grey')
        self.canvas.grid(row = 0, column = 0)
        self.canvas.create_rectangle(0, 10, 400, 650,
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

        self.show_button = tk.Button(self.canvas, text = 'Show graph').place(x = 450, y = 110)


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
        self.add_entry.delete(0, END)
        self.shower(self.coords_str)

    def shower(self, coords_str):
        self.text.delete('1.0', END)
        self.text.insert(END, self.coords_str)
        
    
    def clear_all(self, event):
        self.coords_str = ''
        self.shower(self.coords_str)


root = tk.Tk()
graph = graph(root)

root.mainloop()
