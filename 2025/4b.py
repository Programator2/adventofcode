from aoc import *


def main(infi: str):
    inp = load_map_dd(infi)
    removed = True
    fin = 0
    while removed:
        removed = False
        new = inp.copy()
        for (a, b), roll in inp.items():
            if roll != '@':
                continue
            s = 0
            for di, dj in (
                (1, 0),
                (0, 1),
                (-1, 0),
                (0, -1),
                (1, 1),
                (-1, -1),
                (-1, 1),
                (1, -1),
            ):
                pos = a + di, b + dj
                if inp.get(pos) == '@':
                    s += 1
            if s < 4:
                new[a, b] = '.'
                fin += 1
                removed = True
        inp = new
    return fin


DAY = 4
FILE_TEST = f"{DAY}_testa.txt"
# FILE_TEST = f"{DAY}_testb.txt"
FILE_EXP = f"{DAY}_exp.txt"
FILE = f"{DAY}.txt"
# test_and_submit(main, FILE_TEST, FILE_EXP, FILE, DAY)
# print(main(FILE_TEST))
print(main(FILE))
