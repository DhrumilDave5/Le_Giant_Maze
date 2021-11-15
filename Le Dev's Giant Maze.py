# SHREE GANESHAY NAMAH
# OM NAMAH SHIVAY

import sys
import pygame
from Game_Files.world import World
from Game_Files.player import Player
from Game_Files.camera import Camera
from Le_Dev.devcam import DevCamera
from Le_Dev.wvcamera import WorldViewCamera

GAME_WINDOW_TITLE = "Le Giant Maze"
PLAYER_UP_KEY = pygame.K_w
PLAYER_RIGHT_KEY = pygame.K_d
PLAYER_DOWN_KEY = pygame.K_s
PLAYER_LEFT_KEY = pygame.K_a
WV_CAM_UP_KEY = pygame.K_UP
WV_CAM_RIGHT_KEY = pygame.K_RIGHT
WV_CAM_DOWN_KEY = pygame.K_DOWN
WV_CAM_LEFT_KEY = pygame.K_LEFT
WIN_MUSIC = "data/LeDamnAudio.ogg"

pygame.init()

GAME_WINDOW = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption(GAME_WINDOW_TITLE)

GAME_CLOCK = pygame.time.Clock()

LE_GAME_WORLD = World()
LE_GUY = Player(LE_GAME_WORLD, PLAYER_UP_KEY, PLAYER_RIGHT_KEY,
                PLAYER_DOWN_KEY, PLAYER_LEFT_KEY)
LE_CAM = Camera(GAME_WINDOW, LE_GAME_WORLD, LE_GUY)
LE_DEV_CAM = DevCamera(GAME_WINDOW, LE_GAME_WORLD, LE_GUY)
LE_WV_CAM = WorldViewCamera(GAME_WINDOW, LE_GAME_WORLD, LE_GUY)

pygame.mixer.music.load(WIN_MUSIC)

PLAYER_SPEED = 1


def option_toggle(var: bool) -> bool:
    if var:
        var = False
    elif not var:
        var = True
    return var


def speed_up():
    global PLAYER_SPEED
    max_speed_factor = 3
    if PLAYER_SPEED < (2 ** max_speed_factor):
        PLAYER_SPEED *= 2
    else:
        PLAYER_SPEED = 1
    return PLAYER_SPEED


def display_tps() -> None:
    font = pygame.font.SysFont("ocraextended", 36)
    text = font.render("TPS: %d" % GAME_CLOCK.get_fps(), True,
                       pygame.colordict.THECOLORS["white"])
    GAME_WINDOW.blit(text, (0, 0))


def detected(var: bool) -> None:
    font = pygame.font.SysFont("ocraextended", 400)
    bruh = font.render("BRUH", True, pygame.colordict.THECOLORS["green"])
    a = GAME_WINDOW
    if var:
        a.blit(bruh, ((a.get_width() - bruh.get_width()) // 2,
                      (a.get_height() - bruh.get_height()) // 2))


def main_game_loop() -> None:
    game_on = True
    world_view = False
    dev_view = False
    map_unit_borders = False

    while game_on:

        '''(I) Game Input'''

        for event in pygame.event.get():

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_ESCAPE:
                    game_on = False

                if event.key == pygame.K_e:
                    world_view = option_toggle(world_view)

                if event.key == pygame.K_q:
                    dev_view = option_toggle(dev_view)

                if event.key == pygame.K_r:
                    map_unit_borders = option_toggle(map_unit_borders)

                if event.key == pygame.K_f:
                    speed_up()

        '''(II) Game Logic'''

        for i in range(PLAYER_SPEED):
            LE_GUY.movement()

        '''(III) Game Display'''

        if world_view:
            LE_WV_CAM.display()
        elif dev_view:
            LE_DEV_CAM.display()
            if map_unit_borders:
                LE_DEV_CAM.display_map_unit_borders()
        else:
            LE_CAM.display()
            if map_unit_borders:
                LE_DEV_CAM.display_map_unit_borders()

        detected(pygame.key.get_pressed()[pygame.K_SPACE])

        display_tps()

        pygame.display.flip()

        GAME_CLOCK.tick(60)

    pygame.quit()
    sys.exit()


display_tps()
main_game_loop()
