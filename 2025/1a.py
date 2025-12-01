from aoc import *


def main(infi: str):
    inp = lines_stripped(infi)
    start = 50
    i = 0
    for a in inp:
        way = a[0]
        num = int(a[1:])
        if way == 'L':
            start = (start - num) % 100
        else:
            start = (start + num) % 100
        if start == 0:
            i += 1
    return i


DAY = 1
FILE_TEST = f"{DAY}_testa.txt"
# FILE_TEST = f"{DAY}_testb.txt"
FILE_EXP = f"{DAY}_exp.txt"
FILE = f"{DAY}.txt"
# test_and_submit(main, FILE_TEST, FILE_EXP, FILE, DAY)
# print(main(FILE_TEST))
print(main(FILE))
