from aoc import *
from itertools import combinations


def main(infi: str):
    inp = load_map_dd(infi)
    # maps letters and numbers to a list of positions
    antennas = defaultdict(list)
    antinodes = set()
    maxi = max(i for i, _ in inp) + 1
    maxj = max(j for _, j in inp) + 1
    [
        antennas[inp[i, j]].append((i, j))
        for i, j in product(range(maxi), range(maxj))
        if inp[i,j] != '.'
    ]
    for antenna, positions in antennas.items():
        for a, b in combinations(positions, 2):
            diff = a[0] - b[0], a[1] - b[1]
            an = a[0] + diff[0], a[1] + diff[1]
            while an[0] >= 0 and an[1] >= 0 and an[0] < maxi and an[1] < maxj:
                antinodes.add((an[0], an[1]))
                an = an[0] + diff[0], an[1] + diff[1]
            an = b[0] - diff[0], b[1] - diff[1]
            while an[0] >= 0 and an[1] >= 0 and an[0] < maxi and an[1] < maxj:
                antinodes.add((an[0], an[1]))
                an = an[0] - diff[0], an[1] - diff[1]
            antinodes.add((a[0], a[1]))
            antinodes.add((b[0], b[1]))
    return len(antinodes)


DAY = 8
FILE_TEST = f"{DAY}_testa.txt"
# FILE_TEST = f"{DAY}_testb.txt"
FILE_EXP = f"{DAY}_exp.txt"
FILE = f"{DAY}.txt"
# test_and_submit(main, FILE_TEST, FILE_EXP, FILE, DAY)
# print(main(FILE_TEST))
print(main(FILE))
