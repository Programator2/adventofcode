from aocd import submit
from aoc import *
from functools import cache
from itertools import product


def main():
    # print(max(throw(4, 0, 8, 0)))
    print(max(throw(9, 0, 3, 0)))


@cache
def throw(posa: int, pointsa: int, posb: int, pointsb: int):
    awin = 0
    bwin = 0
    for throwa in product((1, 2, 3), repeat=3):
        points = sum(throwa)
        newposa = (posa + points) % 10
        newposa = 10 if (newposa == 0) else newposa
        newpointsa = pointsa + newposa

        if newpointsa >= 21:
            awin += 1
            continue
        for throwb in product((1, 2, 3), repeat=3):
            points = sum(throwb)
            newposb = (posb + points) % 10
            newposb = 10 if (newposb == 0) else newposb
            newpointsb = pointsb + newposb

            if newpointsb >= 21:
                bwin += 1
                continue

            a, b = throw(newposa, newpointsa, newposb, newpointsb)
            awin += a
            bwin += b
    return awin, bwin


DAY = 21
FILE_TEST = f"{DAY}_test.txt"
FILE_EXP = f"{DAY}_exp.txt"
FILE = f"{DAY}.txt"
# test_and_submit(main, FILE_TEST, FILE_EXP, FILE)
main()
