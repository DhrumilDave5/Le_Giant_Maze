# SHREE GANESHAY NAMAH
# OM NAMAH SHIVAY

import sys
import pygame
from Game_Files import world, player, camera


def main() -> None:

    pygame.init()

    game_window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    pygame.display.set_caption("Le Giant Maze")

    game_clock = pygame.time.Clock()

    le_game_world = world.World()
    le_guy = player.Player(le_game_world)
    le_cam = camera.Camera(game_window, le_game_world, le_guy)

    pygame.mixer.music.load("data/LeDamnAudio.ogg")

    game_on = True
    end_game = pygame.USEREVENT
    pygame.mixer.music.set_endevent(end_game)

    while game_on:

        '''(I) Game Input'''

        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                game_on = False

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_ESCAPE:
                    game_on = False

            if event.type == end_game:
                game_on = False

        '''(II) Game Logic'''

        le_guy.movement()

        '''(III) Game Display & Sounds'''

        le_cam.display()

        pygame.display.flip()

        game_clock.tick(60)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
