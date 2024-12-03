from aoc import *
import re


def main(infi: str):
    return sum(
        int(a) * int(b)
        for a, b in re.findall(r'mul\((\d{1,3}),(\d{1,3})\)', filerstrip(infi))
    )


DAY = 3
FILE_TEST = f"{DAY}_testa.txt"
# FILE_TEST = f"{DAY}_testb.txt"
FILE_EXP = f"{DAY}_exp.txt"
FILE = f"{DAY}.txt"
# test_and_submit(main, FILE_TEST, FILE_EXP, FILE, DAY)
# print(main(FILE_TEST))
print(main(FILE))
