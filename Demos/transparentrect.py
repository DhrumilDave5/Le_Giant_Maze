import sys
import pygame

pygame.init()
SCREEN = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
CLOCK = pygame.time.Clock()
SQUARE_SIZE = 100
TRANSPARENT_SQUARE = pygame.Rect(0, 0, SQUARE_SIZE, SQUARE_SIZE)
BG_COLORS = ["red", "green", "blue", "white"]
BG_COLOR_IN_GRADIENT = BG_COLORS[2]
ALPHA = 127
SPEED = 2
FONT = pygame.font.SysFont("couriernew", 24)


TEST_SQUARE_PAIR_COLOR = pygame.colordict.THECOLORS["red"]
S = pygame.Surface((SQUARE_SIZE, SQUARE_SIZE))
S.set_alpha(ALPHA)
S.fill(TEST_SQUARE_PAIR_COLOR)


def move() -> None:
    if pygame.key.get_pressed()[pygame.K_RIGHT] \
            and TRANSPARENT_SQUARE.x < (SCREEN.get_width() - TRANSPARENT_SQUARE.w):
        TRANSPARENT_SQUARE.x += SPEED
    if pygame.key.get_pressed()[pygame.K_LEFT] and TRANSPARENT_SQUARE.x > 0:
        TRANSPARENT_SQUARE.x -= SPEED


def draw_transparent_square() -> None:
    SCREEN.blit(S, (TRANSPARENT_SQUARE.x, TRANSPARENT_SQUARE.y))


def draw_opaque_square() -> None:
    pygame.draw.rect(SCREEN, TEST_SQUARE_PAIR_COLOR,
                     pygame.Rect(TRANSPARENT_SQUARE.x,
                                 TRANSPARENT_SQUARE.y + TRANSPARENT_SQUARE.h,
                                 TRANSPARENT_SQUARE.w,
                                 TRANSPARENT_SQUARE.h
                                 )
                     )


def draw() -> None:
    draw_transparent_square()
    draw_opaque_square()


def draw_fps() -> None:
    text = FONT.render("FPS: %d  Press ARROW KEYS to move left & right" % CLOCK.get_fps(),
                       True,
                       pygame.colordict.THECOLORS["white"])
    SCREEN.blit(text, (0, 0))


def draw_gradient() -> pygame.Surface:
    tmp_surface = pygame.Surface((SCREEN.get_width(), SCREEN.get_height()))

    def give_tup(var) -> tuple[int, int, int]:
        if BG_COLOR_IN_GRADIENT == "red":
            tup = (var, 0, 0)
        elif BG_COLOR_IN_GRADIENT == "green":
            tup = (0, var, 0)
        elif BG_COLOR_IN_GRADIENT == "blue":
            tup = (0, 0, var)
        elif BG_COLOR_IN_GRADIENT == "white":
            tup = (var, var, var)
        else:
            tup = (0, 0, 0)
            print("Put some valid string in BG_COLOR_IN_GRADIENT, try one of these: 'red', 'green', 'blue', 'white'")
        return tup
    for i in range(256):
        for j in range(tmp_surface.get_width() // 256):
            pygame.PixelArray(tmp_surface)[:][(tmp_surface.get_width() // 256) * i + j][:2 * SQUARE_SIZE] = \
                tmp_surface.map_rgb(give_tup(i))

    return tmp_surface


def main() -> None:

    gradient_surface = draw_gradient()
    win_on = True
    while win_on:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                win_on = False
        move()
        SCREEN.blit(gradient_surface, (0, 0))
        draw_fps()
        draw()
        pygame.display.flip()
        CLOCK.tick()
    pygame.quit()
    sys.exit()


main()
