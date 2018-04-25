import pygame
from math import radians

# Определим некоторые цвета
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BROWN = (179, 89, 0)
WATERBLUE = (0, 153, 255)
DARKGREEN = (0, 128, 0)
LAWNGREEN = (124, 252, 0)
GRAYBLUE = (133, 133, 173)
DARKTURQUOSE = (0, 206, 209)
SUN_SHADES = ((153, 255, 255), (230, 255, 255), (255, 255, 204),
              (255, 255, 153), (255, 255, 102), (255, 255, 26),
              (255, 255, 0))
PARROT_BODY_COLOR = (255, 153, 51)
PARROT_F_WING_COLOR = (255, 204, 0)
DRAGON_WING_COLOR = (0, 102, 0)

# Определим начальные координаты некоторых фигур
# Координаты центров окружностей, образущих облако
CLOUD1 = [800, 40]
CLOUD2 = [830, 40]
CLOUD3 = [860, 40]

# Размер окна
SIZE = (900, 700)

# Название окна
WINDOW_NAME = "My animation"

# Крылья дракона
WING_LINE1 = [[240, 440], [100, 360]]
WING_LINE2 = [[240, 440], [100, 430]]
WING_LINE3 = [[240, 440], [110, 470]]

# Эллипсы, составляющие тело дракона
ARCS = [[200, 400], [30, 400], [45, 447], [47, 447],
        [-36, 477], [-79, 472], [-40, 477]]

# Голова и глаз дракона
DRAGON_HEAD = [280, 390]
DRAGON_EYE = [310, 410]

# Тело птицы
PARROT_BODY = [980, 125]
PARROT_WING = [[990, 135],  [1000, 110], [1020, 100]]
PARROT_HEAD = [970, 125]
PARROT_EYE = [975, 130]
PARROT_TAIL = [[1000, 135], [1020, 130], [1020, 140]]


def draw_background(screen):
    # Рисуем задний фон

    # Небо
    pygame.draw.rect(screen, LAWNGREEN, ((0, 350), (900, 350)), 0)

    # Земля
    pygame.draw.rect(screen, SUN_SHADES[0], ((0, 0), (900, 350)), 0)

    # Облако
    pygame.draw.circle(screen, WHITE, CLOUD1, 30, 0)
    pygame.draw.circle(screen, WHITE, CLOUD2, 30, 0)
    pygame.draw.circle(screen, WHITE, CLOUD3, 30, 0)

    # Солнце
    sun_r = 200
    for sun_color in SUN_SHADES:
        pygame.draw.circle(screen, sun_color, (50, 50), sun_r, 0)
        sun_r -= 20

    # Горы
    pygame.draw.polygon(screen, GRAYBLUE, [[50, 350], [250, 50], [450, 350]], 0)
    pygame.draw.polygon(screen, GRAYBLUE, [[350, 350], [450, 150], [550, 350]], 0)

    # Дерево
    pygame.draw.rect(screen, BROWN, [[600, 220], [20, 260]], 0)
    pygame.draw.ellipse(screen, DARKGREEN, [[560, 120], [100, 200]], 0)

    # Река
    pygame.draw.polygon(screen, WATERBLUE, [[150, 350], [70, 445], [120, 440]], 0)
    pygame.draw.polygon(screen, WATERBLUE, [[70, 445], [120, 440], [500, 700], [130, 700]], 0)


def main():
    pygame.init()
    screen = pygame.display.set_mode(SIZE)
    pygame.display.set_caption(WINDOW_NAME)
    done = False
    clock = pygame.time.Clock()

    # Для изменения направления махов крылом дракона
    q = 0
    inc = 1

    # Для изменения направления махов крылом птицы
    q2 = 0
    inc2 = 1

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        # Если хвост дракона вышел за правую границу окна
        if ARCS[6][0] > 900:
            done = True

        draw_background(screen)

        pygame.draw.arc(screen, BLACK, [ARCS[0], [200, 200]], 
                        radians(90), radians(190), 30)

        if PARROT_BODY[0] >= 640:
            pygame.draw.ellipse(screen, PARROT_BODY_COLOR, 
                                [PARROT_BODY, [30, 20]], 0)
            pygame.draw.ellipse(screen, PARROT_BODY_COLOR, 
                                [PARROT_HEAD, [17, 17]], 0)
            pygame.draw.ellipse(screen, BLACK, 
                                [PARROT_EYE, [2, 2]], 0)
            pygame.draw.polygon(screen, PARROT_F_WING_COLOR,
                                PARROT_WING, 0)
            pygame.draw.polygon(screen, PARROT_BODY_COLOR, 
                                PARROT_TAIL, 0)

        pygame.draw.ellipse(screen, BLACK, [DRAGON_HEAD, [80, 50]], 0)

        if DRAGON_HEAD[1] <= 100 and DRAGON_HEAD[0] <= 590:
            pygame.draw.polygon(screen, SUN_SHADES[0], 
                                [[DRAGON_HEAD[0]+40, DRAGON_HEAD[1]+25],
                                [DRAGON_HEAD[0]+80, DRAGON_HEAD[1]+10],
                                [DRAGON_HEAD[0]+80, DRAGON_HEAD[1]+50]])

        pygame.draw.arc(screen, BLACK, [ARCS[1], [200, 200]], 
                        radians(260), radians(360), 30)
        pygame.draw.arc(screen, BLACK, [ARCS[2], [150, 150]], 
                        radians(225), radians(270), 25)

        pygame.draw.arc(screen, BLACK, [ARCS[3], [150, 150]], 
                        radians(180), radians(225), 20)
        pygame.draw.arc(screen, BLACK, [ARCS[4], [100, 100]], 
                        radians(0), radians(45), 15)
        pygame.draw.arc(screen, BLACK, [ARCS[5], [150, 150]], 
                        radians(45), radians(70), 10)
        pygame.draw.arc(screen, BLACK, [ARCS[6], [100, 100]], 
                        radians(70), radians(90), 5)

        pygame.draw.polygon(screen, DRAGON_WING_COLOR, 
                            [WING_LINE1[0], WING_LINE1[1], WING_LINE2[1]], 0)
        pygame.draw.polygon(screen, DRAGON_WING_COLOR, 
                            [WING_LINE1[0], WING_LINE2[1], WING_LINE3[1]], 0)

        pygame.draw.circle(screen, WHITE, DRAGON_EYE, 2, 0)

        for arc in ARCS:
            arc[0] += 1
            if DRAGON_HEAD[1] >= 100:
                arc[1] -= 1

        DRAGON_HEAD[0] += 1
        if DRAGON_HEAD[1] >= 100:
            DRAGON_HEAD[1] -= 1

        CLOUD1[0] -= q % 2
        CLOUD2[0] -= q % 2
        CLOUD3[0] -= q % 2

        if PARROT_BODY[0] >= 640:
            PARROT_BODY[0] -= 1
            PARROT_WING[0][0] -= 1
            PARROT_WING[1][0] -= 1
            PARROT_WING[2][0] -= 1
            PARROT_HEAD[0] -= 1
            PARROT_EYE[0] -= 1
            PARROT_TAIL[0][0] -= 1
            PARROT_TAIL[1][0] -= 1
            PARROT_TAIL[2][0] -= 1

        DRAGON_EYE[0] += 1
        WING_LINE1[0][0] += 1
        WING_LINE1[1][0] += 1
        WING_LINE2[0][0] += 1
        WING_LINE2[1][0] += 1
        WING_LINE3[0][0] += 1
        WING_LINE3[1][0] += 1

        if DRAGON_HEAD[1] >= 100:
            DRAGON_EYE[1] -= 1
            WING_LINE1[0][1] -= 1
            WING_LINE1[1][1] -= 1
            WING_LINE3[1][1] -= 1
            WING_LINE2[0][1] -= 1
            WING_LINE2[1][1] -= 1
            WING_LINE3[0][1] -= 1

        pygame.draw.line(screen, BLACK, WING_LINE1[0], WING_LINE1[1], 7)
        pygame.draw.line(screen, BLACK, WING_LINE2[0], WING_LINE2[1], 7)
        pygame.draw.line(screen, BLACK, WING_LINE3[0], WING_LINE3[1], 7)

        q2 += inc2
        if inc2 > 0:
            PARROT_WING[1][0] += 1
            PARROT_WING[1][1] += 1

            PARROT_WING[2][0] += 1
            PARROT_WING[2][1] += 1
        if inc2 < 0:
            PARROT_WING[1][0] -= 1
            PARROT_WING[1][1] -= 1
            PARROT_WING[2][0] -= 1
            PARROT_WING[2][1] -= 1

        if q2 == 15:
            inc2 = -1
        if q2 == 0:
            inc2 = 1

        q += inc
        if inc > 0:
            WING_LINE1[1][0] += 1
            WING_LINE1[1][1] += 1

            WING_LINE2[1][0] += 1
            WING_LINE2[1][1] += 1

            WING_LINE3[1][0] += 1
            WING_LINE3[1][1] += 1
        if inc < 0:
            WING_LINE1[1][0] -= 1
            WING_LINE1[1][1] -= 1

            WING_LINE2[1][0] -= 1
            WING_LINE2[1][1] -= 1

            WING_LINE3[1][0] -= 1
            WING_LINE3[1][1] -= 1
        if q == 60:
            inc = -1
        if q == 0:
            inc = 1

        clock.tick(80)
        pygame.display.flip()

    pygame.quit()


main()
