from aoc import *
from collections import defaultdict


D = [(-1, 0), (1, 0), (0, -1), (0, 1)]
D_slope = {
    '^': [(-1, 0)],
    'v': [(1, 0)],
    '>': [(0, 1)],
    '<': [(0, -1)],
}


def search(x, y, visited, inp, max_walk):
    while True:
        possible = []
        visited.add((x, y))
        max_walk[x, y] = max(len(visited), max_walk[x, y])
        d = D
        if inp[x, y] in ['^', '>', 'v', '<']:
            d = D_slope[inp[x, y]]
        for dx, dy in d:
            new_x, new_y = x + dx, y + dy
            new_pos = new_x, new_y
            if (
                new_pos in inp
                and inp[new_pos] in ['.', '^', '>', 'v', '<']
                and new_pos not in visited
            ):
                possible.append(new_pos)
        if len(possible) == 1:
            x, y = possible[0]
            continue
        elif possible:
            for x, y in possible:
                search(x, y, visited.copy(), inp, max_walk)
            break
        break


def main(input_file: str):
    inp = load_map_dd(input_file)
    maxx = max(x for x, y in inp)
    maxy = max(y for x, y in inp)
    visited = set()
    max_walk = defaultdict(int)
    search(0, 1, visited, inp, max_walk)
    return max_walk[maxx, maxy - 1] - 1


DAY = 23
FILE_TEST = f"{DAY}_test.txt"
FILE_EXP = f"{DAY}_expa.txt"
FILE = f"{DAY}.txt"
# test_and_submit(main, FILE_TEST, FILE_EXP, FILE, DAY)
print(main(FILE_TEST))
print(main(FILE))
