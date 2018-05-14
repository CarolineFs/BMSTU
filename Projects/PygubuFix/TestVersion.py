import tkinter as tk
from abc import ABCMeta, abstractmethod


class Layout:
    __metaclass__ = ABCMeta

    def __init__(self, start_pos, size, parent, background, bd, bg, borderwidth, 
                       colormap, container, cursor, height, highlightbackground,
                       highlightcolor, highlightthickness, relief, takefocus, visual, width):
        """ Фреймы размещаются только по координатам """
        self.mStartPos = start_pos
        self.mSize = size
        self.mParent = parent

        self.frame = tk.Frame(self.mParent,
                              bg='red')

    @abstractmethod
    def set_item(self, pos1, pos2, obj):
        pass

    @abstractmethod
    def get_item_by_position(self, pos1, pos2):
        pass

    @abstractmethod
    def get_item_properties(self, obj):
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

    @abstractmethod
    def get_layout_properties(self):
        return self.frame.place_info()


class GridLayout(Layout):
    ''' Все методы возвращают None в случае ошибки '''
    def __init__(self, start_pos, size, parent):
        Layout.__init__(self, start_pos, size, parent)

    def set_item(self, row, col, obj, columnspan=1, rowspan=1, ipadx=0, ipady=0,
                 padx=0, pady=0, sticky=''):
        try:
            obj.grid(row=row, column=col, columnspan=columnspan, rowspan=rowspan,
                     ipadx=ipadx, ipady=ipady, padx=padx, pady=pady, sticky=sticky)
        except AttributeError:
            return None

    def get_item_by_position(self, row, col):
        ''' Возвращает объект на искомой позиции либо None '''
        for item in self.frame.grid_slaves():
            info = item.grid_info()
            if info['row'] == row and info['column'] == col:
                return item
        return None

    def get_item_properties(self, obj):
        ''' Возвращает позицию объекта в виде (ряд, столбец) либо None'''
        try:
            info = obj.grid_info()
        except AttributeError:
            return None
        else:
            if len(info) == 0:
                return None
        return info

    def remove_item(self, obj):
        try:
            obj.grid_forget()
            return obj
        except AttributeError:
            return None

    def move_item(self, new_row, new_col, obj, columnspan=1, rowspan=1, ipadx=0, ipady=0,
                  padx=0, pady=0, sticky=''):
        try:
            obj.grid_forget()
            obj.grid(row=new_row, column=new_col, columnspan=columnspan, rowspan=rowspan,
                     ipadx=ipadx, ipady=ipady, padx=padx, pady=pady, sticky=sticky)
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
        self.mParent=new_parent

    def move_layout(self, new_pos1, new_pos2):
        super().move_layout(new_pos1, new_pos2)

    def get_layout_properties(self):
        return super().get_layout_properties()

    def get_slaves(self):
        return self.frame.grid_slaves()


class PlaceLayout(Layout):
    def __init__(self, start_pos, size, parent):
        Layout.__init__(self, start_pos, size, parent)

    def set_item(self, obj, x=0, y=0,  relx=0, rely=0,
                 width='', height='', relheight='', relwidth='',
                 anchor='nw', bordermode='inside'):
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

    def get_item_properties(self, obj):
        ''' Возвращает позицию объекта в виде (ряд, столбец) либо None'''
        try:
            info = obj.place_info()
        except AttributeError:
            return None
        else:
            if len(info) == 0:
                return None
        return info

    def remove_item(self, obj):
        try:
            obj.place_forget()
            return obj
        except AttributeError:
            return None

    def move_item(self, obj, new_x=0, new_y=0,  new_relx=0, new_rely=0,
                  new_width='', new_height='', new_relheight='', new_relwidth='',
                  new_anchor='nw', new_bordermode='inside'):
        try:
            obj.place_forget()
            obj.place(x=new_x, y=new_y)
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




class VerticalLayout(GridLayout):
    def __init__(self, start_pos, size, row, parent):
        GridLayout.__init__(self, start_pos, size, parent)

    def setItem(self, row, col, obj, columnspan=1, rowspan=1, ipadx=0, ipady=0,
                 padx=0, pady=0, sticky=''):
        obj.grid(row=row, column=col, columnspan=columnspan, rowspan=rowspan,
                     ipadx=ipadx, ipady=ipady, padx=padx, pady=pady, sticky=sticky)


class HorizontalLayout(GridLayout):
    def __init__(self, start_pos, size, col, parent):
        GridLayout.__init__(self, start_pos, size, parent)
        self.mCol = col

    def setItem(self, row, col, obj, columnspan=1, rowspan=1, ipadx=0, ipady=0,
                 padx=0, pady=0, sticky=''):
        obj.grid(row=row, column=col, columnspan=columnspan, rowspan=rowspan,
                     ipadx=ipadx, ipady=ipady, padx=padx, pady=pady, sticky=sticky)


root = tk.Tk()
l1 = tk.Frame(root, bg='red', width=100, height=100)
l1.place(x=100, y=100)
print(l1.cget('width'))


def f(event):
    l1['bg'] = 'yellow'
    l1.place(x=300, y=300)
    print(l1.grid_slaves())
    print(l1.cget('width'))
    print(l1.cget('bg'))

l1.grid_propagate(False)

b = tk.Button(text='push')
b.bind('<Button-1>', f)
b.place(x=0, y=0)
b2 = tk.Button(l1, text='2')
b2.grid(row=0, column=1)

b3 = tk.Button(l1, text='3')
b3.grid(row=2, column=3)

print(l1.cget('width'))
print(l1.cget('bg'))

print(l1.grid_slaves())

root.mainloop()
