import pygame
import Game_Files.Settings as Settings


class Camera:

    def __init__(self, display_surface, maze, player_to_follow,
                 up_key, down_key, right_key, left_key):

        self.display_surface = display_surface
        self.maze = maze
        self.player_to_follow = player_to_follow

        self.x_pv, self.y_pv = 0, 0
        self.x_mv, self.y_mv = 0, 0
        self.xmu_pv = self.x_pv // Settings.mu_size_pv
        self.ymu_pv = self.y_pv // Settings.mu_size_pv
        self.xmu_mv = self.x_mv // Settings.mu_size_pv
        self.ymu_mv = self.y_mv // Settings.mu_size_pv

        self.player_view = True
        self.light_effects = True
        self.wa_display = False

        self.vel = Settings.mvlq

        self.up_key = up_key
        self.down_key = down_key
        self.right_key = right_key
        self.left_key = left_key

    def move_cam_with_player(self):

        self.x_pv = self.player_to_follow.rect.centerx - self.display_surface.get_width() // 2
        self.y_pv = self.player_to_follow.rect.centery - self.display_surface.get_height() // 2
        self.xmu_pv = self.x_pv // Settings.mu_size_pv
        self.ymu_pv = self.y_pv // Settings.mu_size_pv

    def give_display_coords_pv(self, x_coord, y_coord):
        return x_coord - self.x_pv, y_coord - self.y_pv

    def display_pv_without_light_effects(self):

        mus = Settings.mu_size_pv
        cd = Settings.colour_dict
        tdw = self.maze.text_during_win

        self.move_cam_with_player()

        for i in range(self.ymu_pv, self.ymu_pv + Settings.mu_displayed_y_pv):
            if 0 <= i <= len(self.maze.map) - 1:
                for j in range(self.xmu_pv, self.xmu_pv + Settings.mu_displayed_x_pv):
                    if 0 <= j <= len(self.maze.map[i]) - 1:
                        if not self.player_to_follow.won:
                            tmp_coords = self.give_display_coords_pv(j * mus, i * mus)
                            pygame.draw.rect(self.display_surface, cd[self.maze.map[i][j]],
                                             pygame.Rect(tmp_coords, (mus, mus)))
                        elif j >= 80 and i >= 26:   # Displaying only wamu
                            tmp_coords = self.give_display_coords_pv(j * mus, i * mus)
                            pygame.draw.rect(self.display_surface, cd[self.maze.map[i][j]],
                                             pygame.Rect(tmp_coords, (mus, mus)))

        p_tmp_coords = self.give_display_coords_pv(self.player_to_follow.rect.x, self.player_to_follow.rect.y)
        pygame.draw.rect(self.display_surface, self.player_to_follow.colour,
                         pygame.Rect(p_tmp_coords, (Settings.p_size, Settings.p_size)))

        for i in range(len(tdw)):
            for j in range(len(tdw[i])):
                for k in range(len(tdw[i][j])):
                    letter_display_mu = (Settings.win_text_mu[0] + i, Settings.win_text_mu[1])
                    tmp_coords = self.give_display_coords_pv((letter_display_mu[0] * mus) + (14 * k) + 25,
                                                             (letter_display_mu[1] * mus) + (14 * j))
                    if tdw[i][j][k] == 1:
                        pygame.draw.rect(self.display_surface, (0, 0, 0), pygame.Rect(tmp_coords, (14, 14)))

    def display_mu_stuff_for_light_effects(self, x_main, y_main, light_level_var):

        ds = self.display_surface
        mus = Settings.mu_size_pv
        o = Settings.mu_size_pv // 3
        emucs = Settings.empty_mu_colour_shades
        fmucs = Settings.filled_mu_colour_shades
        fmud = Settings.filled_mu_digit

        # Displaying main emu
        tmp_coords = self.give_display_coords_pv(x_main * mus, y_main * mus)
        tmp_colour = emucs[light_level_var]
        pygame.draw.rect(ds, tmp_colour, pygame.Rect(tmp_coords, (mus, mus)))

        top = (x_main, y_main - 1)
        right = (x_main + 1, y_main)
        bottom = (x_main, y_main + 1)
        left = (x_main - 1, y_main)
        top_mu = self.maze.map[top[1]][top[0]]
        right_mu = self.maze.map[right[1]][right[0]]
        bottom_mu = self.maze.map[bottom[1]][bottom[0]]
        left_mu = self.maze.map[left[1]][left[0]]

        # Displaying fmu around main emu, edges and corners

        if top_mu == fmud:
            x, y = top[0] * mus, (top[1] * mus) + (mus - o)
            tmp_coords = self.give_display_coords_pv(x, y)
            pygame.draw.rect(ds, fmucs[light_level_var], pygame.Rect(tmp_coords, (mus, o)))

        if right_mu == fmud:
            x, y = right[0] * mus, right[1] * mus
            tmp_coords = self.give_display_coords_pv(x, y)
            pygame.draw.rect(ds, fmucs[light_level_var], pygame.Rect(tmp_coords, (o, mus)))

        if bottom_mu == fmud:
            x, y = bottom[0] * mus, bottom[1] * mus
            tmp_coords = self.give_display_coords_pv(x, y)
            pygame.draw.rect(ds, fmucs[light_level_var], pygame.Rect(tmp_coords, (mus, o)))

        if left_mu == fmud:
            x, y = (left[0] * mus) + (mus - o), left[1] * mus
            tmp_coords = self.give_display_coords_pv(x, y)
            pygame.draw.rect(ds, fmucs[light_level_var], pygame.Rect(tmp_coords, (o, mus)))

        if top_mu == fmud and right_mu == fmud:
            x, y = (top[0] + 1) * mus, (top[1] * mus) + (mus - o)
            tmp_coords = self.give_display_coords_pv(x, y)
            pygame.draw.rect(ds, fmucs[light_level_var], pygame.Rect(tmp_coords, (o, o)))

        if right_mu == fmud and bottom_mu == fmud:
            x, y = right[0] * mus, (right[1] + 1) * mus
            tmp_coords = self.give_display_coords_pv(x, y)
            pygame.draw.rect(ds, fmucs[light_level_var], pygame.Rect(tmp_coords, (o, o)))

        if bottom_mu == fmud and left_mu == fmud:
            x, y = (bottom[0] * mus) - o, bottom[1] * mus
            tmp_coords = self.give_display_coords_pv(x, y)
            pygame.draw.rect(ds, fmucs[light_level_var], pygame.Rect(tmp_coords, (o, o)))

        if left_mu == fmud and top_mu == fmud:
            x, y = (left[0] * mus) + (mus - o), (left[1] * mus) - o
            tmp_coords = self.give_display_coords_pv(x, y)
            pygame.draw.rect(ds, fmucs[light_level_var], pygame.Rect(tmp_coords, (o, o)))

    def display_pv_with_light_effects(self):

        # Basic algorithm for understanding light hotspot algorithm in LightHotspotDemonstration.py
        # (The displaying for filled_mu around light hotspot is relatively easy to implement and thus not shown)

        ptf = self.player_to_follow
        ds = self.display_surface
        ps = Settings.p_size
        mus = Settings.mu_size_pv
        emucs = Settings.empty_mu_colour_shades
        emud = Settings.empty_mu_digit
        wamud = Settings.win_area_mu_digit

        self.move_cam_with_player()
        if ptf.y_cmu == 27 and 73 <= ptf.x_cmu <= 81:
            self.wa_display = True
        else:
            self.wa_display = False

        past_lh = []
        present_lh = [(ptf.x_cmu, ptf.y_cmu), ]
        if self.wa_display:
            present_lh.append((82, 27))
        future_lh = []

        if Settings.rd > 0:
            tmp_light_level = len(emucs) - Settings.render_distance
            if tmp_light_level < 0:
                tmp_light_level = 0
            self.display_mu_stuff_for_light_effects(ptf.x_cmu, ptf.y_cmu, tmp_light_level)

        # Displaying mu distance by distance
        for i in range(Settings.render_distance):

            # Doing the light hotspots logic
            for j in present_lh:

                top = (j[0], j[1] - 1)
                right = (j[0] + 1, j[1])
                bottom = (j[0], j[1] + 1)
                left = (j[0] - 1, j[1])
                top_mu = self.maze.map[top[1]][top[0]]
                right_mu = self.maze.map[right[1]][right[0]]
                bottom_mu = self.maze.map[bottom[1]][bottom[0]]
                left_mu = self.maze.map[left[1]][left[0]]

                if (top_mu == emud or top_mu == wamud) and top not in past_lh + present_lh + future_lh:
                    future_lh.append(top)
                if (right_mu == emud or right_mu == wamud) and right not in past_lh + present_lh + future_lh:
                    future_lh.append(right)
                if (bottom_mu == emud or bottom_mu == wamud) and bottom not in past_lh + present_lh + future_lh:
                    future_lh.append(bottom)
                if (left_mu == emud or left_mu == wamud) and left not in past_lh + present_lh + future_lh:
                    future_lh.append(left)

            # Updating lh lists after the logic
            past_lh += present_lh
            present_lh.clear()
            for k in future_lh:
                present_lh.append(k)
            future_lh.clear()

            # Displaying mu after the logic
            for m in present_lh:  # can't use 'for l in' as 'l' seems problematic acc to PyCharm

                light_level = i - (Settings.render_distance - len(emucs))
                if light_level < 0:
                    light_level = 0
                if self.maze.map[m[1]][m[0]] == Settings.empty_mu_digit:
                    self.display_mu_stuff_for_light_effects(m[0], m[1], light_level)

        if self.wa_display:
            for n in range(self.ymu_pv, self.ymu_pv + Settings.mu_displayed_y_pv):
                if 0 <= n <= len(self.maze.map) - 1:
                    for o in range(self.xmu_pv, self.xmu_pv + Settings.mu_displayed_x_pv):
                        if 0 <= o <= len(self.maze.map[n]) - 1:
                            if self.maze.map[n][o] == wamud:
                                tmp_coords = self.give_display_coords_pv(o * mus, n * mus)
                                pygame.draw.rect(ds, Settings.colour_dict[wamud], pygame.Rect(tmp_coords, (mus, mus)))

        p_tmp_coords = self.give_display_coords_pv(ptf.rect.x, ptf.rect.y)
        pygame.draw.rect(ds, ptf.colour, pygame.Rect(p_tmp_coords, (ps, ps)))

    def update_mu_stuff_mv(self):
        self.xmu_mv = self.x_mv // Settings.mvlq
        self.ymu_mv = self.y_mv // Settings.mvlq

    def move(self, key_list):
        down_limit = (self.maze.map_size[1] - Settings.mu_displayed_y_mv + 1) * Settings.mvlq
        right_limit = (self.maze.map_size[0] - Settings.mu_displayed_x_mv + 1) * Settings.mvlq
        if key_list[self.up_key] and self.y_mv > 0:
            self.y_mv -= self.vel
        if key_list[self.down_key] and self.y_mv < down_limit:
            self.y_mv += self.vel
        if key_list[self.right_key] and self.x_mv < right_limit:
            self.x_mv += self.vel
        if key_list[self.left_key] and self.x_mv > 0:
            self.x_mv -= self.vel

    def give_display_coords_mv(self, x_coord, y_coord):
        return x_coord - self.x_mv, y_coord - self.y_mv

    def display_mv(self, key_list):

        mus = Settings.mvlq
        cd = Settings.colour_dict

        self.move(key_list)
        self.update_mu_stuff_mv()

        for i in range(self.ymu_mv, self.ymu_mv + Settings.mu_displayed_y_mv):
            if 0 <= i <= len(self.maze.map) - 1:
                for j in range(self.xmu_mv, self.xmu_mv + Settings.mu_displayed_x_mv):
                    if 0 <= j <= len(self.maze.map[i]) - 1:
                        tmp_coords = self.give_display_coords_mv(j * mus, i * mus)
                        pygame.draw.rect(self.display_surface, cd[self.maze.map[i][j]],
                                         pygame.Rect(tmp_coords, (mus, mus)))

        p_tmp_coords = self.give_display_coords_mv(self.player_to_follow.x_cmu * mus, self.player_to_follow.y_cmu * mus)
        pygame.draw.rect(self.display_surface, self.player_to_follow.colour, pygame.Rect(p_tmp_coords, (mus, mus)))

    def display(self, key_list):

        self.display_surface.fill(Settings.world_BG_colour)

        if self.player_view:
            if self.light_effects and not self.player_to_follow.won:
                self.display_pv_with_light_effects()
            else:
                self.display_pv_without_light_effects()
        else:
            self.display_mv(key_list)
