import sys
import pygame
from Game_Files import maze, map
from Game_Files.colourcodes import COLOURS

MAZE_MATRIX_COLOUR_DICT = \
    {map.CONSTANTS["empty map unit"]: COLOURS["world floor"],
     map.CONSTANTS["filled map unit"]: COLOURS["world cave rock"],
     map.CONSTANTS["player spawn map unit"]: COLOURS["player"],
     map.CONSTANTS["win map unit"]: COLOURS["world win area"]
     }


def main(two_d_matrix: list[list[int]]) -> None:
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
        for i in range(len(two_d_matrix)):
            for j in range(len(two_d_matrix[i])):
                colour = MAZE_MATRIX_COLOUR_DICT[two_d_matrix[i][j]]
                rect = pygame.Rect(i * quanta, j * quanta, quanta, quanta)
                pygame.draw.rect(window, colour, rect)
        text = font.render("TPS: %d" % clock.get_fps(), True,
                           pygame.colordict.THECOLORS["white"])
        window.blit(text, (0, 0))
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main(map.create_maze_map(maze.MAZE))
