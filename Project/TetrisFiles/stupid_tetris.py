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

class Shape:
    def __init__(self, shape, piece, row, column, coords):
        self.shape = shape
        self.piece = piece
        self.row = row
        self.column = column
        self.coords = coords

class Tetris:
    def __init__(self, parent):
        self.parent = parent
        parent.title('Tetris')
        self.board_width = 10
        self.board_height = 24
        self.board = [['' for column in range(self.board_width)]
                      for row in range(self.board_height)]
        self.field = [[None for column in range(self.board_width)]
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
        self.colors = {'s': 'green',
                       'z': 'yellow',
                       'r': 'turquoise',
                       'L': 'orange',
                       'o': 'blue',
                       'I': 'red',
                       'T': 'violet'}
        self.parent.bind('<Down>', self.shift)
        self.parent.bind('<Left>', self.shift)
        self.parent.bind('<Right>', self.shift)
        self.parent.bind('<Up>', self.rotate)
        self.parent.bind('w', self.rotate)
        self.parent.bind('W', self.rotate)
        self.parent.bind('a', self.shift)
        self.parent.bind('A', self.shift)
        self.parent.bind('s', self.shift)
        self.parent.bind('S', self.shift)
        self.parent.bind('d', self.shift)
        self.parent.bind('D', self.shift)
        self.parent.bind('q', self.rotate)
        self.parent.bind('Q', self.rotate)
        self.parent.bind('e', self.rotate)
        self.parent.bind('E', self.rotate)
        self.parent.bind('0', self.rotate)
        self.parent.bind('<space>', self.snap)

    def print_board(self):
        for row in self.board:
            print(*(cell or ' ' for cell in row), sep='')

    def check_and_move(self, shape,  r, c, l, w):
        # this method checks whether a piece can exist in the given place
        # if it can the method does everything to move it there

        # can we move it?
        for row, squares in zip(range(r, r+l), shape):
            for column, square in zip(range(c, c + w), squares):
                if (row not in range(self.board_height)
                    or
                    column not in range(self.board_width)
                    or
                    (square and self.board[row][column] == 'x')):
                    return

        square_idxs = iter(range(4))  # iterator of 4 indices

        # remove shape from board
        for row in self.board:
            row[:] = ['' if cell == '*' else cell for cell in row]
        # put shape onto board and piece onto canvas
        for row, squares in zip(range(r, r+l),shape):
            for column, square in zip(range(c, c+w), squares):
                if square:
                    self.board[row][column] = square
                    square_idx = next(square_idxs)
                    coord = (column*self.square_width,
                             row*self.square_width,
                             (column+1)*self.square_width,
                             (row+1)*self.square_width)
                    self.active_piece.coords[square_idx] = coord
                    self.canvas.coords(self.active_piece.piece[square_idx], coord)
        self.active_piece.row = r
        self.active_piece.column = c
        self.active_piece.shape = shape
        self.print_board()
        return True


    def rotate(self, event=None):
        if not self.piece_is_active:
            return
        if len(self.active_piece.shape) == len(self.active_piece.shape[0]):  # it's a square
            return  # we do not rotate squares
        r = self.active_piece.row
        c = self.active_piece.column
        l = len(self.active_piece.shape)
        w = len(self.active_piece.shape[0])
        x = c + w//2  # center column for old shape
        y = r + l//2  # center row for new shape
        direction = event.keysym
        if direction in {'q', 'Q'}:
            shape = ra(self.active_piece.shape, -90)
            rotation_index = (self.active_piece.rotation_index - 1) % 4
            rx, ry = self.active_piece.rotation[rotation_index]
            rotation_offsets = -rx, -ry
        elif direction in {'e', 'E', '0', 'Up', 'w', 'W'}:
            shape = ra(self.active_piece.shape, 90)
            rotation_index = self.active_piece.rotation_index
            rotation_offsets = self.active_piece.rotation[rotation_index]
            rotation_index = (rotation_index + 1) % 4

        l = len(shape)  # length of new shape
        w = len(shape[0])  # width of new shape
        rt = y - l//2  # row of new shape
        ct = x - w//2  # column of new shape
        x_correction, y_correction = rotation_offsets
        rt += y_correction
        ct += x_correction

        success = self.check_and_move(shape, rt, ct, l, w)
        if not success:
            return

        self.active_piece.rotation_index = rotation_index


    def tick(self):
        if not self.piece_is_active:
            self.spawn()
        #self.parent.after(self.tickrate, self.tick)

    def shift(self, event = None):
        down = {'Down', 's', 'S'}
        left = {'Left', 'a', 'A'}
        right = {'Right', 'd', 'D'}
        if not self.piece_is_active:
            return
        r = self.active_piece.row
        c = self.active_piece.column
        l = len(self.active_piece.shape)
        w = len(self.active_piece.shape[0])
        direction = (event and event.keysym) or 'Down'
        if direction  in down:
            rt = r+1  # row, temporary
            ct = c  # column, temporary
        elif direction in left:
            rt = r
            ct = c-1
        elif direction in right:
            rt = r
            ct = c+1

        success = self.check_and_move(self.active_piece.shape, rt, ct, l, w)

        if direction in down and not success:
            self.settle()


    def settle(self):
        self.piece_is_active = False
        print('clock')
        for row in self.board:
            row[:] = ['x' if cell == '*' else cell for cell in row]
        for (x1, y1, x2, y2), id in zip(self.active_piece.coords, self.active_piece.piece):
            self.field[y1//self.square_width][x1//self.square_width] = id

        # do we need to clear anything?
        indices = [idx for idx, row in enumerate(self.board) if all(row)]
        if indices:
            self.clear(indices)
        if any(any(row) for row in self.board[:4]):
            self.lose()
            return
        self.parent.after(self.tickrate, self.spawn())


    def spawn(self):
        self.piece_is_active = True
        key = random.choice('szrLoIT')
        shape = self.shapes[key]
        shape = ra(shape, random.choice((0, 90, 180, 270)))
        width = len(shape[0])
        start = (10-width)//2
        self.active_piece = Shape(shape, [], 0, start, [])
        for y, row in enumerate(shape):
            self.board[y][start:start+width] = shape[y]
            for x, cell in enumerate(row, start = start):
                if cell:
                    self.active_piece.coords.append((self.square_width * x,
                                                       self.square_width * y,
                                                       self.square_width * (x + 1),
                                                       self.square_width * (y + 1)))
                    self.active_piece.piece.append(
                        self.canvas.create_rectangle(self.active_piece.coords[-1],
                                                     fill=self.colors[key],
                                                     outline='black',
                                                     #outline='dark'+self.colors[key],
                                                     width=3))

        self.active_piece.rotation_index = 0
        if 3 in (len(shape), len(shape[0])):
            self.active_piece.rotation = [(0, 0),
                                            (1, 0),
                                            (-1,1),
                                            (0,-1)
                                           ]
        else:
            self.active_piece.rotation = [(1, -1),
                                            (0, 1),
                                            (0, 0),
                                            (-1, 0)
                                           ]

        if len(shape) < len(shape[0]):  # wide shape
            self.active_piece.rotation_index = 1

        self.print_board()


    def new(self):
        pass

    def lose(self):
        pass

    def snap(self, event=None):
        for i in range(24):
            self.shift()
        # does not work too great

    def clear(self, indices):
        for idx in indices:
            self.board.pop(idx)
            self.board.insert(0, ['' for column in range(self.board_width)])
        self.clear_iter(indices)

    def clear_iter(self, indices, current_column=0):
        for row in indices:
            if row % 2:
                cc = current_column
            else:
                cc = self.board_width - current_column - 1
            id = self.field[row][cc]
            self.field[row][cc] = None
            self.canvas.delete(id)
        if current_column < self.board_width-1:
            self.parent.after(50, self.clear_iter, indices, current_column+1)
        else:
            for idx, row in enumerate(self.field):
                offset = sum(r > idx for r in indices)*self.square_width
                for square in row:
                    if square:
                        self.canvas.move(square, 0, offset)
            for row in indices:
                self.field.pop(row)
                self.field.insert(0, [None for x in range(self.board_width)])




root = tk.Tk()
root.title('Tetris')
tetris = Tetris(root)
root.mainloop()



