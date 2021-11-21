CONSTANTS = {"empty map unit": 0,
             "filled map unit": 1,
             "player spawn map unit": 2,
             "win map unit": 3,
             "win area length": 100,
             "win area breadth": 5
             }


def create_maze_map(maze) -> list[list[int]]:
    m = maze

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

    a = CONSTANTS["filled map unit"]
    b = CONSTANTS["player spawn map unit"]
    c = CONSTANTS["win map unit"]

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

    def transpose(matrix: list[list]) -> list[list]:
        return [[matrix[q][p] for q in range(len(matrix))]
                for p in range(len(matrix[0]))]

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
        if m[i][0] == b:
            start_x = i
            m[start_x][0] = CONSTANTS["empty map unit"]
            if start_x == 1:
                start_x += 1
            if start_x == len(m) - 2:
                start_x -= 1
            start_direction = "up"

    if b in m[-1][1:-1]:
        start_y = m[-1].index(b)
        m[-1][start_y] = CONSTANTS["empty map unit"]
        if start_y == 1:
            start_y += 1
        if start_y == len(m[-1]) - 2:
            start_y -= 1
        start_direction = "right"

    for i in range(len(m))[1:-1]:
        if m[i][-1] == b:
            start_x = i
            m[start_x][-1] = CONSTANTS["empty map unit"]
            if start_x == 1:
                start_x += 1
            if start_x == len(m) - 2:
                start_x -= 1
            start_direction = "down"

    if b in m[0][1:-1]:
        start_y = m[0].index(b)
        m[0][start_y] = CONSTANTS["empty map unit"]
        if start_y == 1:
            start_y += 1
        if start_y == len(m[0]) - 2:
            start_y -= 1
        start_direction = "left"

    for i in range(len(m))[1:-1]:
        if m[i][0] == c:
            end_x = i
            m[end_x][0] = CONSTANTS["empty map unit"]
            end_direction = "up"
            if start_direction == "left":
                end_x += len(left_spawn_area)
            if end_x - 1 + len(up_near_win_area) > len(m):
                up_near_win_area_extending = True

    if c in m[-1][1:-1]:
        end_y = m[-1].index(c)
        m[-1][end_y] = CONSTANTS["empty map unit"]
        end_direction = "right"
        if start_direction == "up":
            end_y += len(up_spawn_area[0])
        if end_y - len(right_near_win_area_1[0]) + 2 < 0:
            right_near_win_area_extending = True

    for i in range(len(m))[1:-1]:
        if m[i][-1] == c:
            end_x = i
            m[end_x][-1] = CONSTANTS["empty map unit"]
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
                m[i] = [a, ] * len(up_spawn_area[0]) + m[i]
            else:
                m[i] = up_spawn_area[i - (start_x - (tmp // 2))] + m[i]

    elif start_direction == "right":
        tmp = len(right_spawn_area[0])
        for i in range(len(right_spawn_area)):
            m += [[a, ] * (start_y - (tmp // 2))
                  + right_spawn_area[i]
                  + [a, ] * (len(m[0]) - (start_y + (tmp // 2) + 1)), ]

    elif start_direction == "down":
        tmp = len(up_spawn_area)
        for i in range(len(m)):
            if i < start_x - (tmp // 2) or i > start_x + (tmp // 2):
                m[i] += [a, ] * len(down_spawn_area[0])
            else:
                m[i] += down_spawn_area[i - (start_x - (tmp // 2))]

    elif start_direction == "left":
        tmp = len(left_spawn_area[0])
        for i in range(len(left_spawn_area)):
            m = [[a, ] * (start_y - (tmp // 2))
                 + left_spawn_area[len(left_spawn_area) - 1 - i]
                 + [a, ] * (len(m[0]) - start_y - (tmp // 2) - 1), ] + m

    # Adding Filled Map Units as per the End Direction

    if end_direction == "up":
        for i in range(len(m)):
            if i < end_x - 1 or i > end_x + len(up_near_win_area) - 2:
                m[i] = [a, ] * len(up_near_win_area[0]) + m[i]
            else:
                m[i] = up_near_win_area[i - (end_x - 1)] + m[i]
        if up_near_win_area_extending:
            for i in range((end_x - 1 + len(up_near_win_area)) - len(m)):
                m += [up_near_win_area[i + (len(m) - (end_x - 1))]
                      + [a, ] * len(m[-1]), ]

    elif end_direction == "right":
        if not right_near_win_area_extending:
            for i in range(len(right_near_win_area_1)):
                m += [[a, ] * (end_y - 3)
                      + right_near_win_area_1[i]
                      + [a, ] * (len(m[0]) - (end_y + 2)), ]
        else:
            for i in range(len(right_near_win_area_2)):
                m += [[a, ] * (end_y - 1)
                      + right_near_win_area_2[i]
                      + [a, ] * (len(m[0]) - (end_y + 4)), ]

    elif end_direction == "down":
        for i in range(len(m)):
            if i < end_x - 1 or i > end_x + len(down_near_win_area) - 2:
                m[i] += [a, ] * len(down_near_win_area[0])
            else:
                m[i] += down_near_win_area[i - (end_x - 1)]
        if down_near_win_area_extending:
            for i in range((end_x - 1 + len(down_near_win_area)) - len(m)):
                m += [[a, ] * len(m[-1])
                      + down_near_win_area[i + (len(m) - (end_x - 1))], ]

    # Finding Player Spawn & Win
    for i in range(len(m)):

        if b in m[i]:
            CONSTANTS["maze player spawn"] = (i, m[i].index(b))
            m[i][m[i].index(b)] = CONSTANTS["empty map unit"]

        if c in m[i]:
            CONSTANTS["win"] = (i, m[i].index(c))

            tmp = CONSTANTS["win"][0]
            tmp_list = []
            while True:
                tmp_list.append((tmp, CONSTANTS["win"][1]))
                tmp -= 1
                if m[tmp][CONSTANTS["win"][1]] \
                        == CONSTANTS["filled map unit"]:
                    break
            CONSTANTS["map units near win"] = tmp_list

            m[i][m[i].index(c)] = CONSTANTS["empty map unit"]

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


def create_win_area_map() -> list[list[int]]:
    a = CONSTANTS["empty map unit"]
    b = CONSTANTS["filled map unit"]
    m = [[b, ] * (CONSTANTS["win area breadth"] + 2), ]
    tmp = [a, ] * CONSTANTS["win area breadth"]
    tmp = [b, ] + tmp + [b, ]
    for i in range(CONSTANTS["win area length"]):
        m.append(tmp)
    m.append([b, ] * (CONSTANTS["win area breadth"] + 2))
    CONSTANTS["player spawn"] = (1, len(m[0]) // 2)
    CONSTANTS["win text"] = (len(m[0]) // 2, len(m[0]) // 2)
    return m
