import pygame

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
SIZE = (700, 500)

pygame.init()

screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption('Tetris')

done = False
clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(WHITE)
    pygame.display.flip()
    clock.tick(20)

pygame.quit()
