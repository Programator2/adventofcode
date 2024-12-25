from aoc import *
from itertools import product


def main(infi: str):
    locks = []
    keys = []
    for o in filerstrip(infi).split('\n\n'):
        lines = o.split('\n')
        flist = keys if lines[0] == '.....' else locks
        template = list(lines[0])
        heights = [0] * 5
        for height, l in enumerate(lines[1:]):
            for i, (a, b) in enumerate(zip(l, template)):
                if a != b:
                    heights[i] = height if flist is locks else 5 - height
                    template[i] = a
        flist.append(heights)
    return sum(
        1
        for k, l in product(keys, locks)
        if all(a + b <= 5 for a, b in zip(k, l))
    )


DAY = 25
FILE_TEST = f"{DAY}_testa.txt"
# FILE_TEST = f"{DAY}_testb.txt"
FILE_EXP = f"{DAY}_exp.txt"
FILE = f"{DAY}.txt"
# test_and_submit(main, FILE_TEST, FILE_EXP, FILE, DAY)
# print(main(FILE_TEST))
print(main(FILE))
