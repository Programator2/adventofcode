from aoc import *
from itertools import pairwise, product
from functools import cache

numkey = {
    7: (0, 0),
    8: (0, 1),
    9: (0, 2),
    4: (1, 0),
    5: (1, 1),
    6: (1, 2),
    1: (2, 0),
    2: (2, 1),
    3: (2, 2),
    0: (3, 1),
    'A': (3, 2),
}
numkey_positions = set(numkey.values())

dirkey = {
    '^': (0, 1),
    'A': (0, 2),
    '<': (1, 0),
    'v': (1, 1),
    '>': (1, 2),
}
dirkey_positions = set(dirkey.values())

DIRS = ((-1, 0), (0, 1), (1, 0), (0, -1))
KEY_TO_DIR = {
    '^': (-1, 0),
    '>': (0, 1),
    'v': (1, 0),
    '<': (0, -1),
}


def is_ok(start, sequence, keypad_positions):
    positions = [start]
    for press in sequence:
        positions.append(
            (
                positions[-1][0] + KEY_TO_DIR[press][0],
                positions[-1][1] + KEY_TO_DIR[press][1],
            )
        )
    return all(pos in keypad_positions for pos in positions)


def find_shortest(f, t, postrans, keypad_positions):
    fpos = postrans[f]
    tpos = postrans[t]
    diff = fpos[0] - tpos[0], fpos[1] - tpos[1]
    charh = '<' if diff[1] > 0 else '>'
    charv = '^' if diff[0] > 0 else 'v'
    possible = {
        tuple(charh * abs(diff[1])) + tuple(charv * abs(diff[0])),
        tuple(charv * abs(diff[0])) + tuple(charh * abs(diff[1])),
    }
    possible = list(
        filter(lambda x: is_ok(fpos, x, keypad_positions), possible)
    )
    return possible


@cache
def shortest_numpad(src: int | str, dest: int | str, depth: int):
    seq = []
    for path in numkey_paths[src, dest]:
        # path = numkey_paths[src, dest][0]
        # seq = ''
        s = 0
        for nsrc, ndest in pairwise(('A',) + path + ('A',)):
            s += shortest_dir(nsrc, ndest, depth)
        seq.append(s)
    return min(seq)


@cache
def shortest_dir(src: str, dest: str, depth: int):
    if not depth:
        return 1
        return dest
    seq = []
    for path in dirkey_paths[src, dest]:
        # seq = ''
        s = 0
        for nsrc, ndest in pairwise(('A',) + path + ('A',)):
            s += shortest_dir(nsrc, ndest, depth - 1)
        seq.append(s)
    return min(seq)


def main(infi: str, depth: int):
    inp = lines_stripped(infi)
    global numkey_paths
    global dirkey_paths
    numkey_paths = {
        (fromto[0], fromto[1]): find_shortest(*fromto, numkey, numkey_positions)
        for fromto in product(numkey.keys(), repeat=2)
    }
    dirkey_paths = {
        (fromto[0], fromto[1]): find_shortest(*fromto, dirkey, dirkey_positions)
        for fromto in product(dirkey.keys(), repeat=2)
    }

    s = 0
    for l in inp:
        numbers = list(map(int, l[:-1]))
        path = tuple(numbers + list(l[-1]))
        seq = 0
        for nsrc, ndest in pairwise(('A',) + path):
            adding = shortest_numpad(nsrc, ndest, depth)
            seq += adding
        s += seq * int(l[:-1])

    return s


DAY = 21
FILE_TEST = f"{DAY}_testa.txt"
# FILE_TEST = f"{DAY}_testb.txt"
FILE_EXP = f"{DAY}_exp.txt"
FILE = f"{DAY}.txt"
# test_and_submit(main, FILE_TEST, FILE_EXP, FILE, DAY)
# print(main(FILE_TEST))
print(main(FILE, 2))
print(main(FILE, 25))
