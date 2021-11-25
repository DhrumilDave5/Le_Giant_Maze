import pygame
from Game_Files.colourcodes import COLOURS


def give_shades_list(base_colour: tuple[int]) -> tuple[tuple[int]]:
    shades_list = []
    for i in range(8):
        rgb_list = []
        for j in base_colour:
            x = j - (i * ((j + 1) // 8))
            # j- 1, because range of integers used to describe in RGB is
            # 0-255 and not 1-256
            if x < 5:  # (0, 0, 0) to (4, 4, 4) is almost invisible
                x = 5
            rgb_list.append(x)
        shades_list.append(tuple(rgb_list))
    return tuple(shades_list)


class Camera:

    def __init__(self, display_surface: pygame.Surface, world,
                 player_to_follow):

        self.DISPLAY_SURFACE = display_surface
        self.WORLD = world
        self.PLAYER_TO_FOLLOW = player_to_follow

        tmp = self.DISPLAY_SURFACE.get_width()
        # MU_DISPLAYED_X: Map Units Displayed in X direction
        self.MU_DISPLAYED_X = (tmp // self.WORLD.MAP_UNIT_SIZE) + 2
        tmp = self.DISPLAY_SURFACE.get_height()
        # MU_DISPLAYED_Y: Map Units Displayed in Y direction
        self.MU_DISPLAYED_Y = (tmp // self.WORLD.MAP_UNIT_SIZE) + 2
        # In the above 2 lines, 2 is added because map units extruding
        # partially out of the screen have to be displayed on both the
        # opposite edges of the screen (if still don't get it, try adding
        # removing the  :P)

        tmp = self.WORLD.MAP_UNIT_SIZE
        tmp2 = self.WORLD.WIN_TEXT_UNIT_SIZE
        self.text_x_centre_correction = \
            (tmp - (tmp2 * len(self.WORLD.WIN_TEXT[0][0]))) // 2
        self.text_y_centre_correction = \
            (tmp - (tmp2 * len(self.WORLD.WIN_TEXT[0]))) // 2

        self.EMPTY_MAP_UNIT_COLOUR_SHADES = \
            give_shades_list(COLOURS["world floor"])
        self.FILLED_MAP_UNIT_COLOUR_SHADES = \
            give_shades_list(COLOURS["world cave rock"])

        self.x = self.y = 0
        self.x_map_unit = self.x // self.WORLD.MAP_UNIT_SIZE
        self.y_map_unit = self.y // self.WORLD.MAP_UNIT_SIZE

    def draw_rect(self, x_and_y, width_and_height, colour) -> None:
        rect = pygame.Rect(x_and_y, width_and_height)
        pygame.draw.rect(self.DISPLAY_SURFACE, colour, rect)

    def move_cam_with_player(self) -> None:

        self.x = self.PLAYER_TO_FOLLOW.rect.centerx \
            - (self.DISPLAY_SURFACE.get_width() // 2)
        self.y = self.PLAYER_TO_FOLLOW.rect.centery \
            - (self.DISPLAY_SURFACE.get_height() // 2)
        self.x_map_unit = self.x // self.WORLD.MAP_UNIT_SIZE
        self.y_map_unit = self.y // self.WORLD.MAP_UNIT_SIZE

    def give_display_coords(self, x_coord: int, y_coord: int) \
            -> tuple[int, int]:
        return x_coord - self.x, y_coord - self.y

    def display_light_hotspot(self, x_main: int, y_main: int,
                              light_level_var: int) -> None:

        a = self.WORLD.MAP_UNIT_SIZE
        b = self.WORLD.MAP_UNIT_SIZE // 3
        c = self.WORLD.MAP_UNITS["filled"]
        d = self.FILLED_MAP_UNIT_COLOUR_SHADES

        '''Displaying main empty map unit'''
        tmp_coords = self.give_display_coords(x_main * a, y_main * a)
        tmp_colour = self.EMPTY_MAP_UNIT_COLOUR_SHADES[light_level_var]
        self.draw_rect(tmp_coords, (a, a), tmp_colour)

        top = (x_main, y_main - 1)
        right = (x_main + 1, y_main)
        bottom = (x_main, y_main + 1)
        left = (x_main - 1, y_main)
        top_map_unit = self.WORLD.map[top[0]][top[1]]
        right_map_unit = self.WORLD.map[right[0]][right[1]]
        bottom_map_unit = self.WORLD.map[bottom[0]][bottom[1]]
        left_map_unit = self.WORLD.map[left[0]][left[1]]

        '''Displaying filled map units as walls around main empty map unit,
        in the 8 if statements below
        '''

        if top_map_unit == c:
            x, y = top[0] * a, y_main * a - b
            tmp_coords = self.give_display_coords(x, y)
            self.draw_rect(tmp_coords, (a, b), d[light_level_var])

        if right_map_unit == c:
            x, y = right[0] * a, right[1] * a
            tmp_coords = self.give_display_coords(x, y)
            self.draw_rect(tmp_coords, (b, a), d[light_level_var])

        if bottom_map_unit == c:
            x, y = bottom[0] * a, bottom[1] * a
            tmp_coords = self.give_display_coords(x, y)
            self.draw_rect(tmp_coords, (a, b), d[light_level_var])

        if left_map_unit == c:
            x, y = x_main * a - b, left[1] * a
            tmp_coords = self.give_display_coords(x, y)
            self.draw_rect(tmp_coords, (b, a), d[light_level_var])

        if top_map_unit == c and right_map_unit == c:
            x, y = right[0] * a, y_main * a - b
            tmp_coords = self.give_display_coords(x, y)
            self.draw_rect(tmp_coords, (b, b), d[light_level_var])

        if right_map_unit == c and bottom_map_unit == c:
            x, y = right[0] * a, bottom[1] * a
            tmp_coords = self.give_display_coords(x, y)
            self.draw_rect(tmp_coords, (b, b), d[light_level_var])

        if bottom_map_unit == c and left_map_unit == c:
            x, y = x_main * a - b, bottom[1] * a
            tmp_coords = self.give_display_coords(x, y)
            self.draw_rect(tmp_coords, (b, b), d[light_level_var])

        if left_map_unit == c and top_map_unit == c:
            x, y = x_main * a - b, y_main * a - b
            tmp_coords = self.give_display_coords(x, y)
            self.draw_rect(tmp_coords, (b, b), d[light_level_var])

    def light_hotspot_logic(self) -> None:

        """Basic algorithm for understanding light hotspot algorithm
        in Demos/lighthotspot.py
        """

        past_light_hotspots = []
        present_light_hotspots = [(self.PLAYER_TO_FOLLOW.cmu[0],
                                   self.PLAYER_TO_FOLLOW.cmu[1]), ]
        win_area_light_hotspot_position = -3
        if self.PLAYER_TO_FOLLOW.win_area_display:
            win_area_light_hotspot_x = self.WORLD.WIN_POSITION[0] \
                + win_area_light_hotspot_position
            win_area_light_hotspot_y = self.WORLD.WIN_POSITION[1]
            tmp = (win_area_light_hotspot_x, win_area_light_hotspot_y)
            present_light_hotspots.append(tmp)
        future_light_hotspots = []

        if self.PLAYER_TO_FOLLOW.LIGHT_LEVEL > 0:
            light_level = len(self.EMPTY_MAP_UNIT_COLOUR_SHADES) \
                          - self.PLAYER_TO_FOLLOW.LIGHT_LEVEL
            if light_level < 0:
                light_level = 0
            for i in present_light_hotspots:
                self.display_light_hotspot(i[0], i[1], light_level)

        # Displaying map units distance by distance
        for i in range(self.PLAYER_TO_FOLLOW.LIGHT_LEVEL):

            # Doing the light hotspot spreading logic
            for j in present_light_hotspots:

                top = (j[0], j[1] - 1)
                right = (j[0] + 1, j[1])
                bottom = (j[0], j[1] + 1)
                left = (j[0] - 1, j[1])
                top_map_unit = self.WORLD.map[top[0]][top[1]]
                right_map_unit = self.WORLD.map[right[0]][right[1]]
                bottom_map_unit = self.WORLD.map[bottom[0]][bottom[1]]
                left_map_unit = self.WORLD.map[left[0]][left[1]]

                a = self.WORLD.MAP_UNITS["empty"]
                b = past_light_hotspots
                c = present_light_hotspots
                d = future_light_hotspots
                if top_map_unit == a and top not in (b + c + d):
                    future_light_hotspots.append(top)
                if right_map_unit == a and right not in (b + c + d):
                    future_light_hotspots.append(right)
                if bottom_map_unit == a and bottom not in (b + c + d):
                    future_light_hotspots.append(bottom)
                if left_map_unit == a and left not in (b + c + d):
                    future_light_hotspots.append(left)

            '''Updating light hotspot lists after the logic'''
            past_light_hotspots += present_light_hotspots
            present_light_hotspots.clear()
            present_light_hotspots += future_light_hotspots
            future_light_hotspots.clear()

            for k in present_light_hotspots:
                # Displaying map units after light hotspot logic

                tmp = len(self.EMPTY_MAP_UNIT_COLOUR_SHADES)
                light_level = i - (self.PLAYER_TO_FOLLOW.LIGHT_LEVEL - tmp)
                if light_level < 0:
                    light_level = 0
                x_minimum = self.x_map_unit - 1
                y_minimum = self.y_map_unit - 1
                # -1 in above 2 lines because the walls of light hotspots
                # out of window can have their walls inside the window
                x_maximum = self.x_map_unit + self.MU_DISPLAYED_X
                y_maximum = self.y_map_unit + self.MU_DISPLAYED_Y
                if k[0] in range(x_minimum, x_maximum) \
                        and k[1] in range(y_minimum, y_maximum):
                    self.display_light_hotspot(k[0], k[1], light_level)

    def display_player(self) -> None:
        tmp_coords = self.give_display_coords(self.PLAYER_TO_FOLLOW.rect.x,
                                              self.PLAYER_TO_FOLLOW.rect.y)
        tmp = (self.PLAYER_TO_FOLLOW.SIZE, self.PLAYER_TO_FOLLOW.SIZE)
        self.draw_rect(tmp_coords, tmp, COLOURS["player"])

    def display_win_area_unit(self, x_main: int, y_main: int) -> None:

        a = self.WORLD.MAP_UNIT_SIZE
        b = self.WORLD.MAP_UNIT_SIZE // 3
        c = self.WORLD.MAP_UNITS["filled"]

        tmp_coords = self.give_display_coords(x_main * a, y_main * a)
        self.draw_rect(tmp_coords, (a, a), COLOURS["world win area"])

        top = (x_main, y_main - 1)
        right = (x_main + 1, y_main)
        bottom = (x_main, y_main + 1)
        left = (x_main - 1, y_main)
        top_map_unit = self.WORLD.map[top[0]][top[1]]
        right_map_unit = self.WORLD.map[right[0]][right[1]]
        bottom_map_unit = self.WORLD.map[bottom[0]][bottom[1]]
        left_map_unit = self.WORLD.map[left[0]][left[1]]

        if top_map_unit == c:
            x, y = top[0] * a, y_main * a - b
            tmp_coords = self.give_display_coords(x, y)
            self.draw_rect(tmp_coords, (a, b), COLOURS["world cave rock"])

        if right_map_unit == c:
            x, y = right[0] * a, right[1] * a
            tmp_coords = self.give_display_coords(x, y)
            self.draw_rect(tmp_coords, (b, a), COLOURS["world cave rock"])

        if bottom_map_unit == c:
            x, y = bottom[0] * a, bottom[1] * a
            tmp_coords = self.give_display_coords(x, y)
            self.draw_rect(tmp_coords, (a, b), COLOURS["world cave rock"])

        if left_map_unit == c:
            x, y = x_main * a - b, left[1] * a
            tmp_coords = self.give_display_coords(x, y)
            self.draw_rect(tmp_coords, (b, a), COLOURS["world cave rock"])

        if top_map_unit == c and right_map_unit == c:
            x, y = right[0] * a, y_main * a - b
            tmp_coords = self.give_display_coords(x, y)
            self.draw_rect(tmp_coords, (b, b), COLOURS["world cave rock"])

        if right_map_unit == c and bottom_map_unit == c:
            x, y = right[0] * a, bottom[1] * a
            tmp_coords = self.give_display_coords(x, y)
            self.draw_rect(tmp_coords, (b, b), COLOURS["world cave rock"])

        if bottom_map_unit == c and left_map_unit == c:
            x, y = x_main * a - b, bottom[1] * a
            tmp_coords = self.give_display_coords(x, y)
            self.draw_rect(tmp_coords, (b, b), COLOURS["world cave rock"])

        if left_map_unit == c and top_map_unit == c:
            x, y = x_main * a - b, y_main * a - b
            tmp_coords = self.give_display_coords(x, y)
            self.draw_rect(tmp_coords, (b, b), COLOURS["world cave rock"])

    def display_win_area(self) -> None:
        x_minimum = self.x_map_unit
        y_minimum = self.y_map_unit
        x_maximum = self.x_map_unit + self.MU_DISPLAYED_X
        y_maximum = self.y_map_unit + self.MU_DISPLAYED_Y
        for i in range(x_minimum, x_maximum):
            if 0 <= i <= len(self.WORLD.map) - 1:
                for j in range(y_minimum, y_maximum):
                    if 0 <= j <= len(self.WORLD.map[i]) - 1:
                        if self.WORLD.map[i][j] == \
                                self.WORLD.MAP_UNITS["empty"]:
                            self.display_win_area_unit(i, j)

    def display_win_area_fake(self) -> None:
        a = self.WORLD.MAP_UNIT_SIZE
        b = self.WORLD.MAP_UNIT_SIZE // 3
        c = self.WORLD.WIN_AREA_LENGTH // 10
        d = self.WORLD.WIN_AREA_BREADTH

        x = self.WORLD.WIN_POSITION[0]
        y = self.WORLD.WIN_POSITION[1] - (d // 2)
        tmp_coords = self.give_display_coords(x * a, y * a)
        self.draw_rect(tmp_coords, (c * a, d * a),
                       COLOURS["world win area"])

        x = (self.WORLD.WIN_POSITION[0] * a) - b
        y = ((self.WORLD.WIN_POSITION[1] - (d // 2)) * a) - b
        h = (d // 2) * a + b
        tmp_coords = self.give_display_coords(x, y)
        self.draw_rect(tmp_coords, (b, h), COLOURS["world cave rock"])

        x = (self.WORLD.WIN_POSITION[0] * a) - b
        y = (self.WORLD.WIN_POSITION[1] + 1) * a
        h = (d // 2) * a + b
        tmp_coords = self.give_display_coords(x, y)
        self.draw_rect(tmp_coords, (b, h), COLOURS["world cave rock"])

        x = self.WORLD.WIN_POSITION[0] * a
        y = ((self.WORLD.WIN_POSITION[1] - (d // 2)) * a) - b
        w = c * a
        tmp_coords = self.give_display_coords(x, y)
        self.draw_rect(tmp_coords, (w, b), COLOURS["world cave rock"])

        x = self.WORLD.WIN_POSITION[0] * a
        y = (self.WORLD.WIN_POSITION[1] + (d - (d // 2))) * a
        w = c * a
        tmp_coords = self.give_display_coords(x, y)
        self.draw_rect(tmp_coords, (w, b), COLOURS["world cave rock"])

    def display_text_unit(self, letter_index, text_unit_row_index,
                          text_unit_column_index):
        tmp = self.WORLD.WIN_TEXT_POSITION
        letter_display_map_unit = (tmp[0] + letter_index, tmp[1])
        text_unit_x_coord = \
            (letter_display_map_unit[0] * self.WORLD.MAP_UNIT_SIZE) \
            + (text_unit_column_index * self.WORLD.WIN_TEXT_UNIT_SIZE) \
            + self.text_x_centre_correction
        text_unit_y_coord = \
            (letter_display_map_unit[1] * self.WORLD.MAP_UNIT_SIZE) \
            + (text_unit_row_index * self.WORLD.WIN_TEXT_UNIT_SIZE) \
            + self.text_y_centre_correction
        text_unit_tmp_coords = \
            self.give_display_coords(text_unit_x_coord, text_unit_y_coord)
        text_unit_size = (self.WORLD.WIN_TEXT_UNIT_SIZE,
                          self.WORLD.WIN_TEXT_UNIT_SIZE)
        self.draw_rect(text_unit_tmp_coords, text_unit_size,
                       COLOURS["world win text"])

    def display_win_text(self) -> None:
        for i in range(len(self.WORLD.WIN_TEXT)):
            for j in range(len(self.WORLD.WIN_TEXT[i])):
                for k in range(len(self.WORLD.WIN_TEXT[i][j])):
                    if self.WORLD.WIN_TEXT[i][j][k] == 1:
                        self.display_text_unit(i, j, k)

    def display(self) -> None:

        self.DISPLAY_SURFACE.fill(COLOURS["world bg"])

        self.move_cam_with_player()

        if not self.PLAYER_TO_FOLLOW.won:
            self.light_hotspot_logic()
        else:
            self.display_win_area()

        if not self.PLAYER_TO_FOLLOW.won \
                and self.PLAYER_TO_FOLLOW.win_area_display:
            self.display_win_area_fake()

        self.display_player()

        if self.PLAYER_TO_FOLLOW.won:
            self.display_win_text()
