import pygame
from math import radians, sin, cos

SIZE = (900, 700)
WINDOW_NAME = "Animation"

LAWNGREEN = (0, 223, 0)
DARKTURQUOSE = (0, 171, 255)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
GRAY = (105, 105, 105)
BROWN = (128, 87, 0)
DARKGREEN = (22, 100, 0)


def main():
    pygame.init()
    screen = pygame.display.set_mode(SIZE)
    pygame.display.set_caption(WINDOW_NAME)
    done = False
    clock = pygame.time.Clock()
    a0 = 1

    sun_pos = [40, 40]
    cloud11_pos = [900, 15]
    cloud12_pos = [860, 10]
    cloud13_pos = [820, 15]

    cloud21_pos = [900, 100]
    cloud22_pos = [860, 90]
    cloud23_pos = [820, 100]

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        pygame.draw.rect(screen, DARKTURQUOSE, [[0, 0], [900, 700]], 0)

        pygame.draw.circle(screen, YELLOW, sun_pos, 30)

        pygame.draw.ellipse(screen, DARKGREEN, [[-10, 330], [50, 80]])

        pygame.draw.polygon(screen, GRAY, ([500, 400], [900, 400], [700, 100]))
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

        pygame.draw.ellipse(screen, LAWNGREEN, [[-400, 350], [1700, 700]],  0)

        pygame.draw.ellipse(screen, WHITE, [cloud11_pos, [80, 60]], 0)
        pygame.draw.ellipse(screen, WHITE, [cloud12_pos, [80, 70]], 0)
        pygame.draw.ellipse(screen, WHITE, [cloud13_pos, [80, 60]], 0)

        pygame.draw.ellipse(screen, WHITE, [cloud21_pos, [80, 60]], 0)
        pygame.draw.ellipse(screen, WHITE, [cloud22_pos, [80, 80]], 0)
        pygame.draw.ellipse(screen, WHITE, [cloud23_pos, [80, 60]], 0)
        cloud11_pos[0] -= 8
        cloud12_pos[0] -= 8
        cloud13_pos[0] -= 8

        cloud21_pos[0] -= 6
        cloud22_pos[0] -= 6
        cloud23_pos[0] -= 6

        sun_pos[0] += int(3 * cos(a0))
        sun_pos[1] += int(3 * sin(a0))
        a0 += 0.0000005
        clock.tick(15)

        pygame.display.flip()

    pygame.quit()


main()
