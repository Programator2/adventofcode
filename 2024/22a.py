from aoc import *


def main(infi: str):
    inp = load_ints(infi)
    s = 0
    for n in inp:
        for i in range(2000):
            n = (n * 64 ^ n) % 16777216
            n = (n // 32 ^ n) % 16777216
            n = (n * 2048 ^ n) % 16777216
        s += n
    return s


DAY = 22
FILE_TEST = f"{DAY}_testa.txt"
# FILE_TEST = f"{DAY}_testb.txt"
FILE_EXP = f"{DAY}_exp.txt"
FILE = f"{DAY}.txt"
# test_and_submit(main, FILE_TEST, FILE_EXP, FILE, DAY)
# print(main(FILE_TEST))
print(main(FILE))
