import Game_Files.maze as maze
import Game_Files.winarea as winarea
from Game_Files.textunits import string_to_text_units

CONSTANTS = {"length quanta": 5,
             "map unit size in length quanta": 20,
             "win text": "YOU FOUND YOUR WAY OUT OF THE MAZE!"
                         "     GAME BY: DHRUMIL DAVE"
             }


class World:

    def __init__(self):

        self.MAP = maze.MAZE_MATRIX
        self.PLAYER_SPAWN = maze.CONSTANTS["player spawn"]
        self.MAP_UNITS_NEAR_WIN = maze.CONSTANTS["map units near win"]
        self.WIN_POSITION = maze.CONSTANTS["win"]
        self.WIN_AREA_PLAYER_SPAWN = winarea.CONSTANTS["player spawn"]
        self.WIN_TEXT_POSITION = winarea.CONSTANTS["win text position"]

        self.MAP_UNIT_SIZE = CONSTANTS["length quanta"] \
            * CONSTANTS["map unit size in length quanta"]

        self.WIN_TEXT = string_to_text_units(CONSTANTS["win text"])
        self.WIN_TEXT_UNIT_SIZE = \
            self.MAP_UNIT_SIZE // len(self.WIN_TEXT[0])

    def change_map_to_win_area(self) -> None:
        self.MAP = winarea.WIN_AREA_MATRIX
