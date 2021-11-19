import sys
import pygame


def draw_gradient(window: pygame.Surface, bg_colour: str,
                  square_size: int) -> pygame.Surface:
    tmp_surface = pygame.Surface((window.get_width(), window.get_height()))

    def give_tup(var) -> tuple[int, int, int]:
        if bg_colour == "red":
            tup = (var, 0, 0)
        elif bg_colour == "green":
            tup = (0, var, 0)
        elif bg_colour == "blue":
            tup = (0, 0, var)
        elif bg_colour == "white":
            tup = (var, var, var)
        else:
            tup = (0, 0, 0)
            print("Put some valid string in bg_colour argument of"
                  " draw_gradient(), try one of these: 'red', 'green',"
                  " 'blue', 'white'")
        return tup

    for i in range(256):
        for j in range(tmp_surface.get_width() // 256):
            x = (tmp_surface.get_width() // 256) * i + j
            pygame.PixelArray(tmp_surface)[:][x][:2 * square_size] = \
                tmp_surface.map_rgb(give_tup(i))

    return tmp_surface


def main() -> None:
    pygame.init()
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    clock = pygame.time.Clock()
    square_size = 100
    transparent_square = pygame.Rect(0, 0, square_size, square_size)
    bg_colours = ["red", "green", "blue", "white"]
    alpha = 127

    test_square_pair_color = pygame.colordict.THECOLORS["red"]
    s = pygame.Surface((square_size, square_size))
    s.set_alpha(alpha)
    s.fill(test_square_pair_color)

    def move(speed=2) -> None:
        if pygame.key.get_pressed()[pygame.K_RIGHT]:
            if transparent_square.x < (screen.get_width()
                                       - transparent_square.w):
                transparent_square.x += speed
        if pygame.key.get_pressed()[pygame.K_LEFT]:
            if transparent_square.x > 0:
                transparent_square.x -= speed

    def draw_transparent_square() -> None:
        screen.blit(s, (transparent_square.x, transparent_square.y))

    def draw_opaque_square() -> None:
        x = transparent_square.x
        y = transparent_square.y + transparent_square.h
        w = transparent_square.w
        h = transparent_square.h
        pygame.draw.rect(screen, test_square_pair_color,
                         pygame.Rect(x, y, w, h))

    def draw() -> None:
        draw_transparent_square()
        draw_opaque_square()

    def draw_fps() -> None:
        font = pygame.font.SysFont("couriernew", 24)
        text = font.render("FPS: %d  Press ARROW KEYS to move left & right,"
                           " see how the background colour mixes with"
                           " transparent surface"
                           % clock.get_fps(), True,
                           pygame.colordict.THECOLORS["white"])
        screen.blit(text, (0, 0))

    gradient_surface = draw_gradient(screen, bg_colours[2], square_size)
    win_on = True
    while win_on:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    win_on = False
        move()
        screen.blit(gradient_surface, (0, 0))
        draw_fps()
        draw()
        pygame.display.flip()
        clock.tick()
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
