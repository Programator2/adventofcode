from aoc import *


dir = [(1, 0), (0, 1), (1, 1), (-1, 0), (0, -1), (-1, 1), (1, -1), (-1, -1)]
tofind = ['XMAS']


def search(i, j, inp):
    s = 0
    for d in dir:
        pos = (i, j)
        for word in tofind:
            for l in word:
                if pos not in inp or inp[pos] != l:
                    break
                pos = (pos[0] + d[0], pos[1] + d[1])
            else:
                s += 1
    return s


def main(infi: str):
    inp = load_map_dd(infi)
    maxi = max(i for i, _ in inp) + 1
    maxj = max(j for _, j in inp) + 1
    return sum(search(i, j, inp) for j in range(maxj) for i in range(maxi))


DAY = 4
FILE_TEST = f"{DAY}_testa.txt"
# FILE_TEST = f"{DAY}_testb.txt"
FILE_EXP = f"{DAY}_exp.txt"
FILE = f"{DAY}.txt"
# test_and_submit(main, FILE_TEST, FILE_EXP, FILE, DAY)
# print(main(FILE_TEST))
print(main(FILE))
