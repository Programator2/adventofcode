from typing import Callable
from aocd import submit
from collections import defaultdict
from collections.abc import Sequence
from functools import reduce


def lines(path):
    """Return a list of lines from the file `path`.

    Includes newlines.
    """
    with open(path) as f:
        return f.readlines()


def lines_stripped(path):
    """Return a list of lines from the file `path`.

    Doesn't include newlines.
    """
    with open(path) as f:
        return [l.rstrip('\n') for l in f]


def file(path: str) -> str:
    """Return contents of a file at `path` as a string
    """
    with open(path) as f:
        return f.read()


def filerstrip(path: str) -> str:
    """Return rstripped file contents of file at `path`
    """
    return file(path).rstrip()


def load_map(path: str):
    """Return list of strings ("2D array") from the file at `path`
    """
    with open(path) as f:
        lines = f.readlines()
    return list(map(lambda x: x.rstrip(), lines))


def load_map_dd(path: str, factory=lambda: 0, init=lambda x: x) -> defaultdict:
    """Return `defaultdict` with tuple (x, y) coordinates for each element of
    the map.
    """
    inp = load_map(path)
    d = defaultdict(factory)
    for r, row in enumerate(inp):
        for ei, e in enumerate(row):
            d[(r, ei)] = init(e)
    return d


def load_map_ll(path: str):
    """Return list of lists of one char strings ("2D array") from the file at
    `path`
    """
    with open(path) as f:
        lines = f.readlines()
    return list(map(lambda x: list(x.rstrip()), lines))


def load_ints(path):
    """
    Return a list of ints loaded from file at `path`
    """
    with open(path) as f:
        lines = f.readlines()
    return list(map(lambda x: int(x.rstrip()), lines))


def load_ints_split(path, splitchar):
    """
    Return a list of ints loaded from file at `path` delimited by splitchar.
    """
    line = file(path)
    return [int(i) for i in line.split(splitchar)]


def full_range(start: int, stop: int):
    """
    Similar to `range`, but `stop` is included
    """
    s = start
    while True:
        yield s
        if stop < start:
            s -= 1
        else:
            s += 1
        if s == stop:
            yield s
            return


def pmat(ll):
    """Print a matrix."""
    for row in ll:
        for c in row:
            print(c, end='')
        print()


# Implementation of Chinese Remainder Theorem from
# https://rosettacode.org/wiki/Chinese_remainder_theorem#Python_3.6

def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1:
        return 1
    while a > 1:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += b0
    return x1


def crt(n: Sequence[int], a: Sequence[int]):
    """Chinese remainder theorem.
    :param n: List of moduli.
    :param a: List of numbers for which the modulo should be calculated.
    :returns: Solve a system of linear congruence relations in the form of
    c_i x = n_i (mod a_i).
    """
    sum = 0
    prod = reduce(lambda a, b: a * b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod


def test_and_submit(f: Callable, test_inp: str, expected: str, inp: str, day: int=16):
    test_res = f(test_inp)
    if test_res is None:
        print('Function returned None. Exiting.')
        return
    exp_res = filerstrip(expected)
    if str(test_res) != exp_res:
        print(f'Testing answer incorrect: {test_res}, expected {exp_res}')
        return
    print('Testing data correct, computing on real data now')
    res = f(inp)
    print(f'submitting: {res}')
    submit(res, day=day, year=2024)
