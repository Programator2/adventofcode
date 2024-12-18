from aoc import *
from more_itertools import windowed


def main(infi: str):
    inp = lines_stripped(infi)
    safe = 0
    for l in inp:
        twos = list(windowed(map(int, l.split()), 2))
        check = any(
            [all([a > b for a, b in twos]), all([a < b for a, b in twos])]
        )
        if not check:
            continue
        t = max(abs(a - b) for a, b in twos)
        if t > 3:
            continue
        else:
            safe += 1
    return safe


DAY = 2
FILE_TEST = f"{DAY}_testa.txt"
# FILE_TEST = f"{DAY}_testb.txt"
FILE_EXP = f"{DAY}_exp.txt"
FILE = f"{DAY}.txt"
# test_and_submit(main, FILE_TEST, FILE_EXP, FILE, DAY)
# print(main(FILE_TEST))
print(main(FILE))
