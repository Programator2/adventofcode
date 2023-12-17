from aoc import *
from statistics import median, mode
from more_itertools import windowed, take, peekable, chunked, first_true, split_when, first_true
from heapq import *
# from functools import reduce, cache, cmp_to_key
from functools import cache
from math import ceil
import re
from blessed import BlessedList
from copy import deepcopy
import operator
from string import ascii_letters, ascii_lowercase, ascii_uppercase, digits, hexdigits, whitespace
from pprint import pprint as pp
import bisect
import math
from itertools import pairwise, combinations
import sys
from collections import defaultdict, OrderedDict, deque
# from ordered_set import OrderedSet


D = {'R': (0, 1), 'L': (0, -1), 'D': (1, 0), 'U': (-1, 0)}
POSSIBLE_MOVEMENTS = {'R': ('R', 'U', 'D'),
                      'L': ('L', 'D', 'U'),
                      'U': ('U', 'R', 'L'),
                      'D': ('D', 'R', 'L')}
TR = {'R': '>', 'L': '<', 'U': '^', 'D': 'v'}



def main(input_file: str):
    inp = load_map_dd(input_file)
    max_x = max(x for x, _ in inp.keys())
    max_y = max(y for _, y in inp.keys())
    total_loss = defaultdict(lambda: 999999)

    def dijkstra(source: tuple[int, int], dest: tuple[int, int]):
        assert source in inp
        inf = float('inf')
        q = set(inp.keys())
        neighbours = defaultdict(set)

        # Create all nodes
        start = deque([(0, 0, 'R', 0), (0, 0, 'D', 0)])
        while start:
            s = start.popleft()
            for move in POSSIBLE_MOVEMENTS[s[2]]:
                dx, dy = D[move]
                new_pos = (s[0] + dx, s[1] + dy)
                if new_pos in inp and (s[3] < 3 or s[2] != move):
                    new_node = (new_pos[0], new_pos[1], move,
                                (s[3] + 1) if s[2] == move else 0)
                    start.append(new_node)
                    neighbours[(s[0], s[1])].add(new_node)

        dist = {node: inf for node in neighbours}
        dist[(0, 0, 'R', 0)] = inf
        dist[(0, 0, 'D', 0)] = inf
        previous = {node: None for node in neighbours}
        previous[(0, 0, 'R', 0)] = None
        previous[(0, 0, 'D', 0)] = None
        dist[source] = 0

        #pp(neighbours)

        while q:
            # pp(q)
            u = min(q, key=lambda vertex: dist[vertex])
            q.remove(u)
            if dist[u] == inf or u == dest:
                break
            for v, cost in neighbours[u]:
                alt = dist[u] + cost
                if alt < dist[v]:                                  # Relax (u,v,a)
                    dist[v] = alt
                    previous[v] = u
        #pp(previous)
        s, u = deque(), dest
        while previous[u]:
            s.appendleft(u)
            u = previous[u]
        s.appendleft(u)
        return s

    # total_loss[(0, 0)] = 2
    # x, y, direction, steps in the same direction, total loss
    start = deque([(0, 0, 'R', 0, 0, [(0, 0, TR['R'])]), (0, 0, 'D', 0, 0, [(0, 0, TR['D'])])])
    start = deque([(0, 0, 'R', 0, 0, set([(0, 0)])), (0, 0, 'D', 0, 0, set([(0, 0)]))])
    while start:
        s = start.popleft()
        for move in POSSIBLE_MOVEMENTS[s[2]]:
            dx, dy = D[move]
            new_pos = (s[0] + dx, s[1] + dy)
            if new_pos in inp and (s[3] < 2 or s[2] != move) and new_pos not in s[5]:
                heat_loss = s[4] + inp[new_pos]
                if heat_loss > total_loss[new_pos]:
                    continue
                total_loss[new_pos] = heat_loss
                if new_pos != (max_x, max_y):
                    start.append((new_pos[0], new_pos[1], move,
                                  (s[3] + 1) if s[2] == move else 0, heat_loss,
                                  s[5] | set([new_pos])))
                                  # s[5] + [(*new_pos, TR[move])]))
                # else:
                    # best_trajectory = s[5] + [(*new_pos, TR[move])]
    # best_trajectory = {(x, y): v for x, y, v in best_trajectory}
    # for x in range(max_x):
        # for y in range(max_y):
            # if (x, y) in best_trajectory:
                # print(best_trajectory[(x, y)], end='')
            # else:
                # print(inp[(x, y)], end='')
        # print()
    return total_loss[(max_x, max_y)]


DAY = 17
FILE_TEST = f"{DAY}_test.txt"
FILE_EXP = f"{DAY}_exp.txt"
FILE = f"{DAY}.txt"
test_and_submit(main, FILE_TEST, FILE_EXP, FILE, DAY)
# print(main(FILE_TEST))
# print(main(FILE))
