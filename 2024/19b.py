from aoc import *
from functools import cache


def main(infi: str):
    inp = filerstrip(infi)
    patterns, designs = inp.split('\n\n')
    patterns = set(patterns.split(', '))
    max_pattern = max(len(x) for x in patterns)
    designs = designs.split('\n')

    @cache
    def search(design):
        s = 0
        if not design:
            return 1
        return sum(
            search(design[i:])
            for i in range(1, min(len(design) + 1, max_pattern + 1))
            if design[:i] in patterns
        )

    return sum(search(d) for d in designs)


DAY = 19
FILE_TEST = f"{DAY}_testa.txt"
# FILE_TEST = f"{DAY}_testb.txt"
FILE_EXP = f"{DAY}_exp.txt"
FILE = f"{DAY}.txt"
# test_and_submit(main, FILE_TEST, FILE_EXP, FILE, DAY)
# print(main(FILE_TEST))
print(main(FILE))
