import tkinter as tk

#CONST
CANVAS_WIDTH = 225
CANVAS_HEIGHT = 480


def create_buttons(canvas):
    '''
    Creates buttons
    :return: Nothing
    '''
    button_sign = tk.Button(canvas, text='+/-', fg='white', bg='blue4',
                            font='Verdana 12', width=6, height=3,
                            activebackground='midnight blue',
                            activeforeground='white')
    button_sign.bind('<Button-1>')
    button_sign.place(x=0, y=80)

    button_ac = tk.Button(canvas, text='AC', fg='white', bg='turquoise2',
                          font='Verdana 12', width=6, height=3,
                          activebackground='turquoise3',
                          activeforeground='white')
    button_ac.bind('<Button-1>')
    button_ac.place(x=75, y=80)

    button_c = tk.Button(canvas, text='C', fg='white', bg='turquoise2',
                         font='Verdana 12', width=6, height=3,
                         activebackground='turquoise3',
                         activeforeground='white')
    button_c.bind('<Button-1>')
    button_c.place(x=150, y=80)

    button7 = tk.Button(canvas, text='7', fg='white', bg='Deep sky blue',
                        font='Verdana 12', width=6, height=3,
                        activebackground='dodger blue',
                        activeforeground='white')
    button7.bind('<Button-1>')
    button7.place(x=0, y=160)

    button8 = tk.Button(canvas, text='8', fg='white', bg='Deep sky blue',
                        font='Verdana 12', width=6, height=3,
                        activebackground='dodger blue',
                        activeforeground='white')
    button8.bind('<Button-1>')
    button8.place(x=75, y=160)

    button9 = tk.Button(canvas, text='9', fg='white', bg='Deep sky blue',
                        font='Verdana 12', width=6, height=3,
                        activebackground='dodger blue',
                        activeforeground='white')
    button9.bind('<Button-1>')
    button9.place(x=150, y=160)

    button4 = tk.Button(canvas, text='4', fg='white', bg='Deep sky blue',
                        font='Verdana 12', width=6, height=3,
                        activebackground='dodger blue',
                        activeforeground='white')
    button4.bind('<Button-1>')
    button4.place(x=0, y=240)

    button5 = tk.Button(canvas, text='5', fg='white', bg='Deep sky blue',
                        font='Verdana 12', width=6, height=3,
                        activebackground='dodger blue',
                        activeforeground='white')
    button5.bind('<Button-1>')
    button5.place(x=75, y=240)

    button6 = tk.Button(canvas, text='6', fg='white', bg='Deep sky blue',
                        font='Verdana 12', width=6, height=3,
                        activebackground='dodger blue',
                        activeforeground='white')
    button6.bind('<Button-1>')
    button6.place(x=150, y=240)

    button1 = tk.Button(canvas, text='1', fg='white', bg='Deep sky blue',
                        font='Verdana 12', width=6, height=3,
                        activebackground='dodger blue',
                        activeforeground='white')
    button1.bind('<Button-1>')
    button1.place(x=0, y=320)

    button2 = tk.Button(canvas, text='2', fg='white', bg='Deep sky blue',
                        font='Verdana 12', width=6, height=3,
                        activebackground='dodger blue',
                        activeforeground='white')
    button2.bind('<Button-1>')
    button2.place(x=75, y=320)

    button3 = tk.Button(canvas, text='3', fg='white', bg='Deep sky blue',
                        font='Verdana 12', width=6, height=3,
                        activebackground='dodger blue',
                        activeforeground='white')
    button3.bind('<Button-1>')
    button3.place(x=150, y=320)

    button0 = tk.Button(canvas, text='0', fg='white', bg='Deep sky blue',
                        font='Verdana 12', width=6, height=3,
                        activebackground='dodger blue',
                        activeforeground='white')
    button0.bind('<Button-1>')
    button0.place(x=0, y=400)

    button_point = tk.Button(canvas, text='.', fg='white', bg='blue4',
                             font='Verdana 12', width=6, height=3,
                             activebackground='midnight blue',
                             activeforeground='white')
    button_point.bind('<Button-1>')
    button_point.place(x=75, y=400)

    button_equasion = tk.Button(canvas, text='=', fg='white', bg='turquoise2',
                                font='Verdana 12', width=6, height=3,
                                activebackground='turquoise3',
                                activeforeground='white')
    button_equasion.bind('<Button-1>')
    button_equasion.place(x=150, y=400)


def create_entries(canvas):
    '''
    Creates entries
    :return: Nothing
    '''
    entry_a = tk.Entry(canvas, width=4, bg='SkyBlue1')
    entry_a.place(x=25, y=10)

    canvas.create_text(80, 10, text='x^2+',
                       font='Verdana 12', fill='white',
                       anchor='n')

    entry_b = tk.Entry(canvas, width=4, bg='SkyBlue1')
    entry_b.place(x=105, y=10)

    canvas.create_text(150, 10, text='x+',
                       font='Verdana 12', fill='white',
                       anchor='n')

    entry_c = tk.Entry(canvas, width=4, bg='SkyBlue1')
    entry_c.place(x=163, y=10)

    entry_result = tk.Entry(canvas, width=27, bg='SkyBlue1')
    entry_result.place(x=25, y=35)


def create_drop_menu(root):
    '''
    :return: Nothing
    Creates drop menu
    '''
    drop_menu = tk.Menu(root)
    root.configure(menu=drop_menu)
    first_item = tk.Menu(drop_menu)
    drop_menu.add_cascade(label='Clear', menu=first_item)
    first_item.add_command(label='Clear all')
    first_item.add_command(label='Clear result')


def getter():



def main():
    root = tk.Tk()
    root.title('Calculator')
    canvas = tk.Canvas(root, height=CANVAS_HEIGHT,
                            width=CANVAS_WIDTH,
                            bg='black')
    canvas.grid(row=0, column=0)
    root.resizable(width=False, height=False)

    create_drop_menu(root)
    create_entries(canvas)
    create_buttons(canvas)

    root.mainloop()


main()
