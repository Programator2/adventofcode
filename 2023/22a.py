from aoc import *
from more_itertools import zip_broadcast
from collections import defaultdict


def main(input_file: str):
    inp = lines(input_file)
    bricks = []
    for l in inp:
        start, end = l.split('~')
        start = [int(x) for x in start.split(',')]
        end = [int(x) for x in end.split(',')]
        bricks.append((start, end))

    # Let's check if we don't have any weird "diagonal" bricks.
    #
    # if all(len([(a, b) for a, b in zip(start, end) if a == b])
    #        == 2 for start, end in bricks):
    #     print('OK')

    bricks.sort(key=lambda x: min(x[0][2], x[1][2]))
    space = set()
    space_owners: dict[
        tuple[int, int, int], tuple[tuple[int, int, int], tuple[int, int, int]]
    ] = {}

    def intersection(
        s: tuple[int, int, int], e: tuple[int, int, int]
    ) -> set[tuple[tuple[int, int, int], tuple[int, int, int]]]:
        intersected = set()
        for x, y, z in zip_broadcast(
            range(s[0], e[0] + 1) if s[0] != e[0] else s[0],
            range(s[1], e[1] + 1) if s[1] != e[1] else s[1],
            range(s[2], e[2] + 1) if s[2] != e[2] else s[2],
        ):
            if (x, y, z) in space:
                intersected.add(space_owners[x, y, z])
        return intersected

    fallen_bricks = []
    supported_by: defaultdict[
        tuple[tuple[int, int, int], tuple[int, int, int]],
        set[tuple[tuple[int, int, int], tuple[int, int, int]]],
    ] = defaultdict(set)
    for s, e in bricks:
        while not (inter := intersection(s, e)) and s[2] > 0 and e[2] > 0:
            s = s[0], s[1], s[2] - 1
            e = e[0], e[1], e[2] - 1
        s = s[0], s[1], s[2] + 1
        e = e[0], e[1], e[2] + 1
        brick = (s, e)
        for i in inter:
            supported_by[brick].add(i)
        fallen_bricks.append(brick)
        for x, y, z in zip_broadcast(
            range(s[0], e[0] + 1) if s[0] != e[0] else s[0],
            range(s[1], e[1] + 1) if s[1] != e[1] else s[1],
            range(s[2], e[2] + 1) if s[2] != e[2] else s[2],
        ):
            space.add((x, y, z))
            space_owners[x, y, z] = brick
    return len(inp) - len(
        {
            next(iter(supports))
            for supports in supported_by.values()
            if len(supports) == 1
        }
    )


DAY = 22
FILE_TEST = f"{DAY}_test.txt"
FILE_EXP = f"{DAY}_expa.txt"
FILE = f"{DAY}.txt"
# test_and_submit(main, FILE_TEST, FILE_EXP, FILE, DAY)
print(main(FILE_TEST))
print(main(FILE))
