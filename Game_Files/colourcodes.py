from pygame import colordict as cd

COLOURS = {"world bg colour": cd.THECOLORS["black"],
           "player colour": cd.THECOLORS["dodgerblue3"],
           "world floor colour": cd.THECOLORS["sienna"],
           "world cave rock colour": cd.THECOLORS["grey12"],
           "world win area colour": (255, 215, 31),
           # THECOLORS["gold"] has value (255, 215, 0)
           "world win text colour": cd.THECOLORS["black"]
           }


def give_shades_list(base_colour: tuple[int]) -> tuple[tuple[int]]:
    shades_list = []
    for i in range(8):
        rgb_list = []
        for j in base_colour:
            x = j - (i * ((j + 1) // 8))
            if x < 5:
                x = 5
            rgb_list.append(x)
        shades_list.append(tuple(rgb_list))
    return tuple(shades_list)
