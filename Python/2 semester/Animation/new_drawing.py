import pygame
from math import radians, sin, cos

SIZE = (900, 700)
WINDOW_NAME = "Animation"

LAWNGREEN = (0, 223, 0)
DARKTURQUOSE = [0, 132, 255]
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
GRAY = (105, 105, 105)
BROWN = (128, 87, 0)
DARKGREEN = (22, 100, 0)
BLACK = (0, 0, 0)
DARKBLUE = (0, 13, 123)
DARKORANGE = (255, 110, 18)
ORANGE = (255, 154, 46)


def main():
    pygame.init()
    screen = pygame.display.set_mode(SIZE)
    pygame.display.set_caption(WINDOW_NAME)
    done = False
    clock = pygame.time.Clock()
    a0 = 1
    flag = 0
    b_flag = 0

    sun_pos = [40, 40]
    cloud11_pos = [900, 15]
    cloud12_pos = [860, 10]
    cloud13_pos = [820, 15]

    cloud21_pos = [900, 100]
    cloud22_pos = [860, 90]
    cloud23_pos = [820, 100]

    dragon_inc = [1, 1]

    sky_increment = -0.5
    umouth = [[315, 400], [365, 420], [315, 420]]
    lmouth = [[315, 420], [365, 420], [315, 438]]

    dragon_arc1 = [280, 400]
    dragon_arc2 = [225, 405]
    dragon_arc3 = [105, 400]
    dragon_arc4 = [130, 440]
    dragon_arc5 = [140, 440]
    dragon_arc6 = [68, 475]
    dragon_eye = [300, 415]

    wind_line1 = [[250, 440], [190, 380]]
    wind_line2 = [[190, 380], [100, 400]]
    wing = [[250, 440], [190, 380], [100, 400], [160, 420], [130, 460]]

    wing_counter = 0
    b_wing_counter = 0
    m_flag = 0

    bird_head = [800, 200]
    bird_body = [[805, 190], [40, 30]]
    bird_tail = [[840, 205], [860, 190], [855, 215]]
    bird_wing = [[815, 200], [830, 170], [860, 170]]

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        draw_backgronnd(screen, sun_pos, cloud11_pos, cloud12_pos, cloud13_pos,
                        cloud21_pos, cloud22_pos, cloud23_pos)

        pygame.draw.circle(screen, ORANGE, bird_head, 10)
        pygame.draw.circle(screen, WHITE, bird_head, 2)
        pygame.draw.ellipse(screen, ORANGE, bird_body, 0)
        pygame.draw.polygon(screen, ORANGE, bird_tail, 0)
        pygame.draw.polygon(screen, DARKORANGE, bird_wing, 0)

        pygame.draw.line(screen, BLACK, wind_line1[0], wind_line1[1], 6)
        pygame.draw.line(screen, BLACK, wind_line2[0], wind_line2[1], 6)
        pygame.draw.polygon(screen, DARKBLUE, wing, 0)

        pygame.draw.polygon(screen, BLACK, umouth)
        pygame.draw.polygon(screen, BLACK, lmouth)
        pygame.draw.arc(screen, BLACK, [dragon_arc1, [70, 40]], radians(90), radians(270), 20)
        pygame.draw.arc(screen, BLACK, [dragon_arc2, [150, 190]], radians(90), radians(180), 30)
        pygame.draw.circle(screen, WHITE, dragon_eye, 3)
        pygame.draw.arc(screen, BLACK, [dragon_arc3, [150, 190]], radians(250), radians(0), 30)
        pygame.draw.arc(screen, BLACK, [dragon_arc4, [100, 150]], radians(220), radians(250), 20)
        pygame.draw.arc(screen, BLACK, [dragon_arc5, [60, 150]], radians(180), radians(220), 10)
        pygame.draw.arc(screen, BLACK, [dragon_arc6, [80, 80]], radians(0), radians(90), 5)

        cloud11_pos[0] -= 8
        cloud12_pos[0] -= 8
        cloud13_pos[0] -= 8

        cloud21_pos[0] -= 6
        cloud22_pos[0] -= 6
        cloud23_pos[0] -= 6

        sun_pos[0] += int(3 * cos(a0))
        sun_pos[1] += int(3 * sin(a0))
        a0 += 0.0000005

        if DARKTURQUOSE[1] == 0 or DARKTURQUOSE[2] == 0:
            sky_increment = 0.5
            a0 = -2

        if DARKTURQUOSE[1] == 255 or DARKTURQUOSE[2] == 255:
            sky_increment = -0.5
            a0 = 1

        #DARKTURQUOSE[1] += sky_increment
        #DARKTURQUOSE[2] += 2*sky_increment

        if cloud13_pos[0] < -200:
            cloud11_pos = [900, 15]
            cloud12_pos = [860, 10]
            cloud13_pos = [820, 15]

        if cloud23_pos[0] < -200:
            cloud21_pos = [900, 100]
            cloud22_pos = [860, 90]
            cloud23_pos = [820, 100]

        dragon_arc1[0] += dragon_inc[0]
        dragon_arc1[1] -= dragon_inc[1]
        dragon_arc2[0] += dragon_inc[0]
        dragon_arc2[1] -= dragon_inc[1]
        dragon_arc3[0] += dragon_inc[0]
        dragon_arc3[1] -= dragon_inc[1]
        dragon_arc4[0] += dragon_inc[0]
        dragon_arc4[1] -= dragon_inc[1]
        dragon_arc5[0] += dragon_inc[0]
        dragon_arc5[1] -= dragon_inc[1]
        dragon_arc6[0] += dragon_inc[0]
        dragon_arc6[1] -= dragon_inc[1]
        dragon_eye[0] += dragon_inc[0]
        dragon_eye[1] -= dragon_inc[1]
        umouth[0][0] += dragon_inc[0]
        umouth[0][1] -= dragon_inc[1]
        umouth[1][0] += dragon_inc[0]
        umouth[1][1] -= dragon_inc[1]
        umouth[2][0] += dragon_inc[0]
        umouth[2][1] -= dragon_inc[1]
        lmouth[0][0] += dragon_inc[0]
        lmouth[0][1] -= dragon_inc[1]
        lmouth[1][0] += dragon_inc[0]
        lmouth[1][1] -= dragon_inc[1]
        lmouth[2][0] += dragon_inc[0]
        lmouth[2][1] -= dragon_inc[1]
        wind_line1[0][0] += dragon_inc[0]
        wind_line1[0][1] -= dragon_inc[1]
        wind_line1[1][0] += dragon_inc[0]
        wind_line1[1][1] -= dragon_inc[1]
        wind_line2[0][0] += dragon_inc[0]
        wind_line2[0][1] -= dragon_inc[1]
        wind_line2[1][0] += dragon_inc[0]
        wind_line2[1][1] -= dragon_inc[1]
        wing[0][0] += dragon_inc[0]
        wing[0][1] -= dragon_inc[1]
        wing[1][0] += dragon_inc[0]
        wing[1][1] -= dragon_inc[1]
        wing[2][0] += dragon_inc[0]
        wing[2][1] -= dragon_inc[1]
        wing[3][0] += dragon_inc[0]
        wing[3][1] -= dragon_inc[1]
        wing[4][0] += dragon_inc[0]
        wing[4][1] -= dragon_inc[1]

        if wing_counter == 0:
            flag = 0
        if wing_counter == 60:
            wing_counter -= 1
            flag = 1
        if flag == 0:
            wind_line1[1][1] += 1
            wind_line2[0][1] += 1
            wind_line2[1][1] += 1
            wind_line2[1][0] += 0.5
            wing[1][1] += 1
            wing[2][1] += 1
            wing[3][1] += 1
            wing[4][1] += 0.5
            wing[2][0] += 0.5
            wing[4][0] += 0.5
            wing_counter += 1
        if flag == 1:
            wind_line1[1][1] -= 1
            wind_line2[0][1] -= 1
            wind_line2[1][1] -= 1
            wind_line2[1][0] -= 0.5
            wing[1][1] -= 1
            wing[2][1] -= 1
            wing[3][1] -= 1
            wing[4][1] -= 0.5
            wing[2][0] -= 0.5
            wing[4][0] -= 0.5
            wing_counter -= 1

        if b_wing_counter == 0:
            b_flag = 0
        if b_wing_counter == 30:
            b_flag = 1

        if b_flag == 0:
            bird_wing[1][0] -= 0.5
            bird_wing[1][1] += 1
            bird_wing[2][0] -= 0.5
            bird_wing[2][1] += 1
            b_wing_counter += 1

        if b_flag == 1:
            bird_wing[1][0] += 0.5
            bird_wing[1][1] -= 1
            bird_wing[2][0] += 0.5
            bird_wing[2][1] -= 1
            b_wing_counter -= 1

        if m_flag == 0 and dragon_eye[1] == 200:
            dragon_inc[1] = 0
            umouth[1][1] -= 20
            lmouth[1][1] += 20
            m_flag = 1

        if bird_tail[1][0] <= umouth[1][0]:
            pass

        bird_head[0] -= dragon_inc[0]

        bird_tail[0][0] -= dragon_inc[0]
        bird_tail[1][0] -= dragon_inc[0]
        bird_tail[2][0] -= dragon_inc[0]

        bird_wing[0][0] -= dragon_inc[0]
        bird_wing[1][0] -= dragon_inc[0]
        bird_wing[2][0] -= dragon_inc[0]

        bird_body[0][0] -= 1

        clock.tick(45)

        pygame.display.flip()

    pygame.quit()


def draw_backgronnd(screen, sun_pos, cloud11_pos, cloud12_pos, cloud13_pos,
                    cloud21_pos, cloud22_pos, cloud23_pos):
    pygame.draw.rect(screen, DARKTURQUOSE, [[0, 0], [900, 700]], 0)

    pygame.draw.circle(screen, YELLOW, sun_pos, 30)

    pygame.draw.polygon(screen, GRAY, ([500, 400], [900, 400], [700, 100]))

    pygame.draw.ellipse(screen, WHITE, [cloud11_pos, [80, 60]], 0)
    pygame.draw.ellipse(screen, WHITE, [cloud12_pos, [80, 70]], 0)
    pygame.draw.ellipse(screen, WHITE, [cloud13_pos, [80, 60]], 0)

    pygame.draw.ellipse(screen, WHITE, [cloud21_pos, [80, 60]], 0)
    pygame.draw.ellipse(screen, WHITE, [cloud22_pos, [80, 80]], 0)
    pygame.draw.ellipse(screen, WHITE, [cloud23_pos, [80, 60]], 0)

    pygame.draw.ellipse(screen, DARKGREEN, [[-10, 330], [50, 80]])
    pygame.draw.ellipse(screen, DARKGREEN, [[15, 320], [50, 80]])
    pygame.draw.ellipse(screen, DARKGREEN, [[25, 330], [50, 80]])
    pygame.draw.ellipse(screen, DARKGREEN, [[35, 340], [50, 80]])
    pygame.draw.ellipse(screen, DARKGREEN, [[55, 335], [50, 80]])
    pygame.draw.ellipse(screen, DARKGREEN, [[105, 320], [50, 80]])
    pygame.draw.ellipse(screen, DARKGREEN, [[115, 310], [50, 80]])
    pygame.draw.ellipse(screen, DARKGREEN, [[150, 305], [50, 80]])
    pygame.draw.ellipse(screen, DARKGREEN, [[170, 280], [60, 100]])
    pygame.draw.ellipse(screen, DARKGREEN, [[200, 285], [60, 100]])
    pygame.draw.ellipse(screen, DARKGREEN, [[235, 260], [60, 110]])
    pygame.draw.ellipse(screen, DARKGREEN, [[255, 250], [60, 130]])
    pygame.draw.ellipse(screen, DARKGREEN, [[270, 240], [70, 140]])
    pygame.draw.ellipse(screen, DARKGREEN, [[300, 250], [80, 140]])
    pygame.draw.ellipse(screen, DARKGREEN, [[340, 250], [70, 140]])
    pygame.draw.ellipse(screen, DARKGREEN, [[375, 260], [80, 150]])
    pygame.draw.ellipse(screen, DARKGREEN, [[395, 265], [80, 130]])
    pygame.draw.ellipse(screen, DARKGREEN, [[440, 280], [60, 110]])

    pygame.draw.polygon(screen, BROWN, ([10, 400], [20, 400], [15, 350]))
    pygame.draw.polygon(screen, BROWN, ([30, 400], [40, 400], [35, 370]))
    pygame.draw.polygon(screen, BROWN, ([40, 400], [50, 400], [45, 340]))
    pygame.draw.polygon(screen, BROWN, ([60, 400], [70, 400], [65, 360]))
    pygame.draw.polygon(screen, BROWN, ([80, 400], [90, 400], [85, 350]))
    pygame.draw.polygon(screen, BROWN, ([90, 400], [100, 400], [95, 380]))
    pygame.draw.polygon(screen, BROWN, ([120, 400], [130, 400], [125, 350]))
    pygame.draw.polygon(screen, BROWN, ([130, 400], [140, 400], [135, 330]))
    pygame.draw.polygon(screen, BROWN, ([140, 400], [150, 400], [145, 330]))
    pygame.draw.polygon(screen, BROWN, ([170, 400], [180, 400], [175, 320]))
    pygame.draw.polygon(screen, BROWN, ([190, 400], [200, 400], [195, 300]))
    pygame.draw.polygon(screen, BROWN, ([200, 400], [210, 400], [205, 290]))
    pygame.draw.polygon(screen, BROWN, ([220, 400], [230, 400], [225, 310]))
    pygame.draw.polygon(screen, BROWN, ([230, 400], [240, 400], [235, 300]))
    pygame.draw.polygon(screen, BROWN, ([260, 400], [270, 400], [265, 280]))
    pygame.draw.polygon(screen, BROWN, ([280, 400], [290, 400], [285, 290]))
    pygame.draw.polygon(screen, BROWN, ([300, 400], [310, 400], [305, 290]))
    pygame.draw.polygon(screen, BROWN, ([320, 400], [330, 400], [325, 280]))
    pygame.draw.polygon(screen, BROWN, ([340, 400], [350, 400], [345, 270]))
    pygame.draw.polygon(screen, BROWN, ([360, 400], [370, 400], [365, 280]))
    pygame.draw.polygon(screen, BROWN, ([380, 400], [390, 400], [385, 260]))
    pygame.draw.polygon(screen, BROWN, ([400, 400], [410, 400], [405, 270]))
    pygame.draw.polygon(screen, BROWN, ([420, 400], [430, 400], [425, 280]))
    pygame.draw.polygon(screen, BROWN, ([450, 400], [460, 400], [455, 290]))
    pygame.draw.polygon(screen, BROWN, ([470, 400], [480, 400], [475, 300]))

    pygame.draw.ellipse(screen, LAWNGREEN, [[-400, 350], [1700, 700]], 0)


main()
