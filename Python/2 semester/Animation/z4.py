import pygame
from math import sin, cos

SIZE = (900, 700)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
WINDOW_NAME = 'Defend4'


def main():
    pygame.init()
    screen = pygame.display.set_mode(SIZE)
    pygame.display.set_caption(WINDOW_NAME)
    done = False
    clock = pygame.time.Clock()
    c_center = [70, 400]
    eye1 = [[c_center[0]-30, c_center[1]-30], [c_center[0]-30, c_center[1]-20],
            [c_center[0]-20, c_center[1]-20], [c_center[0]-20, c_center[1]-30]]
    eye2 = [[c_center[0]+30, c_center[1]-30], [c_center[0]+30, c_center[1]-20],
            [c_center[0]+20, c_center[1]-20], [c_center[0]+20, c_center[1]-30]]
    mouth = [[c_center[0]-10, c_center[1]+10], [c_center[0]+10,c_center[1]+10],
             [c_center[0], c_center[1]+20]]

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            screen.fill(WHITE)

            pygame.draw.circle(screen, BLACK, c_center, 70, 3)
            #pygame.draw.polygon(screen, BLACK, eye1, 3)
            #pygame.draw.polygon(screen, BLACK, eye2, 3)
            #pygame.draw.polygon(screen, BLACK, mouth, 3)

            c_center[0] += 1

            clock.tick(1000)
            pygame.display.flip()

    pygame.quit()


main()
