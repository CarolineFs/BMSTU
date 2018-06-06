import pygame

SIZE = (400, 300)
WINDOW_NAME = "Animation"

YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARKBLUE = (0, 13, 123)

def main():
    el = [-80, 35]
    pygame.init()
    screen = pygame.display.set_mode(SIZE)
    pygame.display.set_caption(WINDOW_NAME)
    done = False
    clock = pygame.time.Clock()
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        screen.fill(WHITE)
        pygame.draw.circle(screen, YELLOW, [300, 60], 20, 0)
        pygame.draw.ellipse(screen, DARKBLUE, [el, [80, 50]], 0)
        pygame.draw.polygon(screen, BLACK, [[20, 200], [20, 150], [45, 110],
                                            [70,150], [70, 200]], 3)
        pygame.draw.line(screen, BLACK, [20, 150], [70, 150], 3)
        pygame.draw.circle(screen, BLACK, [45, 175], 15, 3)

        el[0] += 1

        if el[0]== 400:
            el[0] = -80

        if el[0] + 80 >= 300 - 20 and el[0] <= 300 + 20:
            pygame.draw.circle(screen, YELLOW, [45, 175], 12, 0)
        
        clock.tick(40)
        pygame.display.flip()
    pygame.quit()


main()
