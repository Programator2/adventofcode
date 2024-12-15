from aoc import *
from collections import defaultdict
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
    m = list(map(lambda x: x.rstrip(), m.split('\n')))

    d = defaultdict()
    for r, row in enumerate(m):
        for ei, e in enumerate(row):
            if e == '.':
                e = '.', '.'
            elif e == 'O':
                e = '[', ']'
            elif e == '#':
                e = '#', '#'
            elif e == '@':
                e = '@', '.'
            d[(r, ei * 2)] = e[0]
            d[(r, ei * 2 + 1)] = e[1]
    m = d
    # print(m)
    maxi, maxj = map_dd_size(m)
    pos = [(i, j) for (i, j), e in m.items() if e == '@'][0]
    m[pos] = '.'

    instructions = reduce(lambda x, y: x + y, instructions.split('\n'))

    for i, ins in enumerate(instructions):
        diff = ins_to_diff[ins]
        point = (pos[0] + diff[0], pos[1] + diff[1])
        # positions to check
        check_pos = [point]
        # boxes to move
        move = []
        if m.get(point, None) == '.':
            # move robot
            pos = point
            continue
        # check positions which need to be free
        while all(m[cp] in '[].' for cp in check_pos) and any(
            m[cp] in '[]' for cp in check_pos
        ):
            # we have some boxes to move
            for cp in check_pos:
                if m[cp] == '[':
                    move.append(cp)
                elif m[cp] == ']':
                    move.append((cp[0], cp[1] - 1))
            if ins in '<>':
                check_pos = [
                    (point[0] + 2 * diff[0], point[1] + 2 * diff[1])
                    for point in check_pos
                ]
                assert len(check_pos) == 1
            else:
                check_pos = set(check_pos)
                for cp in list(check_pos):
                    if m[cp] == '[':
                        check_pos.add((cp[0], cp[1] + 1))
                    elif m[cp] == ']':
                        check_pos.add((cp[0], cp[1] - 1))
                check_pos = [
                    (point[0] + diff[0], point[1] + diff[1])
                    for point in check_pos
                    if m[point] in '[]'
                ]
        if any(m[cp] == '#' for cp in check_pos):
            # can't move
            continue
        elif all(m[cp] == '.' for cp in check_pos):
            # move boxes
            # first remove old positions
            for cp in move:
                m[cp] = '.'
                m[cp[0], cp[1] + 1] = '.'
            # then write new positions
            for cp in move:
                m[cp[0] + diff[0], cp[1] + diff[1]] = '['
                m[cp[0] + diff[0], cp[1] + diff[1] + 1] = ']'
            pos = (pos[0] + diff[0], pos[1] + diff[1])
        # print(f'{i} move {ins} state')
        # for row in range(maxi):
        #     for c in range(maxj):
        #         if (row, c) == pos:
        #             print('@', end='')
        #         else:
        #             print(m[row, c], end='')
        #     print()

    return sum(100 * i + j for (i, j), e in m.items() if e == '[')


DAY = 15
FILE_TEST = f"{DAY}_testa.txt"
# FILE_TEST = f"{DAY}_testb.txt"
FILE_EXP = f"{DAY}_exp.txt"
FILE = f"{DAY}.txt"
# test_and_submit(main, FILE_TEST, FILE_EXP, FILE, DAY)
# print(main(FILE_TEST))
print(main(FILE))
