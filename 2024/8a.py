from aoc import *
from itertools import combinations


def main(infi: str):
    inp = load_map_dd(infi)
    # maps letters and numbers to a list of positions
    antennas = defaultdict(list)
    maxi = max(i for i, _ in inp) + 1
    maxj = max(j for _, j in inp) + 1
    [
        antennas[inp[i, j]].append((i, j))
        for i, j in product(range(maxi), range(maxj))
        if inp[i,j] != '.'
    ]
    antinodes = set(
        (i, j)
        for antenna, positions in antennas.items()
        for a, b in combinations(positions, 2)
        for i, j in [
                (a[0] + a[0] - b[0], a[1] + a[1] - b[1]),
                (b[0] - (a[0] - b[0]), b[1] - (a[1] - b[1]))
        ]
        if 0 <= i < maxi and 0 <= j < maxj
    )
    return len(antinodes)


DAY = 8
FILE_TEST = f"{DAY}_testa.txt"
# FILE_TEST = f"{DAY}_testb.txt"
FILE_EXP = f"{DAY}_exp.txt"
FILE = f"{DAY}.txt"
# test_and_submit(main, FILE_TEST, FILE_EXP, FILE, DAY)
# print(main(FILE_TEST))
print(main(FILE))
