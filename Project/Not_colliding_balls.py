from tkinter import *

#const
WIDTH = 640
HEIGHT = 480
BG = 'white'
ZERO = 0
MAIN_BALL_RADIUS = 20
MAIN_BALL_COLOR = 'blue'
INIT_DX = 2
INIT_DY = 2
DELAY = 5


#balls class
class Balls():
    def __init__(self, x, y, r, color, dx = 0, dy = 0):
        self.x = x
        self.y = y
        self.r = r
        self.color = color
        self.dx = dx
        self.dy = dy

    def draw(self):
        canvas.create_oval(self.x - self.r, self.y - self.r,\
                            self.x + self.r, self.y + self.r,\
                            fill = self.color, )

    def hide(self):
        canvas.create_oval(self.x - self.r, self.y - self.r,\
                            self.x + self.r, self.y + self.r,\
                            fill = BG, outline = BG)

    def move(self):
        #colliding with walls
        if (self.x + self.r + self.dx >= WIDTH) or\
           (self.x - self.r + self.dx <= ZERO):
            self.dx = -self.dx
        if (self.y + self.r + self.dy >= HEIGHT) or\
           (self.y - self.r + self.dy <= ZERO):
            self.dy = -self.dy  
            
            
        self.hide()
        self.x += self.dx
        self.y += self.dy
        self.draw()
        


#mouse events
def mouse_click(event):
    global main_ball
    if event.num == 1:
        if 'main_ball' not in globals():
            main_ball = Balls(event.x, event.y,\
                          MAIN_BALL_RADIUS,\
                          MAIN_BALL_COLOR,\
                          INIT_DX, INIT_DY)
            main_ball.draw()
        else: #turn left 
            if main_ball.dx * main_ball.dy > 0:
                main_ball.dy = -main_ball.dy
            else:
                main_ball.dx = -main_ball.dx
    elif event.num == 3: #turn right
        if main_ball.dx * main_ball.dy > 0:
            main_ball.dx = -main_ball.dx
        else:
            main_ball.dy = -main_ball.dy
    else:
        main_ball.hide()


#main circle game
def main():
    if 'main_ball' in globals():
        main_ball.move()
    root.after(DELAY, main)


        
root = Tk()
root.title('Balls')
canvas = Canvas(root,width = WIDTH, height = HEIGHT, bg = BG)
canvas.pack()
canvas.bind('<Button-1>',mouse_click)
canvas.bind('<Button-3>',mouse_click, '+')
if 'main_ball' in globals():
    del main_ball
main()
root.mainloop()

