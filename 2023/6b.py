from aoc import *
from functools import reduce
import operator


def main(input_file: str):
    inp = lines(input_file)
    t = int(inp[0][5:].replace(' ', ''))
    d = int(inp[1][9:].replace(' ', ''))
    win = 0
    for i in range(0, t + 1):
        speed = i
        move = (t - i) * speed
        if move > d:
            win += 1
    return win


DAY = 6
FILE_TEST = f"{DAY}_test.txt"
FILE_EXP = f"{DAY}_expb.txt"
FILE = f"{DAY}.txt"
# test_and_submit(main, FILE_TEST, FILE_EXP, FILE)
print(main(FILE_TEST))
print(main(FILE))
