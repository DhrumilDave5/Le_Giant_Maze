import sys
import pygame
from Game_Files import simplemaze, colourcodes

MAZE_MATRIX_COLOUR_DICT = {0: colourcodes.COLOURS["world floor colour"],
                           1: colourcodes.COLOURS["world cave rock colour"],
                           2: colourcodes.COLOURS["player colour"],
                           3: colourcodes.COLOURS["world win area colour"]
                           }


def main() -> None:
    pygame.init()
    window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    pygame.display.set_caption("Maze Viewer")
    clock = pygame.time.Clock()
    quanta, maximum_quanta = 8, 16
    font = pygame.font.SysFont("couriernew", 36)
    window_on = True
    while window_on:
        for event_ in pygame.event.get():
            if event_.type == pygame.KEYDOWN:
                if event_.key == pygame.K_ESCAPE:
                    window_on = False
                if event_.key == pygame.K_UP and quanta < maximum_quanta:
                    quanta += 1
                if event_.key == pygame.K_DOWN and quanta > 1:
                    quanta -= 1
        window.fill((0, 0, 0))
        for i in range(len(simplemaze.MATRIX)):
            for j in range(len(simplemaze.MATRIX[i])):
                colour = MAZE_MATRIX_COLOUR_DICT[simplemaze.MATRIX[i][j]]
                pygame.draw.rect(window, colour,
                                 pygame.Rect(i * quanta, j * quanta,
                                             quanta, quanta))
        text = font.render("TPS: %d" % clock.get_fps(), True,
                           pygame.colordict.THECOLORS["white"])
        window.blit(text, (0, 0))
        pygame.display.flip()
        clock.tick()
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
