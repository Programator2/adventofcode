from aoc import *
from functools import cache
from collections import Counter


S = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def main(input_file: str):
    m = load_map_dd(input_file)
    maxx = max(x for x, y in m)
    sizex = maxx + 1  # 131
    maxy = max(y for x, y in m)
    sizey = maxy + 1  # 131

    @cache
    def step(x, y):
        return {
            ((x + dx), (y + dy))
            for dx, dy in S
            if m[((x + dx) % (maxx + 1), (y + dy) % (maxy + 1))] in ['.', 'S']
        }

    places = {(x, y) for (x, y), c in m.items() if c == 'S'}
    c = Counter()
    c[next(iter(places))] = 1
    start = next(iter(places))
    m[start] = '.'
    steps = 26501365
    suma = 0

    # The best solution is finding the quadratic recurence. Since I can't find
    # it on my own, I have painstakingly split the whole farm into 14 types of
    # squares (each square represents visited places in one map):
    #
    # ^ - UP pentagon
    # V - DOWN pentagon
    # < - LEFT pentagon
    # > - RIGHT pentagon
    # / - RIGHT-DOWN pentagon
    # \ - LEFT-DOWN pentagon
    # ( - LEFT-UP pentagon
    # ) - RIGHT-UP pentagon
    # , - RIGHT-DOWN triangle
    # . - LEFT-DOWN triangle
    # ` - RIGHT-UP triangle
    # ' - LEFT-UP triangle
    # e - even parity square
    # o - odd parity square
    # S - starting square (the same as even parity square)
    #
    #     ,^.
    #    ,/e\.
    #   ,/eoe\.
    #  ,/eoeoe\.
    # ,/eoeoeoe\.
    # <eoeoSoeoe>
    # `(eoeoeoe)'
    #  `(eoeoe)'
    #   `(eoe)'
    #    `(e)'
    #     `V'
    #
    # Pentagons have odd parity an triangles have even parity.
    #
    # Parity can be computed by adding two coordinates together and computing
    # modulo two. (0, 0) has even parity, (1, 2) has odd parity.
    #
    # The input is constructed so that the walking stops right at the edges of
    # squares (0, 65) for the up pentagon, (130, 65) for the down pentagon, (65,
    # 0) for the left pentagon, (65, 130) for the right pentagon. It's because
    # the middle row and middle columns are garden plots. There's also garden
    # plots inside the square creating a 45-degree rotated square of garden
    # plots. Since there are no rocks, this creates a perfect sharp line of
    # visited garden plots in pentagons and triangles, not requiring to manually
    # do flood fill or search.
    #
    # Thus the problem reduces to just counting the number of each square in the
    # whole farm and then counting the garden plots with the correct parity.
    #
    # And one special thing with this approach -- there are some garden plots
    # not visitable by moving in four directions. I have manually detected these
    # using my eyes and a bucket tool in Gimp. The adjusted input file is
    # attached in the repository.

    # Compute all types of squares
    up_pentagon = 0
    for i in range(sizex // 2):
        for col in range(sizey // 2 - i, sizey // 2 + i + 1):
            if (i + col) % 2 and m[i, col] == '.':
                up_pentagon += 1
    for i in range(sizex // 2, sizex):
        for col in range(sizey):
            if (i + col) % 2 and m[i, col] == '.':
                up_pentagon += 1

    down_pentagon = 0
    for i in range(sizex // 2):
        for col in range(sizey // 2 - i, sizey // 2 + i + 1):
            if (maxx - i + col) % 2 and m[maxx - i, col] == '.':
                down_pentagon += 1
    for i in range(sizex // 2, sizex):
        for col in range(sizey):
            if (maxx - i + col) % 2 and m[maxx - i, col] == '.':
                down_pentagon += 1

    right_pentagon = 0
    for i in range(sizex // 2):
        for col in range(sizey // 2 - i, sizey // 2 + i + 1):
            if (maxx - i + col) % 2 and m[col, maxx - i] == '.':
                right_pentagon += 1
    for i in range(sizex // 2, sizex):
        for col in range(sizey):
            if (maxx - i + col) % 2 and m[col, maxx - i] == '.':
                right_pentagon += 1

    left_pentagon = 0
    for i in range(sizex // 2):
        for col in range(sizey // 2 - i, sizey // 2 + i + 1):
            if (i + col) % 2 and m[col, i] == '.':
                left_pentagon += 1
    for i in range(sizex // 2, sizex):
        for col in range(sizey):
            if (i + col) % 2 and m[col, i] == '.':
                left_pentagon += 1

    right_down_pentagon = 0
    for i in range(sizex // 2):
        for col in range(sizey // 2 - i, sizex):
            if (i + col) % 2 and m[i, col] == '.':
                right_down_pentagon += 1
    for i in range(sizex // 2, sizex):
        for col in range(sizey):
            if (i + col) % 2 and m[i, col] == '.':
                right_down_pentagon += 1

    left_down_pentagon = 0
    for i in range(sizex // 2):
        for col in range(sizey // 2 + i + 1):
            if (i + col) % 2 and m[i, col] == '.':
                left_down_pentagon += 1
    for i in range(sizex // 2, sizex):
        for col in range(sizey):
            if (i + col) % 2 and m[i, col] == '.':
                left_down_pentagon += 1

    right_up_pentagon = 0
    for i in range(sizex // 2):
        for col in range(sizey // 2 - i, sizex):
            if (maxx - i + col) % 2 and m[maxx - i, col] == '.':
                right_up_pentagon += 1
    for i in range(sizex // 2, sizex):
        for col in range(sizey):
            if (maxx - i + col) % 2 and m[maxx - i, col] == '.':
                right_up_pentagon += 1

    left_up_pentagon = 0
    for i in range(sizex // 2):
        for col in range(sizey // 2 + i + 1):
            if (maxx - i + col) % 2 and m[maxx - i, col] == '.':
                left_up_pentagon += 1
    for i in range(sizex // 2, sizex):
        for col in range(sizey):
            if (maxx - i + col) % 2 and m[maxx - i, col] == '.':
                left_up_pentagon += 1

    left_up_triangle = 0
    for i in range(sizex // 2):
        for col in range(sizey // 2 - i):
            # The last one should be (64, 0)
            if (i + col) % 2 == 0 and m[i, col] == '.':
                left_up_triangle += 1

    left_down_triangle = 0
    for i in range(sizex // 2):
        for col in range(sizey // 2 - i):
            if (maxx - i + col) % 2 == 0 and m[maxx - i, col] == '.':
                left_down_triangle += 1

    right_up_triangle = 0
    for i in range(sizex // 2):
        for col in range(sizey // 2 + 1 + i, sizey):
            # The last one should be (64, 0)
            if (i + col) % 2 == 0 and m[i, col] == '.':
                right_up_triangle += 1

    right_down_triangle = 0
    for i in range(sizex // 2):
        for col in range(sizey // 2 + 1 + i, sizey):
            if (maxx - i + col) % 2 == 0 and m[maxx - i, col] == '.':
                right_down_triangle += 1

    even_square = 0
    for i in range(sizex):
        for col in range(sizey):
            if (i + col) % 2 == 0 and m[i, col] == '.':
                even_square += 1

    odd_square = 0
    for i in range(sizex):
        for col in range(sizey):
            if (i + col) % 2 and m[i, col] == '.':
                odd_square += 1

    steps = (steps - sizex // 2) // sizex
    suma += (
        up_pentagon
        + down_pentagon
        + left_pentagon
        + right_pentagon
        + (steps - 1)
        * (
            right_down_pentagon
            + right_up_pentagon
            + left_down_pentagon
            + left_up_pentagon
            + right_down_triangle
            + right_up_triangle
            + left_down_triangle
            + left_up_triangle
        )
        + right_down_triangle
        + right_up_triangle
        + left_down_triangle
        + left_up_triangle
        + steps * (steps + 1) // 2 * even_square
        + steps * (steps - 1) // 2 * odd_square
        + steps * (steps - 1) // 2 * even_square
        + (steps - 1) * (steps - 2) // 2 * odd_square
    )
    return suma


DAY = 21
FILE = f"{DAY}mod.txt"
print(main(FILE))
