state = "###....#..#..#......####.#..##..#..###......##.##..#...#.##.###.##.###.....#.###..#.#.##.#..#.#"
# state = '#..#.#..##......###...###'

rules = {
    "..###": "#",
    ".....": ".",
    "..#..": ".",
    ".###.": ".",
    "...##": "#",
    "#.###": ".",
    "#.#.#": "#",
    "##..#": ".",
    "##.##": "#",
    "#...#": ".",
    "..##.": ".",
    "##.#.": ".",
    "...#.": ".",
    "#..#.": "#",
    ".####": "#",
    ".#..#": "#",
    "##...": "#",
    ".##.#": ".",
    "....#": ".",
    "#....": ".",
    ".#.#.": "#",
    ".##..": ".",
    "###.#": "#",
    "####.": ".",
    "#####": "#",
    "#.##.": "#",
    ".#...": "#",
    ".#.##": "#",
    "###..": "#",
    "#..##": ".",
    "#.#..": "#",
    "..#.#": ".",
}

# rules = {
# '...##':  '#',
# '..#..':  '#',
# '.#...':  '#',
# '.#.#.':  '#',
# '.#.##':  '#',
# '.##..':  '#',
# '.####':  '#',
# '#.#.#':  '#',
# '#.###':  '#',
# '##.#.':  '#',
# '##.##':  '#',
# '###..':  '#',
# '###.#':  '#',
# '####.':  '#',
# }


def grow(state, left_index):
    """grows the plants

    :param state: state of plants to grow
    :param lef_index: index of the lefmost plant

    :returns: (new_state, new index of the leftmost plant)

    """
    if state[0] == "#":
        prefix = "...."
        left_index -= 4
    elif state[:2] == ".#":
        prefix = "..."
        left_index -= 3
    elif state[:3] == "..#":
        prefix = ".."
        left_index -= 2
    elif state[:4] == "...#":
        prefix = "."
        left_index -= 1
    else:
        prefix = ""

    if state[-1] == "#":
        postfix = "...."
    elif state[-2:] == "#.":
        postfix = "..."
    elif state[-3:] == "#..":
        postfix = ".."
    elif state[-4:] == "#...":
        postfix = "."
    else:
        postfix = ""

    state = prefix + state + postfix

    new_plant_positions = set()

    for plant_index, i in enumerate(range(len(state) - 4), left_index + 2):
        plant_cut = state[i : i + 5]
        try:
            if rules[plant_cut] == "#":
                new_plant_positions.add(plant_index)
        except KeyError:
            pass

    new_state = "".join(
        "#" if i in new_plant_positions else "."
        for i in range(left_index, len(state) + left_index)
    )

    return new_state, left_index


def main():
    global state
    left_index = 0

    for i in range(20):
        state, left_index = grow(state, left_index)

    print(sum(i for (i, plant) in enumerate(state, left_index) if plant == "#"))


main()


# 3128 too high
# 2688 too high -- 30 generations instead of 20 :facepalm:
