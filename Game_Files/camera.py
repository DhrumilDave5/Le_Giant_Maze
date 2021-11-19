import pygame
from Game_Files import maze, winarea, player, colourcodes


class Camera:

    def __init__(self, display_surface: pygame.Surface, world, player_to_follow):

        # DS: Display Surface
        self.DS = display_surface
        self.WORLD = world
        # PTF: Player To Follow
        self.PTF = player_to_follow

        # MU_DISPLAYED_X: Map Unit Displayed in X direction
        self.MU_DISPLAYED_X = (self.DS.get_width() // self.WORLD.MAP_UNIT_SIZE) + 1 + 1
        # MU_DISPLAYED_Y: Map Unit Displayed in Y direction
        self.MU_DISPLAYED_Y = (self.DS.get_height() // self.WORLD.MAP_UNIT_SIZE) + 1 + 1
        # In the above 2 lines, 1 is added two times because map units extruding partially
        # out of the screen have to be displayed on both the opposite edges of the screen
        # (if still don't get it, try adding 1 only one time and see what happens :P)

        self.EMPTY_MAP_UNIT_COLOUR_SHADES = \
            colourcodes.give_shades_list(colourcodes.COLOURS["world floor colour"])
        self.FILLED_MAP_UNIT_COLOUR_SHADES = \
            colourcodes.give_shades_list(colourcodes.COLOURS["world cave rock colour"])

        self.x = self.y = 0
        self.x_map_unit = self.x // self.WORLD.MAP_UNIT_SIZE
        self.y_map_unit = self.y // self.WORLD.MAP_UNIT_SIZE

    def move_cam_with_player(self) -> None:

        self.x = self.PTF.rect.centerx - self.DS.get_width() // 2
        self.y = self.PTF.rect.centery - self.DS.get_height() // 2
        self.x_map_unit = self.x // self.WORLD.MAP_UNIT_SIZE
        self.y_map_unit = self.y // self.WORLD.MAP_UNIT_SIZE

    def give_display_coords(self, x_coord: int, y_coord: int) -> tuple[int, int]:
        return x_coord - self.x, y_coord - self.y

    def display_light_hotspot(self, x_main: int, y_main: int, light_level_var: int) -> None:

        a = self.WORLD.MAP_UNIT_SIZE
        b = self.WORLD.MAP_UNIT_SIZE // 3
        c = maze.CONSTANTS["filled map unit"]
        d = self.FILLED_MAP_UNIT_COLOUR_SHADES

        '''Displaying main empty map unit'''
        tmp_coords = self.give_display_coords(x_main * a, y_main * a)
        tmp_colour = self.EMPTY_MAP_UNIT_COLOUR_SHADES[light_level_var]
        pygame.draw.rect(self.DS, tmp_colour, pygame.Rect(tmp_coords, (a, a)))

        top = (x_main, y_main - 1)
        right = (x_main + 1, y_main)
        bottom = (x_main, y_main + 1)
        left = (x_main - 1, y_main)
        top_map_unit = self.WORLD.MAP[top[0]][top[1]]
        right_map_unit = self.WORLD.MAP[right[0]][right[1]]
        bottom_map_unit = self.WORLD.MAP[bottom[0]][bottom[1]]
        left_map_unit = self.WORLD.MAP[left[0]][left[1]]

        '''
        Displaying filled map units as walls around main empty map unit,
        in the 8 if statements below
        '''

        if top_map_unit == c:
            x, y = top[0] * a, y_main * a - b
            tmp_coords = self.give_display_coords(x, y)
            pygame.draw.rect(self.DS, d[light_level_var],
                             pygame.Rect(tmp_coords, (a, b)))

        if right_map_unit == c:
            x, y = right[0] * a, right[1] * a
            tmp_coords = self.give_display_coords(x, y)
            pygame.draw.rect(self.DS, d[light_level_var],
                             pygame.Rect(tmp_coords, (b, a)))

        if bottom_map_unit == c:
            x, y = bottom[0] * a, bottom[1] * a
            tmp_coords = self.give_display_coords(x, y)
            pygame.draw.rect(self.DS, d[light_level_var],
                             pygame.Rect(tmp_coords, (a, b)))

        if left_map_unit == c:
            x, y = x_main * a - b, left[1] * a
            tmp_coords = self.give_display_coords(x, y)
            pygame.draw.rect(self.DS, d[light_level_var],
                             pygame.Rect(tmp_coords, (b, a)))

        if top_map_unit == c and right_map_unit == c:
            x, y = right[0] * a, y_main * a - b
            tmp_coords = self.give_display_coords(x, y)
            pygame.draw.rect(self.DS, d[light_level_var],
                             pygame.Rect(tmp_coords, (b, b)))

        if right_map_unit == c and bottom_map_unit == c:
            x, y = right[0] * a, bottom[1] * a
            tmp_coords = self.give_display_coords(x, y)
            pygame.draw.rect(self.DS, d[light_level_var],
                             pygame.Rect(tmp_coords, (b, b)))

        if bottom_map_unit == c and left_map_unit == c:
            x, y = x_main * a - b, bottom[1] * a
            tmp_coords = self.give_display_coords(x, y)
            pygame.draw.rect(self.DS, d[light_level_var],
                             pygame.Rect(tmp_coords, (b, b)))

        if left_map_unit == c and top_map_unit == c:
            x, y = x_main * a - b, y_main * a - b
            tmp_coords = self.give_display_coords(x, y)
            pygame.draw.rect(self.DS, d[light_level_var],
                             pygame.Rect(tmp_coords, (b, b)))

    def light_hotspot_logic(self) -> None:

        past_light_hotspots = []
        present_light_hotspots = [(self.PTF.cmu[0], self.PTF.cmu[1]), ]
        if self.PTF.win_area_display:
            present_light_hotspots.append((maze.CONSTANTS["win"][0] - 3,
                                           maze.CONSTANTS["win"][1]))
        future_light_hotspots = []

        if player.CONSTANTS["light level"] > 0:
            light_level = len(self.EMPTY_MAP_UNIT_COLOUR_SHADES) - player.CONSTANTS["light level"]
            if light_level < 0:
                light_level = 0
            for i in present_light_hotspots:
                self.display_light_hotspot(i[0], i[1], light_level)

        # Displaying map units distance by distance
        for i in range(player.CONSTANTS["light level"]):

            # Doing the light hotspot spreading logic
            for j in present_light_hotspots:

                top = (j[0], j[1] - 1)
                right = (j[0] + 1, j[1])
                bottom = (j[0], j[1] + 1)
                left = (j[0] - 1, j[1])
                top_map_unit = self.WORLD.MAP[top[0]][top[1]]
                right_map_unit = self.WORLD.MAP[right[0]][right[1]]
                bottom_map_unit = self.WORLD.MAP[bottom[0]][bottom[1]]
                left_map_unit = self.WORLD.MAP[left[0]][left[1]]

                a = maze.CONSTANTS["empty map unit"]
                if top_map_unit == a and top not in \
                        (past_light_hotspots + present_light_hotspots + future_light_hotspots):
                    future_light_hotspots.append(top)
                if right_map_unit == a and right not in \
                        (past_light_hotspots + present_light_hotspots + future_light_hotspots):
                    future_light_hotspots.append(right)
                if bottom_map_unit == a and bottom not in \
                        (past_light_hotspots + present_light_hotspots + future_light_hotspots):
                    future_light_hotspots.append(bottom)
                if left_map_unit == a and left not in \
                        (past_light_hotspots + present_light_hotspots + future_light_hotspots):
                    future_light_hotspots.append(left)

            '''Updating light hotspot lists after the logic'''
            past_light_hotspots += present_light_hotspots
            present_light_hotspots.clear()
            present_light_hotspots += future_light_hotspots
            future_light_hotspots.clear()

            for k in present_light_hotspots:  # Displaying map units after light hotspot logic

                light_level = i - (player.CONSTANTS["light level"]
                                   - len(self.EMPTY_MAP_UNIT_COLOUR_SHADES))
                if light_level < 0:
                    light_level = 0
                if k[0] in range(self.x_map_unit - 1, self.x_map_unit + self.MU_DISPLAYED_X) \
                        and k[1] in range(self.y_map_unit - 1, self.y_map_unit + self.MU_DISPLAYED_Y):
                    self.display_light_hotspot(k[0], k[1], light_level)

    def display_player(self) -> None:
        tmp_coords = self.give_display_coords(self.PTF.rect.x, self.PTF.rect.y)
        pygame.draw.rect(self.DS, colourcodes.COLOURS["player colour"],
                         pygame.Rect(tmp_coords, (self.PTF.SIZE, self.PTF.SIZE)))

    def display_win_area_unit(self, x_main: int, y_main: int) -> None:

        a = self.WORLD.MAP_UNIT_SIZE
        b = self.WORLD.MAP_UNIT_SIZE // 3
        c = maze.CONSTANTS["filled map unit"]
        d = colourcodes.COLOURS["world cave rock colour"]

        tmp_coords = self.give_display_coords(x_main * a, y_main * a)
        pygame.draw.rect(self.DS, colourcodes.COLOURS["world win area colour"],
                         pygame.Rect(tmp_coords, (a, a)))

        top = (x_main, y_main - 1)
        right = (x_main + 1, y_main)
        bottom = (x_main, y_main + 1)
        left = (x_main - 1, y_main)
        top_map_unit = self.WORLD.MAP[top[0]][top[1]]
        right_map_unit = self.WORLD.MAP[right[0]][right[1]]
        bottom_map_unit = self.WORLD.MAP[bottom[0]][bottom[1]]
        left_map_unit = self.WORLD.MAP[left[0]][left[1]]

        if top_map_unit == c:
            x, y = top[0] * a, y_main * a - b
            tmp_coords = self.give_display_coords(x, y)
            pygame.draw.rect(self.DS, d, pygame.Rect(tmp_coords, (a, b)))

        if right_map_unit == c:
            x, y = right[0] * a, right[1] * a
            tmp_coords = self.give_display_coords(x, y)
            pygame.draw.rect(self.DS, d, pygame.Rect(tmp_coords, (b, a)))

        if bottom_map_unit == c:
            x, y = bottom[0] * a, bottom[1] * a
            tmp_coords = self.give_display_coords(x, y)
            pygame.draw.rect(self.DS, d, pygame.Rect(tmp_coords, (a, b)))

        if left_map_unit == c:
            x, y = x_main * a - b, left[1] * a
            tmp_coords = self.give_display_coords(x, y)
            pygame.draw.rect(self.DS, d, pygame.Rect(tmp_coords, (b, a)))

        if top_map_unit == c and right_map_unit == c:
            x, y = right[0] * a, y_main * a - b
            tmp_coords = self.give_display_coords(x, y)
            pygame.draw.rect(self.DS, d, pygame.Rect(tmp_coords, (b, b)))

        if right_map_unit == c and bottom_map_unit == c:
            x, y = right[0] * a, bottom[1] * a
            tmp_coords = self.give_display_coords(x, y)
            pygame.draw.rect(self.DS, d, pygame.Rect(tmp_coords, (b, b)))

        if bottom_map_unit == c and left_map_unit == c:
            x, y = x_main * a - b, bottom[1] * a
            tmp_coords = self.give_display_coords(x, y)
            pygame.draw.rect(self.DS, d, pygame.Rect(tmp_coords, (b, b)))

        if left_map_unit == c and top_map_unit == c:
            x, y = x_main * a - b, y_main * a - b
            tmp_coords = self.give_display_coords(x, y)
            pygame.draw.rect(self.DS, d, pygame.Rect(tmp_coords, (b, b)))

    def display_win_area(self) -> None:
        for i in range(self.x_map_unit, self.x_map_unit + self.MU_DISPLAYED_X):
            if 0 <= i <= len(self.WORLD.MAP) - 1:
                for j in range(self.y_map_unit, self.y_map_unit + self.MU_DISPLAYED_Y):
                    if 0 <= j <= len(self.WORLD.MAP[i]) - 1:
                        if self.WORLD.MAP[i][j] == maze.CONSTANTS["empty map unit"]:
                            self.display_win_area_unit(i, j)

    def display_win_area_fake(self) -> None:
        a = self.WORLD.MAP_UNIT_SIZE
        b = self.WORLD.MAP_UNIT_SIZE // 3
        c = winarea.CONSTANTS["win area length"] // 10
        d = winarea.CONSTANTS["win area breadth"]

        x = self.WORLD.WIN_POSITION[0]
        y = self.WORLD.WIN_POSITION[1] - (d // 2)
        tmp_coords = self.give_display_coords(x * a, y * a)
        pygame.draw.rect(self.DS, colourcodes.COLOURS["world win area colour"],
                         pygame.Rect(tmp_coords, (c * a, d * a)))

        x = (self.WORLD.WIN_POSITION[0] * a) - b
        y = ((self.WORLD.WIN_POSITION[1] - (d // 2)) * a) - b
        h = (d // 2) * a + b
        tmp_coords = self.give_display_coords(x, y)
        pygame.draw.rect(self.DS, colourcodes.COLOURS["world cave rock colour"],
                         pygame.Rect(tmp_coords, (b, h)))

        x = (self.WORLD.WIN_POSITION[0] * a) - b
        y = (self.WORLD.WIN_POSITION[1] + 1) * a
        h = (d // 2) * a + b
        tmp_coords = self.give_display_coords(x, y)
        pygame.draw.rect(self.DS, colourcodes.COLOURS["world cave rock colour"],
                         pygame.Rect(tmp_coords, (b, h)))

        x = self.WORLD.WIN_POSITION[0] * a
        y = ((self.WORLD.WIN_POSITION[1] - (d // 2)) * a) - b
        w = c * a
        tmp_coords = self.give_display_coords(x, y)
        pygame.draw.rect(self.DS, colourcodes.COLOURS["world cave rock colour"],
                         pygame.Rect(tmp_coords, (w, b)))

        x = self.WORLD.WIN_POSITION[0] * a
        y = (self.WORLD.WIN_POSITION[1] + (d - (d // 2))) * a
        w = c * a
        tmp_coords = self.give_display_coords(x, y)
        pygame.draw.rect(self.DS, colourcodes.COLOURS["world cave rock colour"],
                         pygame.Rect(tmp_coords, (w, b)))

    def display_win_text(self) -> None:
        a = self.WORLD.WIN_TEXT
        b = self.WORLD.WIN_TEXT_POSITION
        c = self.WORLD.WIN_TEXT_UNIT_SIZE
        d = self.WORLD.MAP_UNIT_SIZE
        x_centre_correction = (d - (c * len(a[0][0]))) // 2
        y_centre_correction = (d - (c * len(a[0]))) // 2
        for i in range(len(a)):
            for j in range(len(a[i])):
                for k in range(len(a[i][j])):
                    if a[i][j][k] == 1:
                        letter_display_map_unit = (b[0] + i, b[1])
                        win_text_unit_x_coord = (letter_display_map_unit[0] * d) \
                            + (k * c) + x_centre_correction
                        win_text_unit_y_coord = (letter_display_map_unit[1] * d) \
                            + (j * c) + y_centre_correction
                        win_text_unit_tmp_coords = self.give_display_coords(win_text_unit_x_coord,
                                                                            win_text_unit_y_coord)
                        pygame.draw.rect(self.DS, colourcodes.COLOURS["world win text colour"],
                                         pygame.Rect(win_text_unit_tmp_coords, (c, c)))

    def display(self) -> None:

        """Basic algorithm for understanding light hotspot algorithm in Demos/lighthotspot.py"""

        self.DS.fill(colourcodes.COLOURS["world bg colour"])

        self.move_cam_with_player()

        if not self.PTF.won:
            self.light_hotspot_logic()
        else:
            self.display_win_area()

        if self.PTF.win_area_display:
            self.display_win_area_fake()

        self.display_player()

        if self.PTF.won:
            self.display_win_text()
