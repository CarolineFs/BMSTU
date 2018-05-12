import tkinter as tk
from abc import ABCMeta, abstractmethod


class Layout:
    __metaclass__ = ABCMeta

    def __init__(self, start_pos, size, parent):
        self.mStartPos = start_pos
        self.mSize = size
        self.mParent = parent

        self.frame = tk.Frame(self.mParent,
                              height=self.mSize[1],
                              width=self.mSize[0])

        self.frame.place(x=self.mStartPos[0],
                         y=self.mStartPos[1])

    @abstractmethod
    def set_item(self, pos1, pos2, obj):
        pass

    @abstractmethod
    def get_item_by_position(self, pos1, pos2):
        pass

    @abstractmethod
    def get_item_position(self, obj):
        pass

    @abstractmethod
    def remove_item(self, obj):
        pass

    @abstractmethod
    def move_item(self, pos1, pos2, obj):
        pass

    @abstractmethod
    def clear_all(self):
        pass

    @abstractmethod
    def change_parent(self):
        pass


class GridLayout(Layout):
    def __init__(self, start_pos, size, parent, col, row):
        Layout.__init__(self, start_pos, size, parent)
        self.mRow = row
        self.mCol = col

    def set_item(self, row, col, obj):
        obj.grid(row=row, column=col)

    def get_item_by_position(self, row, col):
        ''' Возвращает объект на искомой позиции либо None '''
        for item in self.frame.grid_slaves():
            info = item.grid_info()
            if info['row'] == row and info['column'] == col:
                return item
        return None

    def get_item_position(self, obj):
        ''' Возвращает позицию объекта в виде (ряд, столбец) либо None'''
        try:
            info = obj.grid_info()
        except AttributeError:
            return None
        else:
            position = (info['row'], info['column'])
            if len(info) == 0:
                return None
        return position

    def remove_item(self, obj):
        obj.grid_forget()
        return obj

    def move_item(self, row, col, obj):
        pass

    def resize_grid(self):
        pass

    def clear_all(self):
        pass

    def remove_grid(self):
        pass

    def change_parent(self):
        pass


class PlaceLayout(Layout):
    def __init__(self, start_pos, size, parent):
        Layout.__init__(self, start_pos, size, parent)

    def set_item(self, x, y, obj):
        obj.place(x=x, y=y)

    def get_item_by_position(self, x, y):
        pass

    def get_item_position(self, obj):
        pass

    def remove_item(self, obj):
        pass

    def move_item(self, x, y, obj):
        pass

    def clear_all(self):
        pass

    def change_parent(self):
        pass


class VerticalLayout(GridLayout):
    def __init__(self, start_pos, size, row, parent):
        GridLayout.__init__(self, start_pos, size, parent, col=0, row=row)
        self.mRow = row

    def set_item(self, row, col, obj):
        obj.grid(row=row, column=col)

    def get_item_by_position(self, row, col=0):
        pass

    def get_item_position(self, obj):
        info = obj.grid_info()
        position = (info['row'], info['column'])
        return position

    def remove_item(self, obj):
        obj.grid_forget()
        return obj

    def move_item(self, row, col, obj):
        pass

    def clear_all(self):
        pass

    def change_parent(self):
        pass


class HorizontalLayout(GridLayout):
    def __init__(self, start_pos, size, col, parent):
        GridLayout.__init__(self, start_pos, size, parent, row=0, col=col)
        self.mCol = col

    def set_item(self, row, col, obj):
        obj.grid(row=row, column=col)

    def get_item_by_position(self, col, row=0):
        pass

    def get_item_position(self, obj):
        info = obj.grid_info()
        position = (info['row'], info['column'])
        return position

    def remove_item(self, obj):
        obj.grid_forget()
        return obj

    def move_item(self, row, col, obj):
        pass

    def clear_all(self):
        pass

    def change_parent(self):
        pass


root = tk.Tk()
t = tk.Frame(root)
t.grid(row=0, column=0)
b = tk.Button(t, text='rrr')
b.grid(row=0, column=0)

b2 = tk.Button(t, text='zzz')
b2.grid(row=1, column=1)

b3 = tk.Button(root, text='xxx')
b3.place(x=0,y=0)
a = 9
r = a.grid_info()
print(r)


