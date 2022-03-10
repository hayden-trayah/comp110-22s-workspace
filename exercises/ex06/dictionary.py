"""Dictionary functions practcie for ex06 - Hayden Trayah."""

__author__ = "730325581"


def invert(map: dict[str, str]) -> dict[str, str]:
    """Inverts the keys and values of the inputted dictionary."""
    values: list[str] = []
    for x in map.values():
        if x in values:
            raise KeyError("Duplicates values in input")
        else:
            values.append(x)
    inverted_map: dict[str, str] = {}
    for x in map.keys():
        inverted_map[map[x]] = x

    return inverted_map


def favorite_color(map: dict[str, str]) -> str:
    """Returns the most common color in the dictionary."""
    colors: dict[str, int] = {}
    for x in map.values():
        if x in colors.keys():
            colors[x] += 1
        else:
            colors[x] = 1
    mode_color: str = ""

    for x in colors.keys():
        if mode_color == "":
            mode_color = x
        elif colors[mode_color] < colors[x]:
            mode_color = x

    return mode_color


def count(list: list[str]) -> dict[str, int]:
    """Gives a dictionary with keys given by list values and their values given by the count of each key in the list."""
    output_dict: dict[str, int] = {}
    for x in list:
        if x in output_dict.keys():
            output_dict[x] += 1
        else:
            output_dict[x] = 1
    
    return output_dict
