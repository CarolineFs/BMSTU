import tkinter as tk
from marh import trunc

def clear_all(entry_8, entry_10):
    entry_8.delete(0, len(entry_8.get()))
    entry_10.delete(0, len(entry_10.get()))


def clear_one_entry(entry):
    entry.delete(0, len(entry.get()))
    


def get_8(entry_8, entry_10):
    flag = False
    number_8 = entry_8.get()
    
    if number_8 < 0:
        flag = True
        number_8 *= -1
            
    number_8 = ''.join(reversed(number_8))
    res = 0

    for i in range(len(number_8)):
        res += (int(number_8[i])*(8**i))
    res = str(res)

    if flag:
        res = '-' + res
        
    show_result(entry_10, res)
    

def show_result(entry, result):
    clear_one_entry(entry)
    entry.insert(0, result)
    

def get_10(entry_8, entry_10):
    flag = False
    number_10 = float(entry_10.get())
    integer = math.trinc(number_10)
    fl = 
    if number_10 < 0:
        flag = True
        number_10 *= -1
    res = ''
    while number_10 >= 8:
        div = int(number_10//8)
        mod = int(number_10%8)
        if div == 0:
            res = str(mod) + res
            break
        else:
            res = str(mod) + res
        number_10 //= 8
    res = str(int(number_10)) + res 

    if flag:
        res = '-' + res
    show_result(entry_8, res)


def create_button(canvas, text):
    button = tk.Button(canvas, text=text)
    return button


def draw_canwas(root):
    # CONST
    CANVAS_HEIGHT   = 200
    CANVAS_WIDTH    = 300
    
    canvas = tk.Canvas(root, height=CANVAS_HEIGHT,
                             width=CANVAS_WIDTH)
    canvas.grid(row=0, column=0)

    entry_10 = tk.Entry(canvas, width=20)
    entry_10.place(x=150, y=50)
    entry_10.focus()

    label_10 = tk.Label(text='Число в 10-ой с/с: ')
    label_10.place(x = 10, y = 50)

    entry_8 = tk.Entry(canvas, width=20)
    entry_8.place(x=150, y=100)

    label_8 = tk.Label(text='Число в 8-ой с/с: ')
    label_8.place(x = 10, y = 100)

    button_8_to_10 = create_button(canvas, '8 to 10')
    button_8_to_10.bind('<Button-1>', lambda x: get_8(entry_8, entry_10))
    button_8_to_10.place(x=50, y=160)

    button_10_to_8 = create_button(canvas, '10 to 8')
    button_10_to_8.bind('<Button-1>', lambda x: get_10(entry_8, entry_10))
    button_10_to_8.place(x=125, y=160)

    button_delete = create_button(canvas, 'Clear all')
    button_delete.bind('<Button-1>', lambda x: clear_all(entry_8, entry_10))
    button_delete.place(x=200, y=160)

    
def main():
    root = tk.Tk()
    root.title('Calculator')
    root.resizable(width=False, height=False)
    
    draw_canwas(root)
    
    root.mainloop()


main()
