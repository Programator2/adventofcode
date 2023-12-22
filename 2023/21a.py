from aoc import *
from functools import cache


S = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def main(input_file: str):
    m = load_map_dd(input_file)

    @cache
    def step(x, y):
        return {(x + dx, y + dy) for dx, dy in S if m[(x + dx, y + dy)] in ['.', 'S']}

    places = {(x, y) for (x, y), c in m.items() if c == 'S'}
    for i in range(64):
        new_places = set()
        for x, y in places:
            new_places.update(step(x, y))
        places = new_places

    # maxx = max(x for x, y in m)
    # maxy = max(y for x, y in m)
    # for ri in range(maxx + 1):
    #     for ci in range(maxy + 1):
    #         if (ri, ci) in places:
    #             print('O', end='')
    #         else:
    #             print(m[(ri, ci)], end='')
    #     print()

    return len(places)

DAY = 21
FILE = f"{DAY}.txt"
print(main(FILE))
