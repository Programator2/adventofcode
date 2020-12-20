from aoc import *
from collections import defaultdict
from itertools import combinations
from pprint import pprint
from math import sqrt


FILE = "20_test.txt"
FILE = "20.txt"


table = {
    0: {0: 0, 1: 1, 2: 2, 3: 3, "V": 4, "H": 6},
    1: {0: 1, 1: 2, 2: 3, 3: 0, "V": 7, "H": 5},
    2: {0: 2, 1: 3, 2: 0, 3: 1, "V": 6, "H": 4},
    3: {0: 3, 1: 0, 2: 1, 3: 2, "V": 5, "H": 7},
    4: {0: 4, 1: 5, 2: 6, 3: 7, "V": 0, "H": 2},
    5: {0: 5, 1: 6, 2: 7, 3: 4, "V": 3, "H": 1},
    6: {0: 6, 1: 7, 2: 4, 3: 5, "V": 2, "H": 0},
    7: {0: 7, 1: 4, 2: 5, 3: 6, "V": 1, "H": 3},
}


def transform(state, transform):
    global table
    return table[table[state][transform[0]]][transform[1]]


def double_transform(transform1, transform2):
    initial_state = 0
    return transform(transform(initial_state, transform1), transform2)


def get(tile, side, reverse=False):
    if side == "T":
        return list(reversed(tile[0])) if reverse else tile[0]
    elif side == "R":
        col = [x[-1] for x in tile]
        return list(reversed(col)) if reverse else col
    elif side == "B":
        return list(reversed(tile[-1])) if reverse else tile[-1]
    elif side == "L":
        col = [x[0] for x in tile]
        return list(reversed(col)) if reverse else col


def get_transform(side: str, side2: str, reverse: bool):
    numa = {"T": 0, "R": 1, "B": 2, "L": 3}
    numb = {"T": 2, "R": 1, "B": 0, "L": 3}
    rot = (numa[side] + numb[side2]) % 4
    flip = 0
    if not reverse:
        if (side2 == "B" and side in ["B", "L"]) or (
            side2 == "T" and side in ["T", "R"]
        ):
            flip = "V"
        elif (side2 == "L" and side in ["B", "L"]) or (
            side2 == "R" and side in ["T", "R"]
        ):
            flip = "H"
    else:
        if (side2 == "T" and side in ["B", "L"]) or (
            side2 == "B" and side in ["T", "R"]
        ):
            flip = "V"
        elif (side2 == "R" and side in ["B", "L"]) or (
            side2 == "L" and side in ["T", "R"]
        ):
            flip = "H"
    return flip, rot


def find_neig(tiles):
    neig = defaultdict(dict)  # id -> side -> (ID, transf)
    for a, b in combinations(tiles, 2):
        ma = tiles[a]
        mb = tiles[b]
        options = ("T", "R", "B", "L")
        for oa in options:
            for ob in options:
                for r in (False, True):
                    if get(ma, oa) == get(mb, ob, r):
                        # if (a,b) in [(3673,3389), (3389,3673)]:
                        # breakpoint()
                        transform = get_transform(oa, ob, r)
                        neig[a][oa] = (b, transform)
                        transform = get_transform(ob, oa, r)
                        neig[b][ob] = (a, transform)
    return neig


def apply_tran(state, side):
    a = {
        0: {"T": "T", "R": "R", "B": "B", "L": "L"},
        1: {"T": "L", "R": "T", "B": "R", "L": "B"},
        2: {"T": "B", "R": "L", "B": "T", "L": "R"},
        3: {"T": "R", "R": "B", "B": "L", "L": "T"},
        4: {"T": "T", "R": "L", "B": "B", "L": "R"},
        5: {"T": "R", "R": "T", "B": "L", "L": "B"},
        6: {"T": "B", "R": "R", "B": "T", "L": "L"},
        7: {"T": "L", "R": "B", "B": "R", "L": "T"},
    }
    return a[state][side]


def state_get_transform(state):
    return {
        0: (0, 0),
        1: (0, 1),
        2: (0, 2),
        3: (0, 3),
        4: ("V", 0),
        5: ("V", 1),
        6: ("H", 0),
        7: ("H", 1),
    }[state]


def create_map(neig):
    siz = int(sqrt(len(neig)))
    m = [[(None, (0, 0))] * siz for i in range(siz)]

    row = 0
    col = 0

    # This was found by hand in the neig dictionary
    # You just need to find the upper left corner
    # The set the transformation of everything
    # global_transform = (0, 2)
    m[row][col] = (3677, 2, (0, 2))
    while True:
        col += 1
        if col == siz:
            col = 0
            row += 1
            if row == siz:
                break
        if col != 0:
            try:
                left_on_map = m[row][col - 1]
                neighbour_info = neig[left_on_map[0]]
                side = apply_tran(left_on_map[1], "R")
                nex = neighbour_info[
                    side
                ]  # There would be R, but we need to transform it
            except KeyError as err:
                print("Couldnt find key:", err)
                print("Printing current map:")
                pprint(m)
                print(f"block on the left: {left_on_map}")
                print(
                    f"neigh information about the block on the left: {neighbour_info}"
                )
                print(f"searching right block on this absolute side: {side}")
                breakpoint()
            m[row][col] = (
                nex[0],
                n := double_transform(nex[1], left_on_map[2]),
                state_get_transform(n),
            )
        else:
            nex = neig[
                m[row - 1][col][0]
            ][  # There would be B, but we need to transform it
                apply_tran(m[row - 1][col][1], "B")
            ]
            # if row==1 and col==0:
            # breakpoint()
            m[row][col] = (
                nex[0],
                n := double_transform(nex[1], m[row - 1][col][2]),
                state_get_transform(n),
            )
    return m


def transform_picture(picture, tran):
    if tran == 1:
        picture = zip(*picture)
        picture = [list(reversed(x)) for x in picture]
        return picture
    if tran == 2:
        return transform_picture(transform_picture(picture, 1), 1)
    if tran == 3:
        return transform_picture(transform_picture(transform_picture(picture, 1), 1), 1)
    if tran == 4:
        return [list(reversed(x)) for x in picture]
    if tran == 5:
        return transform_picture(transform_picture(picture, 4), 1)
    if tran == 6:
        return list(reversed(picture))
    if tran == 7:
        return transform_picture(transform_picture(picture, 6), 1)
    return picture


def create_raster(tiles, m):
    example_picture = tiles[m[0][0][0]]
    dimension = len(m) * (len(example_picture[0]) - 2)
    small_picture_side = len(example_picture[0]) - 2
    # print(f'Dimension of large image is {dimension}')
    global_picture = [[None] * dimension for i in range(dimension)]
    # print(f'Global picture is {len(global_picture)} x {len(global_picture[0])}')
    for row_index, r in enumerate(m):
        for col_index, c in enumerate(r):
            picture = tiles[c[0]]
            transform_type = c[1]
            new_picture = [a[1:-1] for a in picture[1:-1]]
            new_picture = transform_picture(new_picture, transform_type)
            for p_row_ind, p_row in enumerate(new_picture):
                for p_col_ind, p_col in enumerate(p_row):
                    # print(f'Now writing into row {row_index*dimension+p_row_ind}')
                    # print(f'Now writing into col {col_index*dimension+p_col_ind}')
                    global_picture[row_index * small_picture_side + p_row_ind][
                        col_index * small_picture_side + p_col_ind
                    ] = p_col
    return global_picture


def search_monster(picture):
    monster = [
        "                  # ",
        "#    ##    ##    ###",
        " #  #  #  #  #  #   ",
    ]
    hashes = set()
    width = len(monster[0])
    height = len(monster)
    roughness_monster = -sum(1 for c in monster for d in c if d == "#")
    roughness = sum(1 for c in picture for d in c if d == "#")
    for r, a in enumerate(monster):
        for c, b in enumerate(a):
            if b == "#":
                hashes.add((r, c))
    for row_index, r in enumerate(picture[:-2]):
        for col_index, c in enumerate(r[: -(width - 1)]):
            if all(picture[row_index + a][col_index + b] == "#" for a, b in hashes):
                roughness += roughness_monster
    return roughness


def main():
    inp = file(FILE)
    inp = inp.split("\n\n")
    tiles = {}
    for i in inp:
        i = i.split("\n")
        number = int(i[0][5:-1])
        tiles[number] = list(map(lambda x: list(x.rstrip()), i[1:]))
    neig = find_neig(tiles)
    # pprint(neig)
    m = create_map(neig)
    # pprint(m)
    picture = create_raster(tiles, m)
    # pprint(picture)
    print(min(search_monster(transform_picture(picture, i)) for i in range(8)))


main()
