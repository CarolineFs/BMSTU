import pygame
from math import radians

# Define colors
BLACK = (0, 0, 0)
LAWNGREEN = (124,252,0)
DARKTURQUOSE = (0,206,209)
SUN_SHADES = ((153, 255, 255), (230, 255, 255), (255, 255, 204),
              (255, 255, 153), (255, 255, 102), (255, 255, 26),
              (255, 255, 0))
PARROT_BODY_COLOR = (255, 153, 51)
PARROT_F_WING_COLOR = (255, 204, 0)
PARROT_HEAD_COLOR = (230, 230, 0)
PARROT_NECK_COLOR = (255, 214, 51)
PARROT_TAIL_COLOR = (255, 102, 0)

DRAGON_WING_COLOR = (0, 102, 0)

WING_LEN = 200
PARROT_BODY = [[500, 100], [550, 130], [590, 210], [570, 220], [500, 160]]
NAIL_RAD_CENTER = [(PARROT_BODY[2][0] + PARROT_BODY[3][0])//2, (PARROT_BODY[2][1] + PARROT_BODY[3][1])//2]
PARROT_TAIL = [PARROT_BODY[2], PARROT_BODY[3], [600, 400]]
PARROT_NECK = [[PARROT_BODY[0][0], PARROT_BODY[0][1] + 5], [PARROT_BODY[4][0], PARROT_BODY[4][1] - 20], [475, 120], [480, 95]]
PARROT_HEAD = [[460, 95], [480, 95], [475, 120], [460, 140]]
PARROT_F_WING = [[520, 145], [550, 115], [720, 145]]
CENTER = (450, 350)


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

    q = 0
    inc = 1
    line1_start = [[240, 440], [100, 360]]
    line2_start = [[240, 440], [100, 430]]
    line3_start = [[240, 440], [110, 470]]

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        screen.fill(BLACK)

        pygame.draw.rect(screen, LAWNGREEN, ((0, 350), (900, 350)), 0)
        pygame.draw.rect(screen, SUN_SHADES[0], ((0, 0), (900, 350)), 0)

        sun_r = 200
        for sun_color in SUN_SHADES:
            pygame.draw.circle(screen, sun_color, (50, 50), sun_r, 0)
            sun_r -= 20

        pygame.draw.arc(screen, BLACK, [[200, 400], [200, 200]], radians(90), radians(190), 30)
        pygame.draw.ellipse(screen, BLACK, [[280, 390], [80, 50]], 0)
        pygame.draw.arc(screen, BLACK, [[30, 400], [200, 200]], radians(260), radians(360), 30)
        pygame.draw.arc(screen, BLACK, [[45, 447], [150, 150]], radians(225), radians(270), 25)

        pygame.draw.arc(screen, BLACK, [[47, 447], [150, 150]], radians(180), radians(225), 20)
        pygame.draw.arc(screen, BLACK, [[-36, 477], [100, 100]], radians(0), radians(45), 15)
        pygame.draw.arc(screen, BLACK, [[-79, 472], [150, 150]], radians(45), radians(70), 10)
        pygame.draw.arc(screen, BLACK, [[-40, 477], [100, 100]], radians(70), radians(90), 5)

        pygame.draw.polygon(screen, DRAGON_WING_COLOR, [line1_start[0], line1_start[1], line2_start[1]], 0)
        pygame.draw.polygon(screen, DRAGON_WING_COLOR, [line1_start[0], line2_start[1], line3_start[1]], 0)


        pygame.draw.line(screen, BLACK, line1_start[0], line1_start[1], 7)
        line1_start[0][0] += 1
        line1_start[0][1] -= 1
        line1_start[1][0] += 1
        line1_start[1][1] -= 1


        pygame.draw.line(screen, BLACK, line2_start[0], line2_start[1], 7)
        line2_start[0][0] += 1
        line2_start[0][1] -= 1
        line2_start[1][0] += 1
        line2_start[1][1] -= 1

        pygame.draw.line(screen, BLACK, line3_start[0], line3_start[1], 7)
        line3_start[0][0] += 1
        line3_start[0][1] -= 1
        line3_start[1][0] += 1
        line3_start[1][1] -= 1

        q += inc
        if inc > 0:
            line1_start[1][0] += 1
            line1_start[1][1] += 1

            line2_start[1][0] += 1
            line2_start[1][1] += 1

            line3_start[1][0] += 1
            line3_start[1][1] += 1
        if inc < 0:
            line1_start[1][0] -= 1
            line1_start[1][1] -= 1

            line2_start[1][0] -= 1
            line2_start[1][1] -= 1

            line3_start[1][0] -= 1
            line3_start[1][1] -= 1
        if q == 60:
            inc = -1
        if q == 0:
            inc = 1


        '''pygame.draw.arc(screen, BLACK, [[185, 600], [220, 150]], radians(0), radians(90), 3)
        pygame.draw.arc(screen, BLACK, [[-15, 580], [600, 500]], radians(40), radians(90), 3)
        # pygame.draw.arc(screen, BLACK, [[355, 650], [200, 200]], radians(55), radians(125), 3)
        pygame.draw.arc(screen, BLACK, [[300, 400], [50, 50]], radians(180), radians(270), 3)
        pygame.draw.line(screen, BLACK, [325, 450], [355, 460], 3)
        pygame.draw.arc(screen, BLACK, [[355, 450], [50, 20]], radians(110), radians(180), 3)'''

        '''pygame.draw.polygon(screen, PARROT_BODY_COLOR, PARROT_BODY, 0)
        for i in range(len(PARROT_BODY)):
            PARROT_BODY[i][0] -= 1
            PARROT_BODY[i][1] += 1

        pygame.draw.polygon(screen, PARROT_TAIL_COLOR, PARROT_TAIL, 0)
        PARROT_TAIL[2][0] -= 1
        PARROT_TAIL[2][1] += 1
        pygame.draw.polygon(screen, PARROT_NECK_COLOR, PARROT_NECK, 0)
        for i in range(len(PARROT_NECK)):
            PARROT_NECK[i][0] -= 1
            PARROT_NECK[i][1] += 1
        pygame.draw.polygon(screen, PARROT_HEAD_COLOR, PARROT_HEAD, 0)
        for i in range(len(PARROT_HEAD)):
            PARROT_HEAD[i][0] -= 1
            PARROT_HEAD[i][1] += 1

        pygame.draw.polygon(screen, PARROT_F_WING_COLOR, PARROT_F_WING, 0)
        for i in range(len(PARROT_F_WING)):
            PARROT_F_WING[i][0] -= 1
            PARROT_F_WING[i][1] += 1
        q += inc
        if inc > 0:
            PARROT_F_WING[1][0] -= 1
            PARROT_F_WING[1][1] += 1
            PARROT_F_WING[2][0] -= 1
            PARROT_F_WING[2][1] += 1
        if inc < 0:
            PARROT_F_WING[1][0] += 1
            PARROT_F_WING[1][1] -= 1
            PARROT_F_WING[2][0] += 1
            PARROT_F_WING[2][1] -= 1
        if q == 60:
            inc = -1
        if q == 0:
            inc = 1'''

        clock.tick(70)
        pygame.display.flip()

    pygame.quit()


main()
