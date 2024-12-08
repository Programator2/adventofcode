from aoc import *
from itertools import combinations


def main(infi: str):
    inp = load_map_dd(infi)
    # maps letters and numbers to a list of positions
    antennas = defaultdict(list)
    antinodes = set()
    maxi = max(i for i, _ in inp) + 1
    maxj = max(j for _, j in inp) + 1
    pos = None
    for i in range(maxi):
        for j in range(maxj):
            if inp[i,j] != '.':
                antennas[inp[i, j]].append((i, j))
    for antenna, positions in antennas.items():
        for a, b in combinations(positions, 2):
            diff = a[0] - b[0], a[1] - b[1]
            an1 = a[0] + diff[0], a[1] + diff[1]
            an2 = b[0] - diff[0], b[1] - diff[1]
            for i, j in (an1, an2):
                if i < 0 or j < 0 or i >= maxi or j >= maxj:
                    continue
                antinodes.add((i, j))
    return len(antinodes)

DAY = 8
FILE_TEST = f"{DAY}_testa.txt"
# FILE_TEST = f"{DAY}_testb.txt"
FILE_EXP = f"{DAY}_exp.txt"
FILE = f"{DAY}.txt"
# test_and_submit(main, FILE_TEST, FILE_EXP, FILE, DAY)
# print(main(FILE_TEST))
print(main(FILE))
