from aoc import *

dir = [(1, 0), (0, 1), (1, 1), (-1, 0), (0, -1), (-1, 1), (1, -1), (-1, -1)]
tofind = ['XMAS']


def search(i, j, inp):
    s = 0
    if (
        (
            inp[0 + i, 0 + j] == 'M'
            and inp[0 + i, 2 + j] == 'M'
            and inp[1 + i, 1 + j] == 'A'
            and inp[2 + i, 0 + j] == 'S'
            and inp[2 + i, 2 + j] == 'S'
        )
        or (
            inp[0 + i, 0 + j] == 'M'
            and inp[0 + i, 2 + j] == 'S'
            and inp[1 + i, 1 + j] == 'A'
            and inp[2 + i, 0 + j] == 'M'
            and inp[2 + i, 2 + j] == 'S'
        )
        or (
            inp[0 + i, 0 + j] == 'S'
            and inp[0 + i, 2 + j] == 'S'
            and inp[1 + i, 1 + j] == 'A'
            and inp[2 + i, 0 + j] == 'M'
            and inp[2 + i, 2 + j] == 'M'
        )
        or (
            inp[0 + i, 0 + j] == 'S'
            and inp[0 + i, 2 + j] == 'M'
            and inp[1 + i, 1 + j] == 'A'
            and inp[2 + i, 0 + j] == 'S'
            and inp[2 + i, 2 + j] == 'M'
        )
    ):
        s += 1
    return s


def main(infi: str):
    inp = load_map_dd(infi)
    maxi = max(i for i, _ in inp) + 1
    maxj = max(j for _, j in inp) + 1
    return sum(
        search(i, j, inp) for j in range(maxj - 2) for i in range(maxi - 2)
    )


DAY = 4
FILE_TEST = f"{DAY}_testa.txt"
# FILE_TEST = f"{DAY}_testb.txt"
FILE_EXP = f"{DAY}_exp.txt"
FILE = f"{DAY}.txt"
# test_and_submit(main, FILE_TEST, FILE_EXP, FILE, DAY)
# print(main(FILE_TEST))
print(main(FILE))
