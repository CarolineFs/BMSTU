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
    def get_item(self, obj):
        pass

    @abstractmethod
    def remove_item(self):
        pass

    @abstractmethod
    def move_item(self):
        pass

    @abstractmethod
    def clear_all(self):
        pass


class GridLayout(Layout):
    def __init__(self, start_pos, size, parent, col, row):
        Layout.__init__(self, start_pos, size, parent)
        self.mRow = row
        self.mCol = col

    def set_item(self, col, row, obj):
        pass

    def get_item(self, obj):
        pass

    def remove_item(self):
        pass

    def move_item(self):
        pass

    def resize_grid(self):
        pass

    def clear_all(self):
        pass

    def remove_grid(self):
        pass


class PlaceLayout(Layout):
    def __init__(self, start_pos, size, parent):
        Layout.__init__(self, start_pos, size, parent)

    def set_item(self, x, y, obj):
        pass

    def get_item(self, obj):
        pass

    def remove_item(self):
        pass

    def move_item(self):
        pass

    def clear_all(self):
        pass


class VerticalLayout(GridLayout):
    def __init__(self, start_pos, size, col, parent):
        GridLayout.__init__(self, start_pos, size, parent, col=col, row=0)
        self.mCol = col

    def set_item(self):
        pass

    def get_item(self):
        pass

    def remove_item(self):
        pass

    def move_item(self):
        pass

    def clear_all(self):
        pass


class HorizontalLayout(GridLayout):
    def __init__(self, start_pos, size, row, parent):
        GridLayout.__init__(self, start_pos, size, parent, row=row, col=0)
        self.mRow = row

    def set_item(self):
        pass

    def get_item(self):
        pass

    def remove_item(self):
        pass

    def move_item(self):
        pass

    def clear_all(self):
        pass

