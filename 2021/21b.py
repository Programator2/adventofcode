from aocd import submit
from aoc import *
import re
from blessed import BlessedList
from collections import namedtuple, defaultdict, Counter, deque
from copy import deepcopy
from math import ceil
# from functools import cache
from statistics import mode
from more_itertools import windowed, chunked
from itertools import product, accumulate, permutations, cycle, combinations_with_replacement
import operator
from string import ascii_uppercase
from pprint import pprint as pp
from heapq import *
import itertools
from more_itertools import take, peekable
from functools import reduce as red


def help():
    c = Counter(sum(x) for x in product(range(1, 4), repeat=3))
    print(c)


def get_points(i: int):
    """Compute points from a full position on the board.

    >>> get_points(10)
    10
    >>> get_points(11)
    1
    >>> get_points(20)
    10
    >>> get_points(21)
    1
    """
    i = i % 10
    if i == 0:
        return 10
    return i


def player(starta: int, startb: int):
    occurences = (1, 3, 6, 7, 6, 3, 1)

    throws = {0: {starta:Counter((0,))}}
    throwsb = {0: {startb:Counter((0,))}}
    nthrow = 1
    winnings = Counter()        # Counts number of winnings at a given throw
    winnings_sum = Counter()
    unwinnings = Counter((0,))             # Counts number of unwins after a throw
    unwinnings_sum = Counter((0,))
    winningsb = Counter()        # Counts number of winnings at a given throw
    winningsb_sum = Counter()
    unwinningsb = Counter((0,))             # Counts number of unwins after a throw
    unwinningsb_sum = Counter((0,))

    while True:
        # Player A
        throwplus = defaultdict(Counter)
        throws[nthrow] = throwplus
        for i, occ in enumerate(occurences, 3):
            for position, counter in throws[nthrow-1].items():
                won = False
                for points, times in counter.items():
                    new_points = points + get_points(position + i)
                    if new_points >= 21:
                        winnings[nthrow] += times * occ
                        # won = True
                        # do not add winning ones so that alg stops
                        winnings_sum[nthrow] += occ * unwinningsb_sum[nthrow-1]
                        break
                    throwplus[position+i][points+get_points(position+i)] = times + occ
                # if won:
                unwinnings_sum[nthrow] += occ * unwinningsb_sum[nthrow-1]
        unwinnings[nthrow] = sum(sum(times) for times in (counter.values() for counter in throwplus.values())) * unwinningsb[nthrow-1]
        # nthrow += 1

        if unwinnings_sum[nthrow] == 0:
            break

        # Player B
        throwplusb = defaultdict(Counter)
        throwsb[nthrow] = throwplusb
        for i, occ in enumerate(occurences, 3):
            for position, counter in throwsb[nthrow-1].items():
                won = False
                for points, times in counter.items():
                    new_points = points+get_points(position+i)
                    if new_points >= 21:
                        winningsb[nthrow] += times * occ
                        # won = True
                        winningsb_sum[nthrow] += occ * unwinnings_sum[nthrow]
                        # do not add winning ones so that alg stops
                        break
                    throwplusb[position+i][points+get_points(position+i)] = times + occ
                unwinningsb_sum[nthrow] += occ * unwinnings_sum[nthrow]
                # if won:
        unwinningsb[nthrow] = sum(sum(times) for times in (counter.values() for counter in throwplusb.values())) * unwinnings[nthrow-1]

        if unwinningsb_sum[nthrow] == 0:
            break

        nthrow += 1
    print(winnings)
    print(winningsb)
    # print(unwinnings_sum)
    # print(unwinningsb_sum)


    # return winnings, unwinnings


def get_winnings(wina, unwina, winb, unwinb, this: int, throw: int):
    """
    Get # of universes in which player this wins after `throw`
    this: 0 if a, 1 if b
    """
    if this:
        mewin = winb
        meunwin = unwinb
        otherwin = wina
        otherunwin = unwina
    else:
        mewin = wina
        meunwin = unwina
        otherwin = winb
        otherunwin = unwinb
    nwins = mewin[throw]
    # for i in range(1, throw):
        # nwins *= unwina[i]
        # nwins *= unwinb[i]
    # if this:
        # nwins *= unwina[throw]
    # return nwins
    if this == 0:
        return nwins * unwinb[throw-1]
    else:
        return nwins * unwina[throw]


def main2():
    player(4, 8)
    # print(wina)
    # winb, unwinb = player(8)
    # print(unwina)
    # print(unwinb)
    # return
    # print(winb)
    # print(wina)
    # latest_wina = max(wina.keys())
    # latest_winb = max(winb.keys())
    # latest_win = min(latest_wina, latest_winb)
    # players = list(list(zip(wina, )), list(zip(winb, unwinb)))
    # for throw, times in wina.items():
    # playera_wins = sum(get_winnings(wina, unwina, winb, unwinb, 0, i) for i in wina.keys() if i <= latest_win)
    # print(playera_wins)
    # print(unwina[1])
    # print(player(8))


def main(a, b):
    help()
    return
    # inp = file(input_file).rstrip()
    # a = 9
    # b = 3
    scorea = 0
    scoreb = 0
    roll = 0
    i = chunked(cycle(range(1, 101)), 3)
    while True:
        points = sum(next(i))
        a = (a+points) % 10
        a = 10 if a == 0 else a
        roll += 3
        scorea += a
        # print(f'player a rolls {points} and moves to {a} for total {scorea}')
        if scorea >= 1000:
            return scoreb * roll
        h = next(i)
        # print(h)
        points = sum(h)
        b = (b+points) % 10
        b = 10 if b == 0 else b
        roll += 3
        scoreb += b
        # print(f'player b rolls {points} and moves to {b} for total {scoreb}')
        if scoreb >= 1000:
            return scorea * roll
    out = 0
    return out


DAY = 21
FILE_TEST = f"{DAY}_test.txt"
FILE_EXP = f"{DAY}_exp.txt"
FILE = f"{DAY}.txt"
# test_and_submit(main, FILE_TEST, FILE_EXP, FILE)
# print(main(4, 8))
# print(main(9, 3))
main2()

# 274790922411600
