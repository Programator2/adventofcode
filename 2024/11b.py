from aoc import *
from functools import cache


@cache
def rec(num: int, depth: int):
    if depth == 0:
        return 1
    if num == 0:
        return rec(1, depth - 1)
    elif (lennum := len(strnum := str(num))) % 2 == 0:
        return rec(int(strnum[: lennum // 2]), depth - 1) + rec(
            int(strnum[lennum // 2 :]), depth - 1
        )
    else:
        return rec(num * 2024, depth - 1)


def main(infi: str):
    return sum(rec(int(x), 75) for x in load_ints_split(infi, ' '))


DAY = 11
FILE_TEST = f"{DAY}_testa.txt"
# FILE_TEST = f"{DAY}_testb.txt"
FILE_EXP = f"{DAY}_exp.txt"
FILE = f"{DAY}.txt"
# test_and_submit(main, FILE_TEST, FILE_EXP, FILE, DAY)
# print(main(FILE_TEST))
print(main(FILE))
