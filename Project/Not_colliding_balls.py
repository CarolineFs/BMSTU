from tkinter import *
from random import *

#const
WIDTH = 640
HEIGHT = 480
BG = 'white'
BAD_COLOR = 'red'
BLACK_COLOR = 'black'
COLORS = ['aqua', BAD_COLOR, 'fuchsia', 'pink', 'yellow', 'gold', 'chartreuse', 'green']
ZERO = 0
MAIN_BALL_RADIUS = 20
MAIN_BALL_COLOR = 'blue'
INIT_DX = 2
INIT_DY = 2
DELAY = 5
NUM_OF_BALLS = 10


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
                           fill = self.color,\
                           outline = self.color if self.color != BAD_COLOR\
                           else BLACK_COLOR)

    def hide(self):
        canvas.create_oval(self.x - self.r, self.y - self.r,\
                            self.x + self.r, self.y + self.r,\
                            fill = BG, outline = BG)

    def is_collision(self, ball):
        a = abs(self.x + self.dx - ball.x)
        b = abs(self.y + self.dy - ball.y)
        return (a*a + b*b)**0.5 <= self.r + ball.r
        
    def move(self):
        #colliding with walls
        if (self.x + self.r + self.dx >= WIDTH) or\
           (self.x - self.r + self.dx <= ZERO):
            self.dx = -self.dx
        if (self.y + self.r + self.dy >= HEIGHT) or\
           (self.y - self.r + self.dy <= ZERO):
            self.dy = -self.dy

        #colliding wiht balls
        for ball in balls:
            if self.is_collision(ball):
                if ball.color != BAD_COLOR:
                    ball.hide()
                    balls.remove(ball)
                    self.dx = -self.dx
                    self.dy = -self.dy
                else:
                    self.dx = self.dy = 0
        
            
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


#create list of balls
def create_list_of_balls(number):
    lst = []
    while len(lst) < number:
        next_ball = Balls(choice(range(0, WIDTH)),\
                          choice(range(0, HEIGHT)),\
                          choice(range(15, 35)),\
                          choice(COLORS))
        lst.append(next_ball)
        next_ball.draw()
    return lst


#count bad balls
def count_bad_balls(list_of_balls):
    res = 0
    for ball in list_of_balls:
        if ball.color == BAD_COLOR:
            res += 1
    return res

#main circle game
def main():
    if 'main_ball' in globals():
        main_ball.move()
        if len(balls) - num_of_bad_balls == 0:
            canvas.create_text(WIDTH/2, HEIGHT/2, text = 'WIN!',\
                               font = 'Arial 20', fill = MAIN_BALL_COLOR)
            main_ball.dx = main_ball.dy = 0
        elif main_ball.dx == 0:
            canvas.create_text(WIDTH/2, HEIGHT/2, text = 'YOU LOST!',\
                               font = 'Arial 20', fill = BAD_COLOR)
    root.after(DELAY, main)

        
root = Tk()
root.title('Balls')
canvas = Canvas(root,width = WIDTH, height = HEIGHT, bg = BG)
canvas.pack()
canvas.bind('<Button-1>',mouse_click)
canvas.bind('<Button-3>',mouse_click, '+')
if 'main_ball' in globals():
    del main_ball
balls = create_list_of_balls(NUM_OF_BALLS)
num_of_bad_balls = count_bad_balls(balls)
main()
root.mainloop()
