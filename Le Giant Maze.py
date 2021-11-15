# SHREE GANESHAY NAMAH
# OM NAMAH SHIVAY

import sys
import pygame
from Game_Files.world import World
from Game_Files.player import Player
from Game_Files.camera import Camera

PLAYER_UP_KEY = pygame.K_w
PLAYER_RIGHT_KEY = pygame.K_d
PLAYER_DOWN_KEY = pygame.K_s
PLAYER_LEFT_KEY = pygame.K_a

pygame.init()

GAME_WINDOW = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption("Le Giant Maze")

GAME_CLOCK = pygame.time.Clock()

LE_GAME_WORLD = World()
LE_GUY = Player(LE_GAME_WORLD, PLAYER_UP_KEY, PLAYER_RIGHT_KEY,
                PLAYER_DOWN_KEY, PLAYER_LEFT_KEY)
LE_CAM = Camera(GAME_WINDOW, LE_GAME_WORLD, LE_GUY)

pygame.mixer.music.load("data/LeDamnAudio.ogg")


def main_game_loop() -> None:

    game_on = True
    end_game = pygame.USEREVENT
    pygame.mixer.music.set_endevent(end_game)

    while game_on:

        '''(I) Game Input'''

        for event in pygame.event.get():

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_ESCAPE:
                    game_on = False

            if event.type == end_game:
                game_on = False

        '''(II) Game Logic'''

        LE_GUY.movement()

        '''(III) Game Display & Sounds'''

        LE_CAM.display()

        pygame.display.flip()

        GAME_CLOCK.tick(60)

    pygame.quit()
    sys.exit()


main_game_loop()
