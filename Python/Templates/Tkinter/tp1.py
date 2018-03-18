import tkinter as tk

# CONST
CANVAS_HEIGHT = 300
CANVAS_WIDTH = 500


def create_labels():
    pass


def create_entry(canvas, y, x, width):
    entry = tk.Entry(canvas, width=width)
    entry.place(x=x, y=y)
    return entry


def canvas_creator(root):
    canvas = tk.Canvas(root,
                       height=CANVAS_HEIGHT,
                       width=CANVAS_WIDTH)
    canvas.grid(row=0, column=0)
    return canvas


def main():
    root = tk.Tk()
    root.title('Roots')
    root.resizable(width=False, height=False)

    canvas = canvas_creator(root)

    entry_epsilon = create_entry(canvas, 10, 10, 20)

    root.mainloop()
