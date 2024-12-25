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


def generate_distances():
    diffs = set()
    for i in range(2, 21):
        for a in range(i):
            b = i - a
            diffs.update(
                {
                    (a, b),
                    (a, -b),
                    (-a, b),
                    (-a, -b),
                    (b, a),
                    (b, -a),
                    (-b, a),
                    (-b, -a),
                }
            )
    return diffs


def main(infi: str):
    sys.setrecursionlimit(10000)
    inp = load_map_dd(infi)
    end = [(i, j) for (i, j), e in inp.items() if e == 'E'][0]
    lengths = {}
    search(*end, inp, lengths, 0)
    distances = generate_distances()
    s = 0
    for (i, j), e in inp.items():
        if e in '.SE':
            for a, b in distances:
                if inp.get((i + a, j + b), None) in ['.', 'E', 'S']:
                    length = (
                        lengths[i + a, j + b]
                        - lengths[i, j]
                        - (abs(a) + abs(b))
                    )
                    if length >= 100:
                        s += 1
    return s


DAY = 20
FILE_TEST = f"{DAY}_testa.txt"
# FILE_TEST = f"{DAY}_testb.txt"
FILE_EXP = f"{DAY}_exp.txt"
FILE = f"{DAY}.txt"
# test_and_submit(main, FILE_TEST, FILE_EXP, FILE, DAY)
# print(main(FILE_TEST))
print(main(FILE))
