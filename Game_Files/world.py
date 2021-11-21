from Game_Files import maze, map, textunits

CONSTANTS = {"length quanta": 5,
             "map unit size in length quanta": 20,
             "win text": "YOU FOUND YOUR WAY OUT OF THE MAZE!"
                         "     GAME BY: DHRUMIL DAVE"
             }


class World:

    def __init__(self):

        self.MAZE_MAP = map.create_maze_map(maze.MAZE)
        self.WIN_AREA_MAP = map.create_win_area_map()

        self.EMPTY_MAP_UNIT = map.CONSTANTS["empty map unit"]
        self.PLAYER_SPAWN = map.CONSTANTS["player spawn"]
        self.MAP_UNITS_NEAR_WIN = map.CONSTANTS["map units near win"]
        self.WIN_POSITION = map.CONSTANTS["win"]
        self.WIN_AREA_PLAYER_SPAWN = map.CONSTANTS["player spawn"]
        self.WIN_TEXT_POSITION = map.CONSTANTS["win text"]
        self.WIN_AREA_LENGTH = map.CONSTANTS["win area length"]
        self.WIN_AREA_BREADTH = map.CONSTANTS["win area breadth"]
        self.MAP_UNITS = {"empty": map.CONSTANTS["empty map unit"],
                          "filled": map.CONSTANTS["filled map unit"]
                          }
        self.LENGTH_QUANTA = CONSTANTS["length quanta"]

        self.MAP_UNIT_SIZE = self.LENGTH_QUANTA \
            * CONSTANTS["map unit size in length quanta"]

        self.WIN_TEXT = textunits.get_text_units(CONSTANTS["win text"])
        self.WIN_TEXT_UNIT_SIZE = \
            self.MAP_UNIT_SIZE // len(self.WIN_TEXT[0])

        self.map = self.MAZE_MAP
