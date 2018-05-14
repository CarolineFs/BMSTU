import tkinter as tk
from abc import ABCMeta, abstractmethod




class Layout:
    __metaclass__ = ABCMeta

    def __init__(self, x, y, height, width, parent, bd=0,
                 bg='SystemButtonFace', colormap='', container=0, cursor='',
                 highlightbackground='SystemButtonFace', highlightcolor='SystemButtonFace',
                 highlightthickness=0, relief='flat', takefocus=0, visual='', relx='0', rely=0,
                 relwidth='', relheight='', anchor='nw', bordermode='inside'):
        """ Фреймы размещаются только по координатам """
        self.mX = x
        self.mY = y
        self.mParent = parent
        self.mBd = bd
        self.mBg = bg
        self.mColormap = colormap
        self.mContainer = container
        self.mCursor = cursor
        self.mHeight = height
        self.mHighlightbackground = highlightbackground
        self.mHighlightcolor = highlightcolor
        self.mHighlightthickness = highlightthickness
        self.mRelief = relief
        self.mTakefocus = takefocus
        self.mVisual = visual
        self.mWidth = width
        self.mRelx = relx
        self.mRely = rely
        self.mRelwidth = relwidth
        self.mRelheight = relheight
        self.mAnchor = anchor
        self.mBordermode = bordermode
        self.frame = tk.Frame(self.mParent, bd=self.mBd, bg=self.mBg, colormap=self.mColormap,
                              container=self.mContainer, cursor=self.mCursor, height=self.mHeight,
                              highlightbackground=self.mHighlightbackground, highlightcolor=self.mHighlightcolor,
                              highlightthickness=self.mHighlightthickness, relief=self.mRelief,
                              takefocus=self.mTakefocus, visual=self.mVisual, width=self.mWidth)
        self.frame.place(x=self.mX, y=self.mY, relx=self.mRelx, rely=self.mRely, width=self.mWidth,
                         height=self.mHeight, relwidth=self.mRelwidth, relheight=self.mRelheight,
                         anchor=self.mAnchor, bordermode=self.mBordermode)
        self.frame.grid_propagate(False)

    @abstractmethod
    def set_item(self, pos1, pos2, obj):
        pass

    @abstractmethod
    def remove_item(self, obj):
        pass

    @abstractmethod
    def clear_all(self):
        pass

    def update_layout_properties(self):
        self.frame['bd'] = self.mBd
        self.frame['bg'] = self.mBg
        self.frame['colormap'] = self.mColormap
        self.frame['container'] = self.mContainer
        self.frame['cursor'] = self.mCursor
        self.frame['height'] = self.mHeight
        self.frame['highlightbackground'] = self.mHighlightbackground
        self.frame['highlightcolor'] = self.mHighlightcolor
        self.frame['highlightthickness'] = self.mHighlightthickness
        self.frame['relief'] = self.mRelief
        self.frame['takefocus'] = self.mTakefocus
        self.frame['visual'] = self.mVisual
        self.frame['width'] = self.mWidth

    def get_layout_properties(self):
        info = dict()
        info['bd'] = self.mBd
        info['bg'] = self.mBg
        info['colormap'] = self.mColormap
        info['container'] = self.mContainer
        info['cursor'] = self.mCursor
        info['height'] = self.mHeight
        info['highlightbackground'] = self.mHighlightbackground
        info['highlightcolor'] = self.mHighlightcolor
        info['highlightthickness'] = self.mHighlightthickness
        info['relief'] = self.mRelief
        info['takefocus'] = self.mTakefocus
        info['visual'] = self.mVisual
        info['width'] = self.mWidth
        return info

    def get_layout_place_properties(self):
        return self.frame.place_info()

    def destroy_layout(self):
        self.frame.destroy()


class GridLayout(Layout):
    """ Все методы возвращают None в случае ошибки """
    def __init__(self, x, y, height, width, parent, bd=0, bg='SystemButtonFace', colormap='',
                 container=0, cursor='', highlightbackground='SystemButtonFace',
                 highlightcolor='SystemButtonFace', highlightthickness=0, relief='flat',
                 takefocus=0, visual='', relx='0', rely=0, relwidth='', relheight='',
                 anchor='nw', bordermode='inside'):
        Layout.__init__(self, x=x, y=y, height=height, width=width, parent=parent,
                        bd=bd, bg=bg, colormap=colormap, container=container, cursor=cursor,
                        highlightbackground=highlightbackground, highlightcolor=highlightcolor,
                        highlightthickness=highlightthickness, relief=relief, takefocus=takefocus,
                        visual=visual, relx=relx, rely=rely, relwidth=relwidth,
                        relheight=relheight, anchor=anchor, bordermode=bordermode)

    def set_item(self, row, col, obj, columnspan=1, rowspan=1, ipadx=0, ipady=0,
                 padx=0, pady=0, sticky=''):

        try:
            obj.grid(row=row, column=col, columnspan=columnspan, rowspan=rowspan,
                     ipadx=ipadx, ipady=ipady, padx=padx, pady=pady, sticky=sticky)
        except AttributeError:
            return None

    def get_item_by_position(self, row, col):
        """ Возвращает объект на искомой позиции либо None """
        for item in self.frame.grid_slaves():
            info = item.grid_info()
            if info['row'] == row and info['column'] == col:
                return item
        return None

    @staticmethod
    def get_item_grid_properties(obj):
        """ Возвращает словарь grid-свойств объекта либо None"""
        try:
            info = obj.grid_info()
        except AttributeError:
            return None
        else:
            if len(info) == 0:
                return None
        return info

    @staticmethod
    def get_item_properties(obj):
        """ Возвращает словарь свойств либо None """
        info = dict(obj)
        return info

    def remove_item(self, obj):
        try:
            obj.grid_forget()
            return obj
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

    def get_slaves(self):
        return self.frame.grid_slaves()


class PlaceLayout(Layout):
    def __init__(self, x, y, height, width, parent, bd=0, bg='SystemButtonFace', colormap='',
                 container=0, cursor='', highlightbackground='SystemButtonFace',
                 highlightcolor='SystemButtonFace', highlightthickness=0, relief='flat',
                 takefocus=0, visual='', relx='0', rely=0, relwidth='', relheight='',
                 anchor='nw', bordermode='inside'):
        Layout.__init__(self, x=x, y=y, height=height, width=width, parent=parent,
                        bd=bd, bg=bg, colormap=colormap, container=container, cursor=cursor,
                        highlightbackground=highlightbackground, highlightcolor=highlightcolor,
                        highlightthickness=highlightthickness, relief=relief, takefocus=takefocus,
                        visual=visual, relx=relx, rely=rely, relwidth=relwidth,
                        relheight=relheight, anchor=anchor, bordermode=bordermode)

    def set_item(self, obj, x=0, y=0,  relx=0, rely=0,
                 width='', height='', relheight='', relwidth='',
                 anchor='nw', bordermode='inside'):
        try:
            obj.place(x=x, y=y, relx=relx, rely=rely, width=width,
                      height=height, relheight=relheight, relwidth=relwidth,
                      anchor=anchor, bordermode=bordermode)
        except AttributeError:
            return None

    def get_item_by_position(self, x, y, anchor, relx=0, rely=0):
        """ Возвращает объект на искомой позиции либо None """
        try:
            for item in self.frame.place_slaves():
                info = item.place_info()
                if info['x'] == x and \
                   info['y'] == y and\
                   info['anchor'] == anchor and\
                   info['relx'] == relx and\
                   info['rely'] == rely:
                    return item
        finally:
            return None

    @staticmethod
    def get_item_properties(obj):
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

    def clear_all(self):
        forgot_items = []
        try:
            for item in self.frame.place_slaves():
                item.place_forget()
                forgot_items.append(item)
        except AttributeError:
            return None
        return forgot_items

    def get_slaves(self):
        return self.frame.place_slaves()

    @staticmethod
    def get_item_place_properties(obj):
        """ Возвращает словарь grid-свойств объекта либо None"""
        try:
            info = obj.place_info()
        except AttributeError:
            return None
        else:
            if len(info) == 0:
                return None
        return info


class VerticalLayout(GridLayout):
    def __init__(self, x, y, height, width, parent, bd=0, bg='SystemButtonFace', colormap='',
                 container=0, cursor='', highlightbackground='SystemButtonFace',
                 highlightcolor='SystemButtonFace', highlightthickness=0, relief='flat',
                 takefocus=0, visual='', relx='0', rely=0, relwidth='', relheight='',
                 anchor='nw', bordermode='inside'):
        GridLayout.__init__(self, x, y, height, width, parent, bd=bd, bg=bg, colormap=colormap,
                            container=container, cursor=cursor, highlightbackground=highlightbackground,
                            highlightcolor=highlightcolor, highlightthickness=highlightthickness,
                            relief=relief, takefocus=takefocus, visual=visual, relx=relx, rely=rely,
                            relwidth=relwidth, relheight=relheight, anchor=anchor, bordermode=bordermode)

    def set_item(self, row, obj, columnspan=1, rowspan=1, ipadx=0, ipady=0,
                 padx=0, pady=0, sticky='', col=0):
        obj.grid(row=row, column=0, columnspan=columnspan, rowspan=rowspan,
                 ipadx=ipadx, ipady=ipady, padx=padx, pady=pady, sticky=sticky)


class HorizontalLayout(GridLayout):
    def __init__(self, x, y, height, width, parent, bd=0, bg='SystemButtonFace', colormap='',
                 container=0, cursor='', highlightbackground='SystemButtonFace',
                 highlightcolor='SystemButtonFace', highlightthickness=0, relief='flat',
                 takefocus=0, visual='', relx='0', rely=0, relwidth='', relheight='',
                 anchor='nw', bordermode='inside'):
        GridLayout.__init__(self, x, y, height, width, parent, bd=bd, bg=bg, colormap=colormap,
                            container=container, cursor=cursor, highlightbackground=highlightbackground,
                            highlightcolor=highlightcolor, highlightthickness=highlightthickness,
                            relief=relief, takefocus=takefocus, visual=visual, relx=relx, rely=rely,
                            relwidth=relwidth, relheight=relheight, anchor=anchor, bordermode=bordermode)

    def set_item(self, col, obj, columnspan=1, rowspan=1, ipadx=0, ipady=0,
                 padx=0, pady=0, sticky='', row=0):
        obj.grid(row=0, column=col, columnspan=columnspan, rowspan=rowspan,
                 ipadx=ipadx, ipady=ipady, padx=padx, pady=pady, sticky=sticky)
