from aoc import *
from more_itertools import first_true
from functools import cache


@cache
def cycle(ll):
    for direction in ('north', 'west', 'south', 'east'):
        ll = tilt(ll, direction)
    return ll


@cache
def tilt(ll, direction):
    if direction == 'west':
        inp = zip(*reversed(ll))
    elif direction == 'south':
        inp = reversed(tuple(zip(*ll)))
        inp = reversed(tuple(zip(*inp)))
    elif direction == 'east':
        inp = reversed(tuple(zip(*ll)))
    else:
        inp = ll
    inp = [list(i) for i in inp]
    for i, row in enumerate(inp):
        for j, col in enumerate(row):
            if col == 'O':
                for k in range(i - 1, -1, -1):
                    if inp[k][j] in ['O', '#']:
                        if k != i - 1:
                            inp[k + 1][j] = 'O'
                            inp[i][j] = '.'
                        break
                    elif k == 0:
                        inp[k][j] = 'O'
                        inp[i][j] = '.'
    if direction == 'west':
        inp = tuple(reversed(tuple(zip(*inp))))
    elif direction == 'south':
        inp = reversed(tuple(zip(*inp)))
        inp = tuple(reversed(tuple(zip(*inp))))
    elif direction == 'east':
        inp = tuple(zip(*reversed(inp)))
    else:
        inp = tuple(tuple(i) for i in inp)
    return inp


def main(input_file: str):
    inp = load_map_ll(input_file)
    ll = tuple(tuple(i) for i in inp)
    suma = 0
    results = {}
    # Inspiration for the cycle detection:
    # https://github.com/kwshi/advent-of-code/blob/main/python/2023/14.py
    for i in range(1, 1000000000 + 1):
        ll = cycle(ll)
        if ll in results:
            cycle_start = results[ll]
            period = i - results[ll]
            break
        results[ll] = i
    final_i = (1000000000 - cycle_start) % period + cycle_start
    inp = first_true(results.items(), pred=lambda x: x[1] == final_i)[0]
    for i, row in enumerate(inp):
        for j, col in enumerate(row):
            if col == 'O':
                suma += len(inp) - i
    return suma


DAY = 14
FILE_TEST = f"{DAY}_test.txt"
FILE_EXP = f"{DAY}_expb.txt"
FILE = f"{DAY}.txt"
# test_and_submit(main, FILE_TEST, FILE_EXP, FILE)
print(main(FILE_TEST))
print(main(FILE))
