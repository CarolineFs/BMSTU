import tkinter as tk
from ErrorCatcher import catch_float_error
from quadric_equasion import solve_quadric_equasion

# CONST
CANVAS_WIDTH = 225
CANVAS_HEIGHT = 480


def show_result(x1, x2, entry_result):
    print(x1, x2)
    if x2 is not None:
        res = 'x1='+str(x1)+', x2='+str(x2)
        entry_result.delete(0, len(entry_result.get()))
        entry_result.insert(0, res)
    else:
        if x1 is not None:
            if x1 != 'Нет действительных корней':
                res = 'x=' + str(x1)
            else:
                res = 'Нет действительных корней'
        else:
            res = 'Решений нет'
        entry_result.delete(0, len(entry_result.get()))
        entry_result.insert(0, res)


def getter(event, entry_a, entry_b, entry_c, entry_result):
    a = entry_a.get()
    b = entry_b.get()
    c = entry_c.get()
    a = catch_float_error(a)
    b = catch_float_error(b)
    c = catch_float_error(c)
    if (type(a) is float) and \
        (type(b) is float) and \
        (type(c) is float):
        x1, x2 = solve_quadric_equasion(a, b, c)
        show_result(x1, x2, entry_result)
    else:
        entry_result.delete(0, len(entry_result.get()))
        entry_result.insert(0, 'Некорректный ввод')
        if type(a) is not float:
            entry_a.delete(0, len(entry_a.get()))
        if type(b) is not float:
            entry_b.delete(0, len(entry_b.get()))
        if type(c) is not float:
            entry_c.delete(0, len(entry_c.get()))


def getter_menu(entry_a, entry_b, entry_c, entry_result):
    a = entry_a.get()
    b = entry_b.get()
    c = entry_c.get()
    a = catch_float_error(a)
    b = catch_float_error(b)
    c = catch_float_error(c)
    if (type(a) is float) and \
        (type(b) is float) and \
        (type(c) is float):
        x1, x2 = solve_quadric_equasion(a, b, c)
        show_result(x1, x2, entry_result)
    else:
        entry_result.delete(0, len(entry_result.get()))
        entry_result.insert(0, 'Некорректный ввод')
        if type(a) is not float:
            entry_a.delete(0, len(entry_a.get()))
        if type(b) is not float:
            entry_b.delete(0, len(entry_b.get()))
        if type(c) is not float:
            entry_c.delete(0, len(entry_c.get()))


def clear_all(event, entry_a, entry_b, entry_c, entry_result):
    entry_a.delete(0, len(entry_a.get()))
    entry_b.delete(0, len(entry_b.get()))
    entry_c.delete(0, len(entry_c.get()))
    entry_result.delete(0, len(entry_result.get()))


def clear_all_menu(entry_a, entry_b, entry_c, entry_result):
    entry_a.delete(0, len(entry_a.get()))
    entry_b.delete(0, len(entry_b.get()))
    entry_c.delete(0, len(entry_c.get()))
    entry_result.delete(0, len(entry_result.get()))


def clear_result(entry_result):
    entry_result.delete(0, len(entry_result.get()))



def clear_active_entry(event, root, entry_a, entry_b, entry_c, entry_result):
    entry = str(root.focus_displayof())
    if entry.endswith('entry'):
        entry_a.delete(0, len(entry_a.get()))
    elif entry.endswith('entry2'):
        entry_b.delete(0, len(entry_b.get()))
    elif entry.endswith('entry3'):
        entry_c.delete(0, len(entry_c.get()))
    elif entry.endswith('entry4'):
        entry_result.delete(0, len(entry_result.get()))


def insert(event, root, entry_a, entry_b, entry_c, string):
    entry = str(root.focus_displayof())
    if entry.endswith('entry'):
        entry_a.insert(len(entry_a.get()), string)
    elif entry.endswith('entry2'):
        entry_b.insert(len(entry_b.get()), string)
    elif entry.endswith('entry3'):
        entry_c.insert(len(entry_c.get()), string)


def draw_canvas(root):
    '''
    Creates canvas, entries, buttons, drop menu
    :return: Nothing
    '''
    # Create canvas
    canvas = tk.Canvas(root, height=CANVAS_HEIGHT,
                       width=CANVAS_WIDTH,
                       bg='black')
    canvas.grid(row=0, column=0)

    # Create entries
    entry_a = tk.Entry(canvas, width=4, bg='SkyBlue1')
    entry_a.place(x=25, y=10)

    canvas.create_text(80, 10, text='x^2+',
                       font='Verdana 12', fill='white',
                       anchor='n')

    entry_b = tk.Entry(canvas, width=4, bg='SkyBlue1',)
    entry_b.place(x=105, y=10)

    canvas.create_text(150, 10, text='x+',
                       font='Verdana 12', fill='white',
                       anchor='n')

    entry_c = tk.Entry(canvas, width=4, bg='SkyBlue1')
    entry_c.place(x=163, y=10)

    entry_result = tk.Entry(canvas, width=27, bg='SkyBlue1')
    entry_result.place(x=25, y=35)

    # Create buttons
    def handler_sign(event, root=root, entry_a=entry_a,
                entry_b=entry_b, entry_c=entry_c, string='-'):
        return insert(event, root, entry_a, entry_b, entry_c, string)
    button_sign = tk.Button(canvas, text='+/-', fg='white', bg='blue4',
                            font='Verdana 12', width=6, height=3,
                            activebackground='midnight blue',
                            activeforeground='white')
    button_sign.bind('<Button-1>', handler_sign)
    button_sign.place(x=0, y=80)

    def handler_clear_all(event, entry_a=entry_a,
                          entry_b=entry_b, entry_c=entry_c,
                          entry_result=entry_result):
        return clear_all(event, entry_a, entry_b, entry_c, entry_result)
    button_ac = tk.Button(canvas, text='AC', fg='white', bg='turquoise2',
                          font='Verdana 12', width=6, height=3,
                          activebackground='turquoise3',
                          activeforeground='white')
    button_ac.bind('<Button-1>', handler_clear_all)
    button_ac.place(x=75, y=80)

    def handler_clear_active_entry(event, root=root, entry_a=entry_a,
                                   entry_b=entry_b, entry_c=entry_c, entry_result=entry_result):
        return clear_active_entry(event, root, entry_a, entry_b, entry_c, entry_result)
    button_c = tk.Button(canvas, text='C', fg='white', bg='turquoise2',
                         font='Verdana 12', width=6, height=3,
                         activebackground='turquoise3',
                         activeforeground='white')
    button_c.bind('<Button-1>', handler_clear_active_entry)
    button_c.place(x=150, y=80)

    def handler7(event, root=root, entry_a=entry_a,
                entry_b=entry_b, entry_c=entry_c, string='7'):
        return insert(event, root, entry_a, entry_b, entry_c, string)
    button7 = tk.Button(canvas, text='7', fg='white', bg='Deep sky blue',
                        font='Verdana 12', width=6, height=3,
                        activebackground='dodger blue',
                        activeforeground='white')
    button7.bind('<Button-1>', handler7)
    button7.place(x=0, y=160)

    def handler8(event, root=root, entry_a=entry_a,
                entry_b=entry_b, entry_c=entry_c, string='8'):
        return insert(event, root, entry_a, entry_b, entry_c, string)
    button8 = tk.Button(canvas, text='8', fg='white', bg='Deep sky blue',
                        font='Verdana 12', width=6, height=3,
                        activebackground='dodger blue',
                        activeforeground='white')
    button8.bind('<Button-1>', handler8)

    button8.place(x=75, y=160)

    def handler9(event, root=root, entry_a=entry_a,
                entry_b=entry_b, entry_c=entry_c, string='9'):
        return insert(event, root, entry_a, entry_b, entry_c, string)
    button9 = tk.Button(canvas, text='9', fg='white', bg='Deep sky blue',
                        font='Verdana 12', width=6, height=3,
                        activebackground='dodger blue',
                        activeforeground='white')
    button9.bind('<Button-1>', handler9)
    button9.place(x=150, y=160)

    def handler4(event, root=root, entry_a=entry_a,
                entry_b=entry_b, entry_c=entry_c, string='4'):
        return insert(event, root, entry_a, entry_b, entry_c, string)
    button4 = tk.Button(canvas, text='4', fg='white', bg='Deep sky blue',
                        font='Verdana 12', width=6, height=3,
                        activebackground='dodger blue',
                        activeforeground='white')
    button4.bind('<Button-1>', handler4)
    button4.place(x=0, y=240)

    def handler5(event, root=root, entry_a=entry_a,
                entry_b=entry_b, entry_c=entry_c, string='5'):
        return insert(event, root, entry_a, entry_b, entry_c, string)
    button5 = tk.Button(canvas, text='5', fg='white', bg='Deep sky blue',
                        font='Verdana 12', width=6, height=3,
                        activebackground='dodger blue',
                        activeforeground='white')
    button5.bind('<Button-1>', handler5)
    button5.place(x=75, y=240)

    def handler6(event, root=root, entry_a=entry_a,
                entry_b=entry_b, entry_c=entry_c, string='6'):
        return insert(event, root, entry_a, entry_b, entry_c, string)
    button6 = tk.Button(canvas, text='6', fg='white', bg='Deep sky blue',
                        font='Verdana 12', width=6, height=3,
                        activebackground='dodger blue',
                        activeforeground='white')
    button6.bind('<Button-1>', handler6)
    button6.place(x=150, y=240)

    def handler1(event, root=root, entry_a=entry_a,
                entry_b=entry_b, entry_c=entry_c, string='1'):
        return insert(event, root, entry_a, entry_b, entry_c, string)
    button1 = tk.Button(canvas, text='1', fg='white', bg='Deep sky blue',
                        font='Verdana 12', width=6, height=3,
                        activebackground='dodger blue',
                        activeforeground='white')
    button1.bind('<Button-1>', handler1)
    button1.place(x=0, y=320)

    def handler2(event, root=root, entry_a=entry_a,
                entry_b=entry_b, entry_c=entry_c, string='2'):
        return insert(event, root, entry_a, entry_b, entry_c, string)
    button2 = tk.Button(canvas, text='2', fg='white', bg='Deep sky blue',
                        font='Verdana 12', width=6, height=3,
                        activebackground='dodger blue',
                        activeforeground='white')
    button2.bind('<Button-1>', handler2)
    button2.place(x=75, y=320)

    def handler3(event, root=root, entry_a=entry_a,
                entry_b=entry_b, entry_c=entry_c, string='3'):
        return insert(event, root, entry_a, entry_b, entry_c, string)
    button3 = tk.Button(canvas, text='3', fg='white', bg='Deep sky blue',
                        font='Verdana 12', width=6, height=3,
                        activebackground='dodger blue',
                        activeforeground='white')
    button3.bind('<Button-1>', handler3)
    button3.place(x=150, y=320)

    def handler0(event, root=root, entry_a=entry_a,
                entry_b=entry_b, entry_c=entry_c, string='0'):
        return insert(event, root, entry_a, entry_b, entry_c, string)
    button0 = tk.Button(canvas, text='0', fg='white', bg='Deep sky blue',
                        font='Verdana 12', width=6, height=3,
                        activebackground='dodger blue',
                        activeforeground='white')
    button0.bind('<Button-1>', handler0)
    button0.place(x=0, y=400)

    def handler_point(event, root=root, entry_a=entry_a,
                entry_b=entry_b, entry_c=entry_c, string='.'):
        return insert(event, root, entry_a, entry_b, entry_c, string)
    button_point = tk.Button(canvas, text='.', fg='white', bg='blue4',
                             font='Verdana 12', width=6, height=3,
                             activebackground='midnight blue',
                             activeforeground='white')
    button_point.bind('<Button-1>', handler_point)
    button_point.place(x=75, y=400)

    def handler_getter(event, entry_a=entry_a, entry_b=entry_b,
                       entry_c=entry_c, entry_result=entry_result):
        return getter(event, entry_a, entry_b, entry_c, entry_result)
    button_equasion = tk.Button(canvas, text='=', fg='white', bg='turquoise2',
                                font='Verdana 12', width=6, height=3,
                                activebackground='turquoise3',
                                activeforeground='white')
    button_equasion.bind('<Button-1>', handler_getter)
    button_equasion.place(x=150, y=400)

    # Create drop menu
    drop_menu = tk.Menu(root)
    root.configure(menu=drop_menu)

    clear_item = tk.Menu(drop_menu)
    drop_menu.add_cascade(label='Clear', menu=clear_item)

    def handler_clear_all_menu(entry_a=entry_a, entry_b=entry_b,
                               entry_c=entry_c, entry_result=entry_result):
        return clear_all_menu(entry_a, entry_b, entry_c, entry_result)
    clear_item.add_command(label='Clear all', command=handler_clear_all_menu)

    def handler_clear_result(entry_result=entry_result):
        return clear_result(entry_result)
    clear_item.add_command(label='Clear result', command=handler_clear_result)

    repeat_item = tk.Menu(drop_menu)
    drop_menu.add_cascade(label='Repeat', menu=repeat_item)

    def handler_show_result(entry_a=entry_a, entry_b=entry_b,
                            entry_c=entry_c, entry_result=entry_result):
        return getter_menu(entry_a, entry_b, entry_c, entry_result)
    repeat_item.add_command(label='Show result', command=handler_show_result)

    info_item = tk.Menu(drop_menu)
    drop_menu.add_cascade(label='Info', menu=info_item)
    info_item.add_command(label='Program')
    info_item.add_command(label='Authors')





def main():
    root = tk.Tk()
    root.title('Calculator')
    root.resizable(width=False, height=False)

    draw_canvas(root)

    root.mainloop()


main()
