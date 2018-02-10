import tkinter as tk

root = tk.Tk()

canvas = tk.Canvas(root, height=500,
                       width=500,
                       bg='black')
canvas.grid(row=0, column=0)

entry_c = tk.Entry(canvas, width=4, bg='SkyBlue1')
entry_c.place(x=163, y=10)
entry_c.focus_get()



root.mainloop()
