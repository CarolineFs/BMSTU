import tkinter as tk
import random
from matrix_rotation import rotate_array as ra
#import pygame as pg



#const

WIDTH = 250
HEIGHT = 350
BG = 'white'
OUTLINE = 'black'
COLORS = ['aqua', 'blue', 'fuchsia', 'green', 'maroon', 'orange',
          'pink', 'purple', 'red','yellow', 'violet', 'indigo',
          'chartreuse', 'lime', 'amber', 'electric green', 'cyan']

class Tetris:
    def __init__(self, parent):
        self.parent = parent
        self.board_width = 10
        self.board_height = 24
        self.board = [['' for column in range(self.board_width)]
                      for row in range(self.board_height)]
        self.width = 300
        self.height = 720
        self.square_width = self.width//10
        self.canvas = tk.Canvas(root, height = self.height, width = self.width)
        self.canvas.grid(row=0, column=0)
        self.separator = self.canvas.create_line(0,
                                                 self.height//6,
                                                 self.width,
                                                 self.height//6,
                                                 width = 2)
        self.tickrate = 1000
        self.piece_is_active = False
        self.parent.after(self.tickrate, self.tick)
        self.shapes = {'s':[['*', ''],
                            ['*', '*'],
                            ['', '*']],
                       'z':[['', '*'],
                            ['*', '*'],
                            ['*', '']],
                       'r':[['*', '*'],
                            ['*', ''],
                            ['*', '']],
                       'L':[['*', ''],
                            ['*', ''],
                            ['*', '*']],
                       'o':[['*', '*'],
                            ['*', '*']],
                       'I':[['*'],
                            ['*'],
                            ['*'],
                            ['*']],
                       'T':[['*', '*', '*'],
                            ['', '*', '']]}
        self.parent.bind('<Down>', self.shift)
        self.parent.bind('<Left>', self.shift)
        self.parent.bind('<Right>', self.shift)

    def tick(self):
        if not self.piece_is_active:
            self.spawn()
            self.piece_is_active = not self.piece_is_active

        #self.parent.after(self.tickrate, self.tick)

    def shift(self, event = None):
        if not self.piece_is_active:
            return
        r = self.active_piece['row']
        c = self.active_piece['column']
        l = len(self.active_piece['shape'])
        w = len(self.active_piece['shape'][0])
        direction = (event and event.keysym) or 'Down'
        if direction == 'Down':
            if r + l >= self.board_height:
                self.settle()
                return
            rt = r+1#row, temporary
            ct = c #column, temporary

        elif direction == 'Left':
            if not c:
                return
            rt = r
            ct = c-1
        elif direction == 'Right':
            if c+w >= self.board_width:
                return
            rt = r
            ct = c+1
        for row, squares in zip(range(rt, rt+l), self.active_piece['shape']):
            for column, square in zip(range(ct, ct + w), squares):
                if square and self.board[row][column]:
                    self.settle()
                    return
        if direction == 'Down':
            self.board[r][c:c+w] = ['']*w #blank piece's old top row
            self.active_piece['row'] += 1 #increment piece's row
            r += 1 #increment piece's row
        else:
            if direction == 'Left':
                column = c+w
                self.active_piece['column'] -= 1  # dencrement piece's column
                c -= 1
            elif direction == 'Right':
                column = c-1
                self.active_piece['column'] += 1  # increment piece's column
                c += 1
            if 0 <= column < self.board_width:
                for idx in range(r, r+l): #blank piece's old outer column
                    self.board[idx][column] = ''
        for row, squares in zip(range(r, r+l), self.active_piece['shape']):
            for column, square in zip(range(c, c+w), squares):
                if square:
                    self.board[row][column] = square
        for id, coords_idx in zip(self.active_piece['piece'],
                                  range(len(self.active_piece['coords']))):
            #move visual representation of piece's on canvas
            x1, y1, x2, y2 = self.active_piece['coords'][coords_idx]
            if direction == 'Down':
                y1 += self.square_width
                y2 += self.square_width
            elif direction == 'Left':
                x1 -= self.square_width
                x2 -= self.square_width
            elif direction == 'Right':
                x1 += self.square_width
                x2 += self.square_width
            self.active_piece['coords'][coords_idx] = x1, y1, x2, y2
            self.canvas.coords(id, self.active_piece['coords'][coords_idx])

    def rotate(self):
        pass

    def settle(self):
        self.piece_is_active = not self.piece_is_active
        print('clock')



    def spawn(self):
        shape = self.shapes[random.choice('szrLoIT')]
        shape = ra(shape, random.choice((0, 90, 180, 270)))
        width = len(shape[0])
        start = (10-width)//2
        self.active_piece = {'shape': shape, 'piece': [],
                             'row': 0, 'column': start,
                             'coords': []}
        for y, row in enumerate(shape):
            self.board[y][start:start+width] = shape[y]
            for x, cell in enumerate(row, start = start):
                if cell:
                    self.active_piece['coords'].append((self.square_width * x,
                                                       self.square_width * y,
                                                       self.square_width * (x + 1),
                                                       self.square_width * (y + 1)))
                    self.active_piece['piece'].append(
                        self.canvas.create_rectangle(self.active_piece['coords'][-1]))

        for row in self.board:
            print(row)


    def new(self):
        pass

    def lose(self):
        pass

    def clear(self):
        pass

root = tk.Tk()
root.title('Tetris')
tetris = Tetris(root)
root.mainloop()
