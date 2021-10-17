import pygame
import os
import Game_Files.RGB_ColourCodes as RGB

lq = length_quanta = 5
mvlq = maze_view_length_quanta = 10

emud = empty_mu_digit = 0
fmud = filled_mu_digit = 1
wamud = win_area_mu_digit = 2
mu_size_pv = lq * 20
win_text_mu = (83, 29)

p_vel = lq
p_size = lq * 10
p_spawn_mu = (2, 27)
p_colour = RGB.dodger_blue_2nd_shade
p_up, p_down, p_right, p_left = pygame.K_w, pygame.K_s, pygame.K_d, pygame.K_a

pv_toggle_key = pygame.K_e
light_effects_toggle_key = pygame.K_q
cam_up, cam_down, cam_right, cam_left = pygame.K_UP, pygame.K_DOWN, pygame.K_RIGHT, pygame.K_LEFT
mu_displayed_x_pv = 17
mu_displayed_y_pv = 10
mu_displayed_x_mv = 154
mu_displayed_y_mv = 87


def give_shades_list(base_colour):
    shades_list = []
    for i in range(8):
        RGB_list = []
        for j in base_colour:
            RGB_list.append(j - (i * ((j + 1) // 8)))
        shades_list.append(RGB_list)
    return shades_list


emucs = empty_mu_colour_shades = give_shades_list(RGB.empty_mu_colour)
fmucs = filled_mu_colour_shades = give_shades_list(RGB.filled_mu_colour)
fmucs[-1] = [5, 5, 5]
wamucs = win_area_mu_colour_shades = give_shades_list(RGB.win_area_mu_colour)
cd = colour_dict = {emud: emucs[0], fmud: fmucs[0], wamud: wamucs[0]}

game_display_caption = "Le Giant Maze"
game_quit_key = pygame.K_ESCAPE
permissions = os.path.isdir("C:/Users/HP/PycharmProjects/Le_Giant_Maze_Project/Le_Giant_Maze/Le_Dev/")
TPS = 60
TPS_toggle_key = pygame.K_f
world_BG_colour = RGB.black
rd = render_distance = 0


'''
Below are short forms (which are made by me) used in code:
    mu = Maze Unit (used as a suffix with lots of other short forms)
    pv = Player View
    mv = Maze View
    p = Player
    lh = Light Hotspots
'''
