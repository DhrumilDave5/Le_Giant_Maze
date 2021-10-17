# SHREE GANESHAY NAMAH
# OM NAMAH SHIVAY

import pygame
from pygame import mixer
import sys
import Game_Files.Settings as Settings
import Game_Files.MazeClass as MazeClass
import Game_Files.PlayerClass as PlayerClass
import Game_Files.CameraClass as CameraClass

pygame.init()

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption(Settings.game_display_caption)

game_clock = pygame.time.Clock()

leGameMaze = MazeClass.Maze()
leGuy = PlayerClass.Player(Settings.p_spawn_mu, Settings.p_colour, leGameMaze,
                           Settings.p_up, Settings.p_down, Settings.p_right, Settings.p_left)
leCam = CameraClass.Camera(screen, leGameMaze, leGuy,
                           Settings.cam_up, Settings.cam_down, Settings.cam_right, Settings.cam_left)

mixer.music.load("Game_Files/leDamnAudio.ogg")


def option_toggle(boolean_var):
    if boolean_var:
        boolean_var = False
    elif not boolean_var:
        boolean_var = True
    return boolean_var


def main_game_loop():

    game_on = True
    limited_TPS = True
    win_music_played = False

    unlimited_TPS_permission = Settings.permissions
    mv_permission = Settings.permissions
    toggle_light_effects_permission = Settings.permissions

    while game_on:

        '''(I) Game Input'''

        for event in pygame.event.get():

            if event.type == pygame.KEYDOWN:

                if event.key == Settings.game_quit_key:
                    game_on = False

                if unlimited_TPS_permission:
                    if event.key == Settings.TPS_toggle_key:
                        limited_TPS = option_toggle(limited_TPS)

                if mv_permission:
                    if event.key == Settings.pv_toggle_key:
                        leCam.player_view = option_toggle(leCam.player_view)

                if toggle_light_effects_permission:
                    if event.key == Settings.light_effects_toggle_key:
                        leCam.light_effects = option_toggle(leCam.light_effects)

        keys = pygame.key.get_pressed()

        '''(II) Game Logic'''

        leGuy.movement(keys)

        if leGuy.won and not win_music_played:
            pygame.mixer.music.play()
            win_music_played = True

        '''(III) Game Display'''

        leCam.display(keys)

        pygame.display.update()

        if limited_TPS:
            game_clock.tick(Settings.TPS)
        else:
            game_clock.tick()

    pygame.quit()
    sys.exit()


main_game_loop()
