import pygame
from math import radians

# Define colors
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
PARROT_HEAD_COLOR = (230, 230, 0)
PARROT_NECK_COLOR = (255, 214, 51)
PARROT_TAIL_COLOR = (255, 102, 0)

DRAGON_WING_COLOR = (0, 102, 0)

CLOUD1 = [800, 40]
CLOUD2 = [830, 40]
CLOUD3 = [860, 40]


CENTER = (450, 350)


def draw_background(screen):
    pygame.draw.rect(screen, LAWNGREEN, ((0, 350), (900, 350)), 0)
    pygame.draw.rect(screen, SUN_SHADES[0], ((0, 0), (900, 350)), 0)

    pygame.draw.circle(screen, WHITE, CLOUD1, 30, 0)
    pygame.draw.circle(screen, WHITE, CLOUD2, 30, 0)
    pygame.draw.circle(screen, WHITE, CLOUD3, 30, 0)

    sun_r = 200
    for sun_color in SUN_SHADES:
        pygame.draw.circle(screen, sun_color, (50, 50), sun_r, 0)
        sun_r -= 20

    pygame.draw.polygon(screen, GRAYBLUE, [[50, 350], [250, 50], [450, 350]], 0)
    pygame.draw.polygon(screen, GRAYBLUE, [[350, 350], [450, 150], [550, 350]], 0)

    pygame.draw.rect(screen, BROWN, [[600, 220], [20, 260]], 0)
    pygame.draw.ellipse(screen, DARKGREEN, [[560, 120], [100, 200]], 0)

    pygame.draw.polygon(screen, WATERBLUE, [[150, 350], [70, 445], [120, 440]], 0)
    pygame.draw.polygon(screen, WATERBLUE, [[70, 445], [120, 440], [500, 700], [130, 700]], 0)




def main():
    pygame.init()
    size = (900, 700)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("My animation")
    done = False

    clock = pygame.time.Clock()

    q = 0
    q2 = 0
    inc = 1
    inc2 = 1
    line1_start = [[240, 440], [100, 360]]
    line2_start = [[240, 440], [100, 430]]
    line3_start = [[240, 440], [110, 470]]
    arcs = [[200, 400], [30, 400], [45, 447], [47, 447], [-36, 477], [-79, 472], [-40, 477]]
    ell_start = [280, 390]
    dragon_eye = [310, 410]
    parr_body_start = [980, 125]
    parr_wing = [[990, 135],  [1000, 110], [1020, 100]]
    parr_head_start = [970, 125]
    parr_eye = [975, 130]
    parr_tail = [[1000, 135], [1020, 130], [1020, 140]]

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        if arcs[6][0] > 900:
            done = True



        draw_background(screen)

        pygame.draw.arc(screen, BLACK, [arcs[0], [200, 200]], radians(90), radians(190), 30)

        if parr_body_start[0] >= 640:
            pygame.draw.ellipse(screen, PARROT_BODY_COLOR, [parr_body_start, [30, 20]], 0)
            pygame.draw.ellipse(screen, PARROT_BODY_COLOR, [parr_head_start, [17, 17]], 0)
            pygame.draw.ellipse(screen, BLACK, [parr_eye, [2, 2]], 0)
            pygame.draw.polygon(screen, PARROT_F_WING_COLOR, parr_wing, 0)
            pygame.draw.polygon(screen, PARROT_BODY_COLOR, parr_tail, 0)

        pygame.draw.ellipse(screen, BLACK, [ell_start, [80, 50]], 0)

        if ell_start[1] <= 100 and ell_start[0] <= 590:
            pygame.draw.polygon(screen, SUN_SHADES[0], [[ell_start[0]+40, ell_start[1]+25],
                                                        [ell_start[0]+80, ell_start[1]+10],
                                                        [ell_start[0]+80, ell_start[1]+50]])

        pygame.draw.arc(screen, BLACK, [arcs[1], [200, 200]], radians(260), radians(360), 30)
        pygame.draw.arc(screen, BLACK, [arcs[2], [150, 150]], radians(225), radians(270), 25)

        pygame.draw.arc(screen, BLACK, [arcs[3], [150, 150]], radians(180), radians(225), 20)
        pygame.draw.arc(screen, BLACK, [arcs[4], [100, 100]], radians(0), radians(45), 15)
        pygame.draw.arc(screen, BLACK, [arcs[5], [150, 150]], radians(45), radians(70), 10)
        pygame.draw.arc(screen, BLACK, [arcs[6], [100, 100]], radians(70), radians(90), 5)


        pygame.draw.polygon(screen, DRAGON_WING_COLOR, [line1_start[0], line1_start[1], line2_start[1]], 0)
        pygame.draw.polygon(screen, DRAGON_WING_COLOR, [line1_start[0], line2_start[1], line3_start[1]], 0)

        pygame.draw.circle(screen, WHITE, dragon_eye, 2, 0)

        for arc in arcs:
            arc[0] += 1
            if ell_start[1] >= 100:
                arc[1] -= 1

        ell_start[0] += 1
        if ell_start[1] >= 100:
            ell_start[1] -= 1

        CLOUD1[0] -= q % 2
        CLOUD2[0] -= q % 2
        CLOUD3[0] -= q % 2

        if parr_body_start[0] >= 640:
            parr_body_start[0] -= 1
            parr_wing[0][0] -= 1
            parr_wing[1][0] -= 1
            parr_wing[2][0] -= 1
            parr_head_start[0] -= 1
            parr_eye[0] -= 1
            parr_tail[0][0] -= 1
            parr_tail[1][0] -= 1
            parr_tail[2][0] -= 1


        dragon_eye[0] += 1
        if ell_start[1] >= 100:
            dragon_eye[1] -= 1

        pygame.draw.line(screen, BLACK, line1_start[0], line1_start[1], 7)
        line1_start[0][0] += 1
        if ell_start[1] >= 100:
            line1_start[0][1] -= 1
        line1_start[1][0] += 1
        if ell_start[1] >= 100:
            line1_start[1][1] -= 1

        pygame.draw.line(screen, BLACK, line2_start[0], line2_start[1], 7)
        line2_start[0][0] += 1
        if ell_start[1] >= 100:
            line2_start[0][1] -= 1
        line2_start[1][0] += 1
        if ell_start[1] >= 100:
            line2_start[1][1] -= 1

        pygame.draw.line(screen, BLACK, line3_start[0], line3_start[1], 7)
        line3_start[0][0] += 1
        if ell_start[1] >= 100:
            line3_start[0][1] -= 1
        line3_start[1][0] += 1
        if ell_start[1] >= 100:
            line3_start[1][1] -= 1

        q2 += inc2
        if inc2 > 0:
            parr_wing[1][0] += 1
            parr_wing[1][1] += 1

            parr_wing[2][0] += 1
            parr_wing[2][1] += 1
        if inc2 < 0:
            parr_wing[1][0] -= 1
            parr_wing[1][1] -= 1
            parr_wing[2][0] -= 1
            parr_wing[2][1] -= 1

        if q2 == 15:
            inc2 = -1
        if q2 == 0:
            inc2 = 1

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

        clock.tick(60)
        pygame.display.flip()

    pygame.quit()


main()
