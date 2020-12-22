from aocd import submit
from aoc import *
from collections import defaultdict, deque
from itertools import combinations
from pprint import pprint
from math import sqrt
import re
import functools


FILE = "22_test.txt"
FILE = "22.txt"


def recursive_combat(hand1, hand2):
    games = set()
    while len(hand1) > 0 and len(hand2) > 0:
        game = (tuple(hand1), tuple(hand2))
        if game in games:
            score = 0
            for i, c in enumerate(hand1):
                score += (len(hand1)-i) * c
            return 'player1'
        games.add(game)
        card1 = hand1.popleft()
        card2 = hand2.popleft()
        if card1 <= len(hand1) and card2 <= len(hand2):
            winner = recursive_combat(deque(list(hand1)[:card1]), deque(list(hand2)[:card2]))
            if winner == 'player1':
                hand1.extend((card1, card2))
            elif winner == 'player2':
                hand2.extend((card2, card1))
            else:
                hand1.extend((card1, card2))
                return 'instant'
        else:
            if card1 > card2:
                hand1.extend((card1, card2))
            else:
                hand2.extend((card2, card1))

    if len(hand1) > 0:
        return 'player1'
    else:
        return 'player2'


def main():
    inp = file(FILE).rstrip()
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
    games = set()
    winner = recursive_combat(hand1, hand2)
    if winner == 'instant':
        winner = 'player1'
    if winner == 'player1':
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
