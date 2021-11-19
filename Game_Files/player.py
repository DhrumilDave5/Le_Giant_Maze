import pygame
from Game_Files import maze, world as world_

CONSTANTS = {"player size in length quanta": 10,
             "light level": 9
             }


class Player:

    def tmp(self):
        pass

    def __init__(self, world, up_key=pygame.K_w, right_key=pygame.K_d,
                 down_key=pygame.K_s, left_key=pygame.K_a):

        self.WORLD = world
        self.UP_KEY = up_key
        self.RIGHT_KEY = right_key
        self.DOWN_KEY = down_key
        self.LEFT_KEY = left_key

        lq = world_.CONSTANTS["length quanta"]
        mus = self.WORLD.MAP_UNIT_SIZE

        self.SIZE = lq * CONSTANTS["player size in length quanta"]

        self.rect = pygame.Rect((self.WORLD.PLAYER_SPAWN[0] * mus),
                                (self.WORLD.PLAYER_SPAWN[1] * mus),
                                self.SIZE, self.SIZE)
        self.rect.x += (((mus - self.SIZE) // 2) // lq) * lq
        self.rect.y += (((mus - self.SIZE) // 2) // lq) * lq

        '''
        tlmu: Top-left Map Unit
        trmu: Top-right Map Unit
        blmu: Bottom-left Map Unit
        brmu: Bottom-left Map Unit
        cmu: Centre Map Unit
        These variables basically represent which map unit the corners and
        centre of Player.rect is in
        '''
        self.tlmu = (self.rect.topleft[0] // mus,
                     self.rect.topleft[1] // mus)
        self.trmu = ((self.rect.topright[0] - lq) // mus,
                     self.rect.topright[1] // mus)
        self.blmu = (self.rect.bottomleft[0] // mus,
                     (self.rect.bottomleft[1] - lq) // mus)
        self.brmu = ((self.rect.bottomright[0] - lq) // mus,
                     (self.rect.bottomright[1] - lq) // mus)
        self.cmu = (self.rect.center[0] // mus,
                    self.rect.center[1] // mus)

        self.won = False
        self.win_area_display = False

    def update_map_unit_stuff(self) -> None:
        lq = world_.CONSTANTS["length quanta"]
        mus = self.WORLD.MAP_UNIT_SIZE
        self.tlmu = (self.rect.topleft[0] // mus,
                     self.rect.topleft[1] // mus)
        self.trmu = ((self.rect.topright[0] - lq) // mus,
                     self.rect.topright[1] // mus)
        self.blmu = (self.rect.bottomleft[0] // mus,
                     (self.rect.bottomleft[1] - lq) // mus)
        self.brmu = ((self.rect.bottomright[0] - lq) // mus,
                     (self.rect.bottomright[1] - lq) // mus)
        self.cmu = (self.rect.center[0] // mus,
                    self.rect.center[1] // mus)

    def move_up(self) -> None:
        self.rect.y -= world_.CONSTANTS["length quanta"]
        self.update_map_unit_stuff()

    def move_right(self) -> None:
        self.rect.x += world_.CONSTANTS["length quanta"]
        self.update_map_unit_stuff()

    def move_down(self) -> None:
        self.rect.y += world_.CONSTANTS["length quanta"]
        self.update_map_unit_stuff()

    def move_left(self) -> None:
        self.rect.x -= world_.CONSTANTS["length quanta"]
        self.update_map_unit_stuff()

    def check_up_collision(self) -> None:
        a = maze.CONSTANTS["filled map unit"]
        if self.WORLD.MAP[self.tlmu[0]][self.tlmu[1]] == a \
                or self.WORLD.MAP[self.trmu[0]][self.trmu[1]] == a:
            self.move_down()

    def check_right_collision(self) -> None:
        a = maze.CONSTANTS["filled map unit"]
        if self.WORLD.MAP[self.trmu[0]][self.trmu[1]] == a \
                or self.WORLD.MAP[self.brmu[0]][self.brmu[1]] == a:
            self.move_left()

    def check_down_collision(self) -> None:
        a = maze.CONSTANTS["filled map unit"]
        if self.WORLD.MAP[self.blmu[0]][self.blmu[1]] == a \
                or self.WORLD.MAP[self.brmu[0]][self.brmu[1]] == a:
            self.move_up()

    def check_left_collision(self) -> None:
        a = maze.CONSTANTS["filled map unit"]
        if self.WORLD.MAP[self.tlmu[0]][self.tlmu[1]] == a \
                or self.WORLD.MAP[self.blmu[0]][self.blmu[1]] == a:
            self.move_right()

    def check_near_win(self) -> None:
        if self.cmu in self.WORLD.MAP_UNITS_NEAR_WIN:
            self.win_area_display = True
        else:
            self.win_area_display = False

    def declare_win(self) -> None:
        self.won = True
        self.WORLD.change_map_to_win_area()
        a = self.WORLD.MAP_UNIT_SIZE
        x = (self.WORLD.WIN_AREA_PLAYER_SPAWN[0] * a) + (self.rect.x % a)
        y = (self.WORLD.WIN_AREA_PLAYER_SPAWN[1] * a) + (self.rect.y % a)
        self.rect.x, self.rect.y = x, y
        pygame.mixer.music.play()

    def movement(self) -> None:

        keys = pygame.key.get_pressed()

        if keys[self.UP_KEY]:
            self.move_up()
            self.check_up_collision()

        if keys[self.RIGHT_KEY]:
            self.move_right()
            self.check_right_collision()

        if keys[self.DOWN_KEY]:
            self.move_down()
            self.check_down_collision()

        if keys[self.LEFT_KEY]:
            self.move_left()
            self.check_left_collision()

        self.check_near_win()

        if not self.won:
            if (self.tlmu[0], self.tlmu[1]) == self.WORLD.WIN_POSITION:
                self.declare_win()
