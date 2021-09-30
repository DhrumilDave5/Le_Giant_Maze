import pygame
import os
import Game_Files.RGB_ColourCodes as RGB_ColourCodes

game_display_caption = "Le Giant Maze"  # Not to be changed
game_quit_key = pygame.K_ESCAPE
permissions = os.path.isdir("C:/Users/HP/PycharmProjects/Le_Giant_Maze_Project/Le_Giant_Maze/Le_Dev/")
TPS = 60
TPS_toggle_key = pygame.K_f
world_BG_colour = RGB_ColourCodes.black

pv_toggle_key = pygame.K_e
light_effects_toggle_key = pygame.K_q
render_distance = 8
omega = filled_maze_unit_edge_slice_display_size = 33
cam_vel = 10    # Not to be changed
cam_up, cam_down, cam_right, cam_left = pygame.K_UP, pygame.K_DOWN, pygame.K_RIGHT, pygame.K_LEFT
mu_displayed_x_pv = 17
mu_displayed_y_pv = 10
mu_displayed_x_mv = 154
mu_displayed_y_mv = 87

p_vel = 5  # Not to be changed
p_size = p_vel * 10  # 10 * x
p1_spawn_mu = (2, 27)
p1_colour = (23, 107, 191)  # 2nd Shade of Dodger Blue
p1_up, p1_down, p1_right, p1_left = pygame.K_w, pygame.K_s, pygame.K_d, pygame.K_a
p2_spawn_mu = (-1, -1)

mu_size_pv = p_size * 2  # Not to be changed
mu_size_mv = cam_vel
empty_mu_digit = 0
filled_mu_digit = 1
win_area_mu_digit = 2
win_text_mu = (83, 29)


def give_shades_list(base_colour):
    shades_list = []
    for i in range(8):
        RGB_list = []
        for j in base_colour:
            RGB_list.append(j - (i * ((j + 1) // 8)))
        shades_list.append(RGB_list)
    return shades_list


empty_mu_colour_shades = give_shades_list((159, 79, 47))
filled_mu_colour_shades = give_shades_list((31, 31, 31))
filled_mu_colour_shades[-1] = [5, 5, 5]
win_area_mu_colour_shades = give_shades_list((255, 215, 31))
colour_dict = {empty_mu_digit: empty_mu_colour_shades[0],
               filled_mu_digit: filled_mu_colour_shades[0],
               win_area_mu_digit: win_area_mu_colour_shades[0]
               }

'''
Below are short forms (which are made by me) used in code:
    mu = Maze Unit
    tlmu = Top Left 'mu'
    trmu = Top Left 'mu'
    blmu = Bottom Left 'mu'
    brmu = Bottom Right 'mu'
    cmu = Center 'mu'
    pv = Player View
    mv = Maze View
    p = Player
    lh = Light Hotspots
    wa = Winning Area
'''
