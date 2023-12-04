from typing import Callable
from aocd import submit


def lines(path):
    """
    Return a list of lines from the file `path`
    """
    with open(path) as f:
        return f.readlines()


def file(path: str) -> str:
    """
    Return contents of a file at `path` as a string
    """
    with open(path) as f:
        return f.read()


def filerstrip(path: str) -> str:
    """
    Return rstripped file contents of file at `path`
    """
    return file(path).rstrip()


def load_map(path):
    """
    Return list of strings ("2D array") from the file at `path`
    """
    with open(path) as f:
        lines = f.readlines()
    return list(map(lambda x: x.rstrip(), lines))


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


def test_and_submit(f: Callable, test_inp: str, expected: str, inp: str):
    test_res = f(test_inp)
    if test_res is None:
        return
    exp_res = filerstrip(expected)
    if str(test_res) != exp_res:
        print(f'Incorrect: {test_res}, expected {exp_res}')
        return
    res = f(inp)
    print(f'submitting: {res}')
    submit(res, day=4, year=2023)
