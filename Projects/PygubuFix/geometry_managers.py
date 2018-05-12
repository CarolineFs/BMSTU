import tkinter as tk
from abc import ABCMeta, abstractmethod


class Layout:
    __metaclass__ = ABCMeta

    def __init__(self, start_pos, size, parent):
        ''' Фреймы размещаются только по коордиатам '''
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
    def move_item(self, new_x, new_y, obj):
        pass

    @abstractmethod
    def clear_all(self):
        pass

    @abstractmethod
    def change_layout_parent(self, new_parent):
        pass

    @abstractmethod
    def move_layout(self, new_pos1, new_pos2):
        pass


class GridLayout(Layout):
    ''' Все методы возвращают None в случае ошибки '''
    def __init__(self, start_pos, size, parent, col, row):
        Layout.__init__(self, start_pos, size, parent)
        self.mRow = row
        self.mCol = col

    def set_item(self, row, col, obj):
        try:
            obj.grid(row=row, column=col)
        except AttributeError:
            return None

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
        try:
            obj.grid_forget()
            return obj
        except AttributeError:
            return None

    def move_item(self, new_row, new_col, obj):
        try:
            obj.grid_forget()
            obj.grid(row=new_row, col=new_col)
        except AttributeError:
            return None

    def clear_all(self):
        forgot_items = []
        try:
            for item in self.frame.grid_slaves():
                item.grid_forget()
                forgot_items.append(item)
        except AttributeError:
            return None
        return forgot_items

    def change_layout_parent(self, new_parent):
        self.mParent = new_parent

    def move_layout(self, new_x, new_y):
        self.mStartPos[0] = new_x
        self.mStartPos[1] = new_y


class PlaceLayout(Layout):
    def __init__(self, start_pos, size, parent):
        Layout.__init__(self, start_pos, size, parent)

    def set_item(self, x, y, obj):
        try:
            obj.place(x=x, y=y)
        except AttributeError:
            return None

    def get_item_by_position(self, x, y):
        ''' Возвращает объект на искомой позиции либо None '''
        try:
            for item in self.frame.place_slaves():
                info = item.place_info()
                if info['x'] == x and info['y'] == y:
                    return item
        finally:
            return None

    def get_item_position(self, obj):
        ''' Возвращает позицию объекта в виде (ряд, столбец) либо None'''
        try:
            info = obj.place_info()
        except AttributeError:
            return None
        else:
            position = (info['x'], info['y'])
            if len(info) == 0:
                return None
        return position

    def remove_item(self, obj):
        try:
            obj.place_forget()
            return obj
        except AttributeError:
            return None

    def move_item(self, new_x, new_y, obj):
        try:
            obj.place_forget()
            obj.grid(row=new_x, col=new_y)
        except AttributeError:
            return None

    def clear_all(self):
        forgot_items = []
        try:
            for item in self.frame.place_slaves():
                item.place_forget()
                forgot_items.append(item)
        except AttributeError:
            return None
        return forgot_items

    def change_layout_parent(self, new_parent):
        self.mParent = new_parent

    def move_layout(self, new_x, new_y):
        self.mStartPos[0] = new_x
        self.mStartPos[1] = new_y


class VerticalLayout(GridLayout):
    def __init__(self, start_pos, size, row, parent):
        GridLayout.__init__(self, start_pos, size, parent, col=0, row=row)

    def set_item(self, row, obj, col=0):
        obj.grid(row=row, column=col)


class HorizontalLayout(GridLayout):
    def __init__(self, start_pos, size, col, parent):
        GridLayout.__init__(self, start_pos, size, parent, row=0, col=col)
        self.mCol = col

    def set_item(self, row, col, obj):
        obj.grid(row=row, column=col)
