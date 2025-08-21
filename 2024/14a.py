from aoc import *
import re


def main(infi: str):
    inp = lines_stripped(infi)
    width = 101
    height = 103
    # width = 11
    # height = 7
    robots = []
    for l in inp:
        match = re.fullmatch(r'^p=(.*),(.*) v=(.*),(.*)$', l)
        robot = tuple(map(int, match.groups()))
        robots.append([(robot[0], robot[1]), (robot[2], robot[3])])
    for _ in range(100):
        for r in robots:
            newpos = (
                (r[0][0] + r[1][0]) % width,
                (r[0][1] + r[1][1]) % height,
            )
            r[0] = newpos
    # fmt: off
    q1 = sum(1 for r in robots if r[0][0] < (width // 2) and r[0][1] < (height // 2))
    q2 = sum(1 for r in robots if r[0][0] > (width // 2) and r[0][1] < (height // 2))
    q3 = sum(1 for r in robots if r[0][0] < (width // 2) and r[0][1] > (height // 2))
    q4 = sum(1 for r in robots if r[0][0] > (width // 2) and r[0][1] > (height // 2))
    # fmt: on
    # for r in robots:
    #     print(r)
    # print(q1, q2, q3, q4)
    return q1 * q2 * q3 * q4


DAY = 14
FILE_TEST = f"{DAY}_testa.txt"
# FILE_TEST = f"{DAY}_testb.txt"
FILE_EXP = f"{DAY}_exp.txt"
FILE = f"{DAY}.txt"
# test_and_submit(main, FILE_TEST, FILE_EXP, FILE, DAY)
# print(main(FILE_TEST))
print(main(FILE))
