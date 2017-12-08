import tkinter as tk
from tkinter.filedialog import *





class graph:
    def __init__(self, parent):
        self.parent = parent
        parent.title('Triangle')
        self.canv_width = 200
        self.canv_height = 200
        self.width = 600
        self.height = 700
        self.canvas = tk.Canvas(root, height = self.height,\
                                width = self.width, bg = 'light grey')
        self.canvas.grid(row = 0, column = 0)
        self.canvas.create_rectangle(0, 10, 400, 600,
                                     fill = 'white',
                                     outline = 'white')
        self.add_button = tk.Button(self.canvas, text = 'Add').place(x = 550, y = 50)
        self.add_entry = tk.Entry(self.canvas, width = 15, bd = 3).place(x = 450, y = 50)
        self.show_button = tk.Button(self.canvas, text = 'Show graph').place(x = 450, y = 100)

    def getter(self):
        
          
    
        
        #self.parent.bind('<>'



root = tk.Tk()
graph = graph(root)

root.mainloop()
