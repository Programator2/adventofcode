from aoc import *
from more_itertools import zip_broadcast
from pprint import pprint as pp
from collections import defaultdict


def search(node, di, falling, supported_by):
    falling[node] = True
    s = set()
    for n in di[node]:
        # Check if the brick is really falling. Another brick may still be
        # supporting it.
        if all(falling[s] for s in supported_by[n]):
            # All bricks above `n` it must be falling.
            falling[n] = True
            s.add(n)
    for n in s.copy():
        s.update(search(n, di, falling, supported_by))
    return s


def main(input_file: str):
    inp = lines(input_file)
    bricks = []
    for l in inp:
        start, end = l.split('~')
        start = [int(x) for x in start.split(',')]
        end = [int(x) for x in end.split(',')]
        bricks.append((start, end))

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

    # This list contains positions of bricks after they fall into static state
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

    # Reversed graph. Means key brick supports bricks in the set
    supports_ = defaultdict(set)
    for ciel, zdroje in supported_by.items():
        for z in zdroje:
            supports_[z].add(ciel)

    # Fragile bricks are those that would cause falling of other bricks if one
    # of them are removed
    fragile = {
        next(iter(supports))
        for supports in supported_by.values()
        if len(supports) == 1
    }
    suma = 0
    for f in fragile:
        # Store falling state in this dictionary
        falling = defaultdict(lambda: False)
        suma += len(search(f, supports_, falling, supported_by))
    return suma


DAY = 22
FILE_TEST = f"{DAY}_test.txt"
FILE_EXP = f"{DAY}_expb.txt"
FILE = f"{DAY}.txt"
# test_and_submit(main, FILE_TEST, FILE_EXP, FILE, DAY)
print(main(FILE_TEST))
print(main(FILE))
