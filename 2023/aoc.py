from typing import Callable
from aocd import submit
from collections import defaultdict


def lines(path):
    """Return a list of lines from the file `path`
    """
    with open(path) as f:
        return f.readlines()


def file(path: str) -> str:
    """Return contents of a file at `path` as a string
    """
    with open(path) as f:
        return f.read()


def filerstrip(path: str) -> str:
    """Return rstripped file contents of file at `path`
    """
    return file(path).rstrip()


def load_map(path):
    """Return list of strings ("2D array") from the file at `path`
    """
    with open(path) as f:
        lines = f.readlines()
    return list(map(lambda x: x.rstrip(), lines))


def load_map_dd(path: str, factory=lambda: 0) -> defaultdict:
    """Return `defaultdict` with tuple (x, y) coordinates for each element of
    the map.
    """
    inp = load_map(path)
    d = defaultdict(factory)
    for r, row in enumerate(inp):
        for ei, e in enumerate(row):
            d[(r, ei)] = e
    return d


def load_map_ll(path):
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


def full_range(start, stop):
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
    """Print a matrix"""
    for row in ll:
        for c in row:
            print(c, end='')
        print()


def test_and_submit(f: Callable, test_inp: str, expected: str, inp: str):
    test_res = f(test_inp)
    if test_res is None:
        return
    exp_res = filerstrip(expected)
    if str(test_res) != exp_res:
        print(f'Incorrect: {test_res}, expected {exp_res}')
        return
    print('Testing data correct, computing on real data now')
    res = f(inp)
    print(f'submitting: {res}')
    submit(res, day=6, year=2023)
