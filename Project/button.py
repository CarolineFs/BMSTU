from tkinter import *

root = Tk()
but = Button(root)
but['text'] = 'Печать'
def printer(event):
     print ("Как всегда очередной 'Hello World!'")

but.bind("<Button-1>",printer)
but.pack()
