import pygame

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
PARROT_BODY = [[500, 100], [550, 130], [590, 210], [570, 220], [500, 160]]
NAIL_RAD_CENTER = [(PARROT_BODY[2][0] + PARROT_BODY[3][0])//2, (PARROT_BODY[2][1] + PARROT_BODY[3][1])//2]
PARROT_TAIL = [PARROT_BODY[2], PARROT_BODY[3], [600, 400]]
PARROT_NECK = [[PARROT_BODY[0][0], PARROT_BODY[0][1] + 5], [PARROT_BODY[4][0], PARROT_BODY[4][1] - 20], [475, 120], [480, 95]]
PARROT_HEAD = [[460, 95], [480, 95], [475, 120], [460, 140]]
PARROT_F_WING = [[530, 145], [530, 155], [540, 165], [690, 165], [565, 120], [545, 125]]


def nail_move(arg):
    # x [480, 680]
    pass


def main():
    pygame.init()
    size = (900, 700)
    screen = pygame.display.set_mode(size)

    pygame.display.set_caption("My animation")

    done = False

    clock = pygame.time.Clock()
    end_line = [20, 20]
    start_line = [0, 0]
    increment = 1

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        screen.fill(BLACK)

        pygame.draw.polygon(screen, WHITE, PARROT_BODY, 3)
        for i in range(len(PARROT_BODY)):
            PARROT_BODY[i][0] -= 1
            PARROT_BODY[i][1] += 1

        pygame.draw.polygon(screen, WHITE, PARROT_TAIL, 3)
        PARROT_TAIL[2][0] -= 1
        PARROT_TAIL[2][1] += 1
        pygame.draw.polygon(screen, WHITE, PARROT_NECK, 3)
        for i in range(len(PARROT_NECK)):
            PARROT_NECK[i][0] -= 1
            PARROT_NECK[i][1] += 1
        pygame.draw.polygon(screen, WHITE, PARROT_HEAD, 3)
        for i in range(len(PARROT_HEAD)):
            PARROT_HEAD[i][0] -= 1
            PARROT_HEAD[i][1] += 1

        for i in range(len(PARROT_F_WING)):
            PARROT_F_WING[i][0] -= 1
            PARROT_F_WING[i][1] += 1
        pygame.draw.polygon(screen, WHITE, PARROT_F_WING, 3)
        clock.tick(100)
        pygame.display.flip()

    pygame.quit()




''' pygame.draw.arc(screen, RED, [[200, 400], [200, 200]], radians(90), radians(270), 3)
pygame.draw.arc(screen, RED, [[220, 420], [160, 160]], radians(90), radians(270), 3)
pygame.draw.arc(screen, RED, [[185, 600], [220, 150]], radians(0), radians(90), 3)
pygame.draw.arc(screen, RED, [[-15, 580], [600, 500]], radians(40), radians(90), 3)
#pygame.draw.arc(screen, RED, [[355, 650], [200, 200]], radians(55), radians(125), 3)
pygame.draw.arc(screen, RED, [[300, 400], [50, 50]], radians(180), radians(270), 3)
pygame.draw.line(screen, RED, [325, 450], [355, 460], 3)
pygame.draw.arc(screen, RED, [[355, 450], [50, 20]], radians(110), radians(180), 3)


pygame.draw.line(screen, WHITE, start_line, end_line, 10)
if end_line[0] < size[0] and end_line[1] < size[1]:
end_line[0] += increment
end_line[1] += increment
start_line[0] += increment
start_line[1] += increment
clock.tick(100)'''





main()
