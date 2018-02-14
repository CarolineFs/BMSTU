import tkinter as tk
from quadric_equasion import solve_quadric_equasion

# CONST
# Геометрия
CANVAS_WIDTH = 225
CANVAS_HEIGHT = 480
# Название главного окна 
TITLE = 'Calculator'
# Цвета кнопок
ENTRIES_COLOR = 'SkyBlue1'
NUM_BUTTONS_PASSIVE_COLOR = 'Deep sky blue'
NUM_BUTTONS_ACTIVE_COLOR = 'dodger blue'
SIGNS_ACTIVE_COLOR = 'blue4'
SIGNS_PASSIVE_COLOR = 'midnight blue'
RESULTS_PASSIVE_COLORS = 'turquoise2'
RESULTS_ACTIVE_COLORS = 'turquoise3'
BUTTONS_FG_COLOR = 'white'
BUTTONS_FONT = 'Verdana 12'

# Цвет фона главного окна
CANVAS_BG = 'black'


def info_program(root):
    '''
    Создает новое окно с информацией о программе
    Ничего не возвращает
    '''
    info_win = tk.Toplevel(root, bg=ENTRIES_COLOR)
    info_win.resizable(width = False, height = False)
    text = 'Дата создания программы: 11.02.2018\n' +\
            'Создатель: Овчинникова Анастасия\n' +\
            'Язык программирования: Python\n'
    info_label = tk.Label(info_win,
                          text=text,
                          bg=ENTRIES_COLOR,
                          width=30, height=10,
                          justify='left')
    info_label.grid(row=0, column=0)


def info_authors(root):
    '''
    Создает новое окно с информацией о создателе программы
    Ничего не возвращает
    '''
    info_win = tk.Toplevel(root, bg=ENTRIES_COLOR)
    info_win.resizable(width = False, height = False)
    text = 'Создатель: Овчинникова Анастасия\n' + \
           'Курс: 1\n' + \
           'Группа: ИУ7-25\n' + \
           'ВУЗ: МГТУ им Баумана'
    info_label = tk.Label(info_win,
                          text=text,
                          bg=ENTRIES_COLOR,
                          width=30, height=10,
                          justify='left')
    info_label.grid(row=0, column=0)


def show_result(x1, x2, entry_result):
    '''
    Выводит на экран конри уравнения
    '''
    if x2 is not None:
        x1 = '{:0.4f}'.format(x1)
        x2 = '{:0.4f}'.format(x2)
        res = 'x1='+x1+', x2='+x2
        entry_result.delete(0, len(entry_result.get()))
        entry_result.insert(0, res)
    else:
        if x1 is not None:
            if x1 != 'Нет действительных корней':
                x1 = '{:0.4f}'.format(x1)
                res = 'x=' + x1
            else:
                res = 'Нет действительных корней'
        else:
            res = 'Решений нет'
        entry_result.delete(0, len(entry_result.get()))
        entry_result.insert(0, res)


def getter(entry_a, entry_b, entry_c, entry_result):
    '''
    Собирает введенные пользователем данные,
    и на их основании пытается посчитать корни уравнения.
    В случае успеха вызывает функцию show_result.
    В случае неудачи выводит сообщение об ошибке
    '''
    a = entry_a.get()
    b = entry_b.get()
    c = entry_c.get()
    try:
        a = float(a)
        b = float(b)
        c = float(c)
    except ValueError:
        pass
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


def clear_all(entry_a, entry_b, entry_c, entry_result):
    '''
    Очищает все поля ввода
    '''
    entry_a.delete(0, len(entry_a.get()))
    entry_b.delete(0, len(entry_b.get()))
    entry_c.delete(0, len(entry_c.get()))
    entry_result.delete(0, len(entry_result.get()))


def clear_result(entry_result):
    '''
    Очищает поле, где выводится результат
    '''
    entry_result.delete(0, len(entry_result.get()))


def clear_active_entry(root):
    '''
    Очищает поле ввода, где находится курсор
    '''
    entry = root.focus_displayof()
    entry.delete(0, len(entry.get()))


def insert(root, entry_a, entry_b, entry_c, string):
    '''
    Добавляет в поле ввода новый символ,
    в зависимости от того, какая кнопка на калькуляторе была нажта
    '''
    entry = root.focus_displayof()
    if string == '-':
        text = entry.get()
        if text == '':
            return
        else:
            if text[0] == '-':
                new_text = text[1:]
            else:
                new_text = '-' + text
            entry.delete(0, len(text))
            entry.insert(0, new_text)
    else:
        entry.insert(len(entry.get()), string)
    


def create_button(canvas, text, bg, activebackground, width=6, height=3,
                  fg=BUTTONS_FG_COLOR, font=BUTTONS_FONT, activeforeground=BUTTONS_FG_COLOR):
    '''
    Получает все необходимые характеристики кнопки и создает ее
    '''
    button = tk.Button(canvas, text=text, fg=fg, bg=bg,
                       font=font, width=width, height=height,
                       activebackground=activebackground,
                       activeforeground=activeforeground)
    return button


def draw_canvas(root):
    '''
    Создает холст, поля ввода, кнопки и выпадающее меню
    :return: Nothing
    '''
    # Создаем холст
    canvas = tk.Canvas(root, height=CANVAS_HEIGHT,
                       width=CANVAS_WIDTH,
                       bg=CANVAS_BG)
    canvas.grid(row=0, column=0)

    # Создаем поля ввода 
    entry_a = tk.Entry(canvas, width=4, bg=ENTRIES_COLOR)
    entry_a.place(x=25, y=10)
    entry_a.focus()

    canvas.create_text(80, 10, text='x^2+',
                       font=BUTTONS_FONT, fill=BUTTONS_FG_COLOR,
                       anchor='n')

    entry_b = tk.Entry(canvas, width=4, bg=ENTRIES_COLOR,)
    entry_b.place(x=105, y=10)

    canvas.create_text(150, 10, text='x+',
                       font=BUTTONS_FONT, fill=BUTTONS_FG_COLOR,
                       anchor='n')

    entry_c = tk.Entry(canvas, width=4, bg=ENTRIES_COLOR)
    entry_c.place(x=163, y=10)

    entry_result = tk.Entry(canvas, width=27, bg=ENTRIES_COLOR)
    entry_result.place(x=25, y=35)

    # Создаем кнопки
    button_sign = create_button(canvas, '+/-', SIGNS_ACTIVE_COLOR, SIGNS_PASSIVE_COLOR)
    button_sign.bind('<Button-1>',
                     lambda x: insert(root, entry_a, entry_b, entry_c, string='-'))
    button_sign.place(x=0, y=80)


    button_ac = create_button(canvas, 'AC', RESULTS_PASSIVE_COLORS, RESULTS_ACTIVE_COLORS)
    button_ac.bind('<Button-1>',
                   lambda x: clear_all(entry_a, entry_b,
                                       entry_c, entry_result))
    button_ac.place(x=75, y=80)


    button_c = create_button(canvas, 'C', RESULTS_PASSIVE_COLORS, RESULTS_ACTIVE_COLORS)
    button_c.bind('<Button-1>',
                  lambda x: clear_active_entry(root))
    button_c.place(x=150, y=80)


    button7 = create_button(canvas, '7', NUM_BUTTONS_PASSIVE_COLOR, NUM_BUTTONS_ACTIVE_COLOR)
    button7.bind('<Button-1>',
                 lambda x: insert(root, entry_a, entry_b, entry_c, string='7'))
    button7.place(x=0, y=160)


    button8 = create_button(canvas, '8', NUM_BUTTONS_PASSIVE_COLOR, NUM_BUTTONS_ACTIVE_COLOR)
    button8.bind('<Button-1>',
                 lambda x: insert(root, entry_a, entry_b, entry_c, string='8'))
    button8.place(x=75, y=160)


    button9 = create_button(canvas, '9', NUM_BUTTONS_PASSIVE_COLOR, NUM_BUTTONS_ACTIVE_COLOR)
    button9.bind('<Button-1>',
                 lambda x: insert(root, entry_a, entry_b, entry_c, string='9'))
    button9.place(x=150, y=160)


    button4 = create_button(canvas, '4', NUM_BUTTONS_PASSIVE_COLOR, NUM_BUTTONS_ACTIVE_COLOR)
    button4.bind('<Button-1>',
                 lambda x: insert(root, entry_a, entry_b, entry_c, string='4'))
    button4.place(x=0, y=240)


    button5 = create_button(canvas, '5', NUM_BUTTONS_PASSIVE_COLOR, NUM_BUTTONS_ACTIVE_COLOR)
    button5.bind('<Button-1>',
                 lambda x: insert(root, entry_a, entry_b, entry_c, string='5'))
    button5.place(x=75, y=240)


    button6 = create_button(canvas, '6', NUM_BUTTONS_PASSIVE_COLOR, NUM_BUTTONS_ACTIVE_COLOR)
    button6.bind('<Button-1>',
                 lambda x: insert(root, entry_a, entry_b, entry_c, string='6'))
    button6.place(x=150, y=240)


    button1 = create_button(canvas, '1', NUM_BUTTONS_PASSIVE_COLOR, NUM_BUTTONS_ACTIVE_COLOR)
    button1.bind('<Button-1>',
                 lambda x: insert(root, entry_a, entry_b, entry_c, string='1'))
    button1.place(x=0, y=320)


    button2 = create_button(canvas, '2', NUM_BUTTONS_PASSIVE_COLOR, NUM_BUTTONS_ACTIVE_COLOR)
    button2.bind('<Button-1>',
                 lambda x: insert(root, entry_a, entry_b, entry_c, string='2'))
    button2.place(x=75, y=320)


    button3 = create_button(canvas, '3', NUM_BUTTONS_PASSIVE_COLOR, NUM_BUTTONS_ACTIVE_COLOR)
    button3.bind('<Button-1>',
                 lambda x: insert(root, entry_a, entry_b, entry_c, string='3'))
    button3.place(x=150, y=320)


    button0 = create_button(canvas, '0', NUM_BUTTONS_PASSIVE_COLOR, NUM_BUTTONS_ACTIVE_COLOR)
    button0.bind('<Button-1>',
                 lambda x: insert(root, entry_a, entry_b, entry_c, string='0'))
    button0.place(x=0, y=400)


    button_point = create_button(canvas, '.', SIGNS_ACTIVE_COLOR, SIGNS_PASSIVE_COLOR)
    button_point.bind('<Button-1>',
                      lambda x: insert(root, entry_a, entry_b, entry_c, string='.'))
    button_point.place(x=75, y=400)


    button_equasion = create_button(canvas, '=', RESULTS_PASSIVE_COLORS, RESULTS_ACTIVE_COLORS)
    button_equasion.bind('<Button-1>',
                         lambda x: getter(entry_a, entry_b, entry_c, entry_result))
    button_equasion.place(x=150, y=400)

    # Создаем выпадающее меню
    drop_menu = tk.Menu(root)
    root.configure(menu=drop_menu)

    clear_item = tk.Menu(drop_menu)
    drop_menu.add_cascade(label='Clear', menu=clear_item)


    clear_item.add_command(label='Clear all',
                           command=lambda: clear_all(entry_a, entry_b,
                                                     entry_c, entry_result))
    clear_item.add_command(label='Clear result',
                           command=lambda: clear_result(entry_result))


    repeat_item = tk.Menu(drop_menu)
    drop_menu.add_cascade(label='Repeat', menu=repeat_item)
    repeat_item.add_command(label='Show result',
                            command=lambda: getter(entry_a, entry_b,
                                                   entry_c, entry_result))

    info_item = tk.Menu(drop_menu)
    drop_menu.add_cascade(label='Info', menu=info_item)
    info_item.add_command(label='Program', command=lambda: info_program(root))
    info_item.add_command(label='Authors', command=lambda: info_authors(root))


def main():
    root = tk.Tk()
    root.title(TITLE)
    root.resizable(width=False, height=False)

    draw_canvas(root)

    root.mainloop()


main()
