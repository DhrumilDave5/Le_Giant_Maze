from Game_Files.maze import CONSTANTS as MAZE_CONSTANTS

CONSTANTS = {"win area length": 100,
             "win area breadth": 5
             }


def create_win_area_matrix() -> list[list[int]]:
    a = MAZE_CONSTANTS["empty map unit"]
    b = MAZE_CONSTANTS["filled map unit"]
    m = [[b, ] * (CONSTANTS["win area breadth"] + 2), ]
    tmp = [a, ] * CONSTANTS["win area breadth"]
    tmp = [b, ] + tmp + [b, ]
    for i in range(CONSTANTS["win area length"]):
        m.append(tmp)
    m.append([b, ] * (CONSTANTS["win area breadth"] + 2))
    CONSTANTS["player spawn"] = (1, len(m[0]) // 2)
    CONSTANTS["win text position"] = (len(m[0]) // 2, len(m[0]) // 2)
    return m


WIN_AREA_MATRIX = create_win_area_matrix()
