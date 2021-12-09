from aoc import *


def search_basin(start, checked: set, m, this_basin: set):
    if start in checked:
        return False
    x, y = start
    checked.add((x, y))
    e = m[x][y]
    if e == 9:
        return False
    this_basin.add((x, y))
    up = m[x][y+1]
    if up > e:
        search_basin((x, y+1), checked, m, this_basin)
    down = m[x][y-1]
    if down > e:
        search_basin((x, y-1), checked, m, this_basin)
    left = m[x-1][y]
    if left > e:
        search_basin((x-1, y), checked, m, this_basin)
    right = m[x+1][y]
    if right > e:
        search_basin((x+1, y), checked, m, this_basin)


def main(input_file: str):
    inp = load_map_ll(input_file)
    out = 0
    m = [[0] * (len(inp[0]) + 2)]
    for i, row in enumerate(inp):
        m.append([0] + [int(x) for x in row] + [0])
    m.append([0] * len(m[0]))
    checked = set()
    basins = []
    for i in range(0, 9):
        for y in range(1, len(m[0])-1):
            for x in range(1, len(m)-1):
                if m[x][y] != i:
                    continue
                basin = set()
                search_basin((x, y), checked, m, basin)
                if basin:
                    basins.append(basin)
    out = sorted([len(b) for b in basins])[-3:]
    return out[0]*out[1]*out[2]

DAY = 9
FILE_TEST = f"{DAY}_test.txt"
FILE_EXP = f"{DAY}_exp.txt"
FILE = f"{DAY}.txt"
# test_and_submit(main, FILE_TEST, FILE_EXP, FILE)
print(main(FILE))
