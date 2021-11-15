from pygame.colordict import THECOLORS

COLOURS = {"world bg colour": THECOLORS["black"],
           "player colour": THECOLORS["dodgerblue3"],
           "world floor colour": THECOLORS["sienna"],
           "world cave rock colour": THECOLORS["grey12"],
           "world win area colour": (255, 215, 31),
           # THECOLORS["gold"] has value (255, 215, 0)
           "world win text colour": THECOLORS["black"]
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
