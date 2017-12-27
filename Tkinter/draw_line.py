import pygame

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 238, 0)
LIGHT_BLUE = (0, 221, 255)
ORANGE = (255, 136, 0)


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

    for y_offset in range(0, 300, 10):
        pygame.draw.line(screen, RED, [0, 10+y_offset], [100, 110+y_offset], 5)
    for x_offset in range(100, 300, 10):
        pygame.draw.line(screen, GREEN, [10+x_offset, 0], [110+x_offset, 110], 5)
    for y_offset in range(300, 400, 10):
        for x_offset in range(100, 300, 10):
            pygame.draw.line(screen, ORANGE,\
                             [10+x_offset, 10+y_offset],\
                             [110+x_offset, 110+y_offset], 5)
        
        
    pygame.draw.line(screen, YELLOW, [0,0], [700, 500], 5)
    pygame.draw.line(screen, LIGHT_BLUE, [50, 0], [700, 500], 5)
    
    pygame.display.flip()
    clock.tick(20)

pygame.quit()
