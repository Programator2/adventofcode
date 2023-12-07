from aoc import *
from collections import Counter
from functools import cmp_to_key
from operator import itemgetter


strength = {
    'A': 13,
    'K': 12,
    'Q': 11,
    'T': 9,
    '9': 8,
    '8': 7,
    '7': 6,
    '6': 5,
    '5': 4,
    '4': 3,
    '3': 2,
    '2': 1,
    'J': 0,
}


def comp_type(hand: str):
    c = Counter(hand)
    if len(c) == 1:
        return 7 # five of a kind
    if len(c) == 2 and 4 in c.values():
        if 'J' in c:
            # AAAAJ -> AAAAA
            return 7
        return 6 # four of a kind
    if len(c) == 2 and set(c.values()) == {2, 3}:
        if 'J' in c:
            # JJJAA -> AAAAA
            # AAAJJ -> AAAAA
            return 7
        return 5 # full house
    if 3 in c.values():
        if 'J' in c:
            # JJJAB -> AAAAB, BBBAB
            # AAAJB -> AAAAB
            return 6
        return 4 # three of a kind
    if Counter(c.values())[2] == 2:
        if c['J'] == 1:
            # AABBJ -> AABBA, AABBB
            return 5
        if c['J'] == 2:
            # JJAAB -> AAAAB
            return 6
        return 3 # two pairs
    if 2 in c.values():
        if 'J' in c:
            # AAJBC -> AAABC
            # JJABC -> AAABC, BBABC, CCABC
            return 4
        return 2 # one pair
    if 'J' in c:
        # JABCD -> AABCD, BABCD, CABCD, DABCD
        return 2
    return 1

def comp_same_type(first, second):
    for i, j in zip(first, second):
        if strength[i] > strength[j]:
            return 1
        elif strength[i] < strength[j]:
            return -1


def compare(first, second):
    first, second = map(itemgetter(0), (first, second))
    aa, bb = map(comp_type, (first, second))
    if aa == bb:
        return comp_same_type(first, second)
    if aa > bb:
        return 1
    return -1


def main(input_file: str):
    cards = sorted([x.split() for x in lines(input_file)], key=cmp_to_key(compare))
    return sum([int(c[1]) * i for i, c in zip(range(1, len(cards)+1), cards)])


DAY = 7
FILE_TEST = f"{DAY}_test.txt"
FILE_EXP = f"{DAY}_expb.txt"
FILE = f"{DAY}.txt"
# test_and_submit(main, FILE_TEST, FILE_EXP, FILE)
print(main(FILE_TEST))
print(main(FILE))
