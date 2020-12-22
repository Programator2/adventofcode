from aocd import submit
from aoc import *
from collections import defaultdict, deque
from itertools import combinations
from pprint import pprint
from math import sqrt
import re


FILE = "22_test.txt"
FILE = "22.txt"


def main():
    inp = file(FILE)
    p1,p2 = inp.split('\n\n')
    p1 = p1.split('\n')[1:]
    p2 = p2.split('\n')[1:]
    print(p1)
    print()
    print(p2)
    p1 = [int(x) for x in p1]
    p2 = [int(x) for x in p2]
    hand1 = deque(p1)
    hand2 = deque(p2)
    out = 0
    while len(hand1) > 0 and len(hand2) > 0:
        if hand1[0] > hand2[0]:
            hand1.extend((hand1.popleft(), hand2.popleft()))
        else:
            hand2.extend((hand2.popleft(), hand1.popleft()))

    if len(hand1) > 0:
        h = hand1
    else:
        h = hand2
    score = 0
    for i, c in enumerate(h):
        score += (len(h)-i) * c
    out = score
    print(out)
    return
    input()
    print("submitting")
    submit(out)


main()
