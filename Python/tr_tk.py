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
        self.canvas = tk.Canvas(root, height = self.height,\
                                width = self.width, bg = 'light grey')
        self.canvas.grid(row = 0, column = 0)
        self.canvas.create_rectangle(0, 10, 400, 650,
                                     fill = 'white',
                                     outline = 'white')
        
        self.add_button = tk.Button(self.canvas, text = 'Add')
        self.add_entry = tk.Entry(self.canvas, width = 15, bd = 3)
        self.add_entry.place(x = 450, y = 50)
        #self.add_entry.bind('<Return>', lambda e: self.getter)
        self.add_button.bind('<Button-1>', self.getter)
        self.add_button.place(x = 550, y = 50)
        self.show_button = tk.Button(self.canvas, text = 'Show graph').place(x = 450, y = 100)

        #self.canvas.create_rectangle(450, 150, 590, 600,
                                     #fill = 'white',
                                     #outline = 'white')

        self.clear_button = tk.Button(self.canvas, text = 'Clear all')
        self.clear_button.bind('<Button-1>', self.clear_all)
        self.clear_button.place(x = 500, y = 630)
        

    
    
    def getter(self, event):
        new_coords = self.add_entry.get()
        self.add_entry.delete(0, END)
        self.shower(new_coords)

    def shower(self, new_coords):
        text = tk.Text(root, width = 15, height = 25)
        text.place(x = 450, y = 150)
        text.config(takefocus=0)
        text.insert(END, new_coords+'\n')
        
    
    def clear_all(self, event):
        pass


root = tk.Tk()
graph = graph(root)

root.mainloop()


