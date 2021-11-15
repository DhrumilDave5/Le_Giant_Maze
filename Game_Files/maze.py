from Game_Files.simplemaze import SIMPLE_MAZE_MATRIX, transpose
from Game_Files.simplemaze import CONSTANTS as SIMPLE_MAZE_CONSTANTS

CONSTANTS = {"empty map unit":
             SIMPLE_MAZE_CONSTANTS["empty simple maze unit"],
             "filled map unit":
             SIMPLE_MAZE_CONSTANTS["filled simple maze unit"],
             "player spawn map unit": 2,
             "win map unit": 3,
             }


def create_maze_matrix() -> list[list[int]]:
    m = SIMPLE_MAZE_MATRIX[:]

    """
    '''dlt_it:'''
    a = CONSTANTS["spawn area size"]
    b = CONSTANTS["win area breadth"]
    c = CONSTANTS["empty map unit"]
    d = CONSTANTS["filled map unit"]
    e = CONSTANTS["win area map unit"]
    f = maze.CONSTANTS["start point maze unit"]
    g = maze.CONSTANTS["end point maze unit"]

    start_y = m[0].index(f)
    for i in range(a):
        m.insert(0, ([d, ] * (start_y - (a // 2))
                     + [c, ] * a
                     + [d, ] * (len(m[0]) - (start_y - a // 2) - a)))
    m.insert(0, [d, ] * len(m[0]))

    for i in range(len(m)):
        if f in m[i]:
            start_x = i
            break
    else:
        start_x = 0

    end_y = m[len(m) - 1].index(g)
    for i in range(CONSTANTS["win area length"]):
        m.append([d, ] * (end_y - (b // 2))
                 + [e, ] * b
                 + [d, ] * (len(m[0]) - (end_y - (b // 2)) - b))
    m.append([d, ] * len(m[0]))

    end_x = 0
    for i in range(len(m)):
        if g in m[i]:
            end_x = i
            break

    list1 = []
    h = end_x + 1
    while True:
        list1.append((h, end_y))
        h -= 1
        if m[h][end_y] == CONSTANTS["filled map unit"]:
            break

    m[start_x][start_y] = m[end_x][end_y] = c
    CONSTANTS["player spawn map unit"] = start_x - ((a // 2) + 1), start_y
    CONSTANTS["win text map unit"] = (end_x + (b // 2) + 1, end_y)
    CONSTANTS["win area light hotspot"] = (end_x - (b // 2), end_y)
    CONSTANTS["map units near win area"] = list1
    """

    a = SIMPLE_MAZE_CONSTANTS["start point simple maze unit"]
    b = SIMPLE_MAZE_CONSTANTS["end point simple maze unit"]
    c = CONSTANTS["empty map unit"]
    d = CONSTANTS["filled map unit"]
    e = CONSTANTS["player spawn map unit"]
    f = CONSTANTS["win map unit"]

    up_spawn_area = [[1, 1, 1, 1, 1],
                     [1, 0, 0, 0, 1],
                     [1, 0, 2, 0, 1],
                     [1, 0, 0, 0, 1],
                     ]
    right_spawn_area = [[1, 1, 1, 1],
                        [0, 0, 0, 1],
                        [0, 2, 0, 1],
                        [0, 0, 0, 1],
                        [1, 1, 1, 1]
                        ]
    down_spawn_area = [[1, 0, 0, 0, 1],
                       [1, 0, 2, 0, 1],
                       [1, 0, 0, 0, 1],
                       [1, 1, 1, 1, 1],
                       ]
    left_spawn_area = [[1, 1, 1, 1],
                       [1, 0, 0, 0],
                       [1, 0, 2, 0],
                       [1, 0, 0, 0],
                       [1, 1, 1, 1]
                       ]
    up_near_win_area = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                        [1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                        [1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                        [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 3, 1],
                        [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                        [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
                        ]
    right_near_win_area_1 = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                             [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                             [0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                             [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 3, 1],
                             [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
                             ]
    right_near_win_area_2 = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                             [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 3, 1],
                             [0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                             [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                             [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
                             ]
    down_near_win_area = [[1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                          [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                          [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 3, 1],
                          [1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                          [1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                          [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
                          ]
    up_spawn_area = transpose(up_spawn_area)
    right_spawn_area = transpose(right_spawn_area)
    down_spawn_area = transpose(down_spawn_area)
    left_spawn_area = transpose(left_spawn_area)
    up_near_win_area = transpose(up_near_win_area)
    right_near_win_area_1 = transpose(right_near_win_area_1)
    right_near_win_area_2 = transpose(right_near_win_area_2)
    down_near_win_area = transpose(down_near_win_area)

    start_direction, end_direction = "", ""
    start_x = start_y = end_x = end_y = -1
    up_near_win_area_extending = False
    right_near_win_area_extending = False
    down_near_win_area_extending = False

    # Checking for start & end point in up, right, down, left directions

    """
    dlt_it:
    for i in range(1, len(m) - 1):
        if m[i][0] == a:
            start_x = i
            if i == 1:
                start_x += 1
            if i == len(m) - 2:
                start_x -= 1
            start_direction = "up"
            m[i][0] = c
        elif m[i][len(m[i]) - 1] == a:
            start_x = i
            if i == 1:
                start_x += 1
            if i == len(m) - 2:
                start_x -= 1
            start_direction = "down"
            m[i][len(m[i]) - 1] = c
        if m[i][0] == b:
            end_x = i
            end_direction = "up"
            m[i][0] = c
        elif m[i][len(m[i]) - 1] == b:
            end_x = i
            end_direction = "down"
            m[i][len(m[i]) - 1] = c
    for i in range(1, len(m[len(m) - 1]) - 1):
        if m[len(m) - 1][i] == a:
            start_y = i
            if i == 1:
                start_y += 1
            if i == len(m[len(m) - 1]) - 2:
                start_y -= 1
            start_direction = "right"
            m[len(m) - 1][i] = c
        if m[len(m) - 1][i] == b:
            end_y = i
            end_direction = "right"
            m[len(m) - 1][i] = c
    for i in range(1, len(m[0]) - 1):
        if m[0][i] == a:
            start_y = i
            if i == 1:
                start_y += 1
            if i == len(m[len(m) - 1]) - 2:
                start_y -= 1
            start_direction = "left"
            m[0][i] = c
        if m[0][i] == b:
            end_y = i
            end_direction = "left"
            m[0][i] = c
    """

    for i in range(len(m))[1:-1]:
        if m[i][0] == a:
            start_x = i
            m[start_x][0] = c
            if start_x == 1:
                start_x += 1
            if start_x == len(m) - 2:
                start_x -= 1
            start_direction = "up"

    if a in m[-1][1:-1]:
        start_y = m[-1].index(a)
        m[-1][start_y] = c
        if start_y == 1:
            start_y += 1
        if start_y == len(m[-1]) - 2:
            start_y -= 1
        start_direction = "right"

    for i in range(len(m))[1:-1]:
        if m[i][-1] == a:
            start_x = i
            m[start_x][-1] = c
            if start_x == 1:
                start_x += 1
            if start_x == len(m) - 2:
                start_x -= 1
            start_direction = "down"

    if a in m[0][1:-1]:
        start_y = m[0].index(a)
        m[0][start_y] = c
        if start_y == 1:
            start_y += 1
        if start_y == len(m[0]) - 2:
            start_y -= 1
        start_direction = "left"

    for i in range(len(m))[1:-1]:
        if m[i][0] == b:
            end_x = i
            m[end_x][0] = c
            end_direction = "up"
            if start_direction == "left":
                end_x += len(left_spawn_area)
            if end_x - 1 + len(up_near_win_area) > len(m):
                up_near_win_area_extending = True

    if b in m[-1][1:-1]:
        end_y = m[-1].index(b)
        m[-1][end_y] = c
        end_direction = "right"
        if start_direction == "up":
            end_y += len(up_spawn_area[0])
        if end_y - len(right_near_win_area_1[0]) + 2 < 0:
            right_near_win_area_extending = True

    for i in range(len(m))[1:-1]:
        if m[i][-1] == b:
            end_x = i
            m[end_x][-1] = c
            end_direction = "down"
            if start_direction == "left":
                end_x += len(left_spawn_area)
            if end_x - 1 + len(down_near_win_area) > len(m):
                down_near_win_area_extending = True

    # Adding Filled Map Units as per the Start Direction

    if start_direction == "up":
        tmp = len(up_spawn_area)
        for i in range(len(m)):
            if i < start_x - (tmp // 2) or i > start_x + (tmp // 2):
                m[i] = [d, ] * len(up_spawn_area[0]) + m[i]
            else:
                m[i] = up_spawn_area[i - (start_x - (tmp // 2))] + m[i]

    elif start_direction == "right":
        tmp = len(right_spawn_area[0])
        for i in range(len(right_spawn_area)):
            m += [[d, ] * (start_y - (tmp // 2))
                  + right_spawn_area[i]
                  + [d, ] * (len(m[0]) - (start_y + (tmp // 2) + 1)), ]

    elif start_direction == "down":
        tmp = len(up_spawn_area)
        for i in range(len(m)):
            if i < start_x - (tmp // 2) or i > start_x + (tmp // 2):
                m[i] += [d, ] * len(down_spawn_area[0])
            else:
                m[i] += down_spawn_area[i - (start_x - (tmp // 2))]

    elif start_direction == "left":
        tmp = len(left_spawn_area[0])
        for i in range(len(left_spawn_area)):
            m = [[d, ] * (start_y - (tmp // 2))
                 + left_spawn_area[len(left_spawn_area) - 1 - i]
                 + [d, ] * (len(m[0]) - start_y - (tmp // 2) - 1), ] + m

    # Adding Filled Map Units as per the End Direction

    if end_direction == "up":
        tmp = len(up_near_win_area)
        tmp2 = len(m)
        tmp3 = len(m[-1])
        for i in range(len(m)):
            if i < end_x - 1 or i > end_x + tmp - 2:
                m[i] = [d, ] * len(up_near_win_area[0]) + m[i]
            else:
                m[i] = up_near_win_area[i - (end_x - 1)] + m[i]
        if up_near_win_area_extending:
            for i in range((end_x - 1 + tmp) - tmp2):
                m += [up_near_win_area[i + (tmp2 - (end_x - 1))]
                      + [d, ] * tmp3, ]

    elif end_direction == "right":
        if not right_near_win_area_extending:
            for i in range(len(right_near_win_area_1)):
                m += [[d, ] * (end_y - 3)
                      + right_near_win_area_1[i]
                      + [d, ] * (len(m[0]) - (end_y + 2)), ]
        else:
            for i in range(len(right_near_win_area_2)):
                m += [[d, ] * (end_y - 1)
                      + right_near_win_area_2[i]
                      + [d, ] * (len(m[0]) - (end_y + 4)), ]

    elif end_direction == "down":
        tmp = len(down_near_win_area)
        tmp2 = len(m)
        tmp3 = len(m[-1])
        for i in range(len(m)):
            if i < end_x - 1 or i > end_x + tmp - 2:
                m[i] += [d, ] * len(down_near_win_area[0])
            else:
                m[i] += down_near_win_area[i - (end_x - 1)]
        if down_near_win_area_extending:
            for i in range((end_x - 1 + tmp) - tmp2):
                m += [[d, ] * tmp3
                      + down_near_win_area[i + (tmp2 - (end_x - 1))], ]

    # Finding Player Spawn & Win
    for i in range(len(m)):

        if e in m[i]:
            CONSTANTS["player spawn"] = (i, m[i].index(e))
            m[i][m[i].index(e)] = c

        if f in m[i]:
            CONSTANTS["win"] = (i, m[i].index(f))

            tmp = CONSTANTS["win"][0]
            tmp_list = []
            while True:
                tmp_list.append((tmp, CONSTANTS["win"][1]))
                tmp -= 1
                if m[tmp][CONSTANTS["win"][1]] \
                        == CONSTANTS["filled map unit"]:
                    break
            CONSTANTS["map units near win"] = tmp_list

            m[i][m[i].index(f)] = c

    """
    dlt_it:
    # Reassigning positions after adding Filled Map Units
    found_start = False
    if start_direction == "up":
        for i in range(len(m[0])):
            for j in range(len(m)):
                if m[j][i] == a:
                    start_x, start_y = j, i
                    found_start = True
                    break
            if found_start:
                break
    elif start_direction == "right":
        for i in range(len(m) - 1, -1, -1):
            for j in range(len(m[0])):
                if m[i][j] == a:
                    start_x, start_y = i, j
                    found_start = True
                    break
            if found_start:
                break
    elif start_direction == "down":
        for i in range(len(m[0]) - 1, -1, -1):
            for j in range(len(m)):
                if m[j][i] == a:
                    start_x, start_y = j, i
                    found_start = True
                    break
            if found_start:
                break
    elif start_direction == "left":
        for i in range(len(m)):
            for j in range(len(m[0])):
                if m[i][j] == a:
                    start_x, start_y = i, j
                    found_start = True
                    break
            if found_start:
                break
    """

    return m


MAZE_MATRIX = create_maze_matrix()
