from aoc import *
from functools import reduce


ins_to_diff = {
    '^': (-1, 0),
    '>': (0, 1),
    'v': (1, 0),
    '<': (0, -1),
}


def main(infi: str):
    inp = filerstrip(infi)
    m, instructions = inp.split('\n\n')
    m = map_dd_from_str(m)

    maxi, maxj = map_dd_size(m)
    pos = [(i, j) for (i, j), e in m.items() if e == '@'][0]
    m[pos] = '.'

    instructions = reduce(lambda x, y: x + y, instructions.split('\n'))

    for ins in instructions:
        diff = ins_to_diff[ins]
        point = (pos[0] + diff[0], pos[1] + diff[1])
        if m.get(point, None) == '.':
            # move robot
            pos = point
            continue
        while (last_item := m.get(point, None)) == 'O':
            point = (point[0] + diff[0], point[1] + diff[1])
        if last_item == '#':
            # can't move
            continue
        elif last_item == '.':
            # move boxes
            pos = (pos[0] + diff[0], pos[1] + diff[1])
            m[pos] = '.'
            m[point] = 'O'
    # for row in range(maxi):
    #     for c in range(maxj):
    #         print(m[row, c], end='')
    #     print()

    return sum(100 * i + j for (i, j), e in m.items() if e == 'O')


DAY = 15
FILE_TEST = f"{DAY}_testa.txt"
# FILE_TEST = f"{DAY}_testb.txt"
FILE_EXP = f"{DAY}_exp.txt"
FILE = f"{DAY}.txt"
# test_and_submit(main, FILE_TEST, FILE_EXP, FILE, DAY)
# print(main(FILE_TEST))
print(main(FILE))
