import sys
import pygame
import Game_Files.simplemaze as simplemaze
import Game_Files.maze as maze
from Game_Files.colourcodes import COLOURS

pygame.init()
WINDOW = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption("Maze Viewer")
CLOCK = pygame.time.Clock()


def draw_tps() -> None:
    font = pygame.font.SysFont("couriernew", 36)
    text = font.render("TPS: %d" % CLOCK.get_fps(), True,
                       pygame.colordict.THECOLORS["white"])
    WINDOW.blit(text, (0, 0))


def main(two_d_matrix: list[list], colour_dict: dict, quanta: int = 8) \
        -> None:
    window_on = True
    while window_on:
        for event_ in pygame.event.get():
            if event_.type == pygame.KEYDOWN:
                if event_.key == pygame.K_ESCAPE:
                    window_on = False
                if event_.key == pygame.K_UP and quanta < 16:
                    quanta += 1
                if event_.key == pygame.K_DOWN and quanta > 1:
                    quanta -= 1
        WINDOW.fill((0, 0, 0))
        for i in range(len(two_d_matrix)):
            for j in range(len(two_d_matrix[i])):
                pygame.draw.rect(WINDOW, colour_dict[two_d_matrix[i][j]],
                                 pygame.Rect(i * quanta, j * quanta,
                                             quanta, quanta))
        pygame.display.flip()
        CLOCK.tick(30)
    pygame.quit()
    sys.exit()


MAZE_MATRIX_COLOUR_DICT = {simplemaze.CONSTANTS["empty simple maze unit"]:
                           COLOURS["world floor colour"],
                           simplemaze.CONSTANTS["filled simple maze unit"]:
                           COLOURS["world cave rock colour"],
                           simplemaze.CONSTANTS
                               ["start point simple maze unit"]:
                           COLOURS["player colour"],
                           simplemaze.CONSTANTS
                               ["end point simple maze unit"]:
                           COLOURS["world win area colour"]
                           }
MAP_MATRIX_COLOUR_DICT = {maze.CONSTANTS["empty map unit"]:
                          COLOURS["world floor colour"],
                          maze.CONSTANTS["filled map unit"]:
                          COLOURS["world cave rock colour"]
                          }
main(maze.MAZE_MATRIX, MAP_MATRIX_COLOUR_DICT, 16)
