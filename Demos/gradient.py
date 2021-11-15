import sys
import pygame

pygame.init()
screen = pygame.display.set_mode((0, 0))
clock = pygame.time.Clock()
a = len(pygame.PixelArray(screen)[:])
print(a, len(pygame.PixelArray(screen)[:][0]))


def loop():

    screen.fill((255, 0, 0))
    for i in range(3):
        print(i + 1)
        for j in range(3):
            print(pygame.Surface.unmap_rgb(screen, pygame.PixelArray(screen)[:][i][j]), end=" ")
        print()
        clock.tick(1)
    pygame.quit()
    sys.exit()


def draw_gradient():

    win_on = True
    while win_on:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                win_on = False
        screen.fill((0, 0, 0))
        for y in range(255):
            pygame.PixelArray(screen)[:, y] = (y, y, y)
        pygame.display.update()
        clock.tick(10)
    pygame.quit()
    sys.exit()


# Remove the comment hash of the function calls below to run them
draw_gradient()
# loop()
