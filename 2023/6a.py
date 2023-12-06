from aoc import *
from functools import reduce, cache
import operator


def main(input_file: str):
    inp = lines(input_file)
    times = [int(x) for x in inp[0][5:].split()]
    distances = [int(x) for x in inp[1][9:].split()]
    won = []
    for t, d in zip(times, distances):
        win = 0
        for i in range(0, t + 1):
            speed = i
            move = (t - i) * speed
            if move > d:
                win += 1
        won.append(win)
    return reduce(operator.mul, won, 1)


DAY = 6
FILE_TEST = f"{DAY}_test.txt"
FILE_EXP = f"{DAY}_expa.txt"
FILE = f"{DAY}.txt"
# test_and_submit(main, FILE_TEST, FILE_EXP, FILE)
print(main(FILE_TEST))
print(main(FILE))
