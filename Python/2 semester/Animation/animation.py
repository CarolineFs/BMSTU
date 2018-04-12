import pygame

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)


def main():
    pygame.init()
    size = (700, 500)
    screen = pygame.display.set_mode(size)

    pygame.display.set_caption("My animation")

    done = False

    clock = pygame.time.Clock()

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        screen.fill(BLACK)
        end_line = [20, 20]
        start_line = [0, 0]
        #while end_line[0] <= size[0] or end_line[1] <= size[1]:
            #screen.fill(BLACK)
            #print("3324")
        pygame.draw.line(screen, WHITE, start_line, end_line, 10)
        clock.tick(1000)
            #end_line[0] += 1
            #end_line[1] += 1
            #start_line[0] += 1
            #start_line[1] += 1
        screen.fill(BLACK)

        pygame.display.flip()

        clock.tick(50)

    pygame.quit()


main()


import pygame

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)


def main():
    pygame.init()
    size = (700, 500)
    screen = pygame.display.set_mode(size)

    pygame.display.set_caption("My animation")

    done = False

    clock = pygame.time.Clock()

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        screen.fill(BLACK)
        end_line = [20, 20]
        start_line = [0, 0]
        #while end_line[0] <= size[0] or end_line[1] <= size[1]:
            #screen.fill(BLACK)
            #print("3324")
        pygame.draw.line(screen, WHITE, start_line, end_line, 10)
        clock.tick(1000)
            #end_line[0] += 1
            #end_line[1] += 1
            #start_line[0] += 1
            #start_line[1] += 1
        screen.fill(BLACK)

        pygame.display.flip()

        clock.tick(50)

    pygame.quit()


main()

