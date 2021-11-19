import sys
import pygame


def loop_through_pixelarray():

    pygame.init()
    window = pygame.display.set_mode((120, 12))
    # Minimum width of a pygame.Surface object is 120, whereas there is no
    # minimum limit for its height
    a = pygame.PixelArray(window)
    window.fill((255, 0, 0))
    for i in range(len(a[:])):
        print(i)
        for j in range(len(a[:][i])):
            print(j, ":", window.unmap_rgb(a[:][i][j]), end=" | ")
        print()
    pygame.quit()
    sys.exit()


def main() -> None:

    pygame.init()
    window = pygame.display.set_mode((0, 0))
    clock = pygame.time.Clock()
    a = len(pygame.PixelArray(window)[:])
    print(a, len(pygame.PixelArray(window)[:][0]))

    win_on = True
    while win_on:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    win_on = False
        window.fill((0, 0, 0))
        for i in range(255):
            pygame.PixelArray(window)[:, i] = (i, i, i)
        pygame.display.update()
        clock.tick(10)
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    loop_through_pixelarray()
