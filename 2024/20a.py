from aoc import *
import sys


DIRS = ((-1, 0), (0, 1), (1, 0), (0, -1))


def search(i, j, m, lengths, length):
    """
    :param lengths: lengths from the end
    """
    togo = []
    for d in DIRS:
        pos = i + d[0], j + d[1]
        if (
            pos in m
            and m[pos] in '.SE'
            and (pos not in lengths or lengths[pos] > length + 1)
        ):
            lengths[pos] = length + 1
            togo.append(pos)
    for pos in togo:
        search(*pos, m, lengths, length + 1)


def main(infi: str):
    sys.setrecursionlimit(10000)
    inp = load_map_dd(infi)
    end = [(i, j) for (i, j), e in inp.items() if e == 'E'][0]
    lengths = {}
    search(*end, inp, lengths, 0)
    s = 0
    for (i, j), e in inp.items():
        if e == '#':
            connected = [
                (i + d[0], j + d[1])
                for d in DIRS
                if (i + d[0], j + d[1]) in inp
                and inp[i + d[0], j + d[1]] in '.SE'
            ]
            if len(connected) == 2:
                length = abs(lengths[connected[0]] - lengths[connected[1]]) - 2
                if length >= 100:
                    s += 1
            elif len(connected) > 2:
                continue
    return s


DAY = 20
FILE_TEST = f"{DAY}_testa.txt"
# FILE_TEST = f"{DAY}_testb.txt"
FILE_EXP = f"{DAY}_exp.txt"
FILE = f"{DAY}.txt"
# test_and_submit(main, FILE_TEST, FILE_EXP, FILE, DAY)
# print(main(FILE_TEST))
print(main(FILE))
