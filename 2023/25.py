from aoc import *
from collections import defaultdict
from graphviz import Graph


def search(node, m, visited):
    if node in visited:
        return
    visited.add(node)
    for n in m[node]:
        search(n, m, visited)


def main(input_file: str):
    inp = lines(input_file)
    dot = Graph()
    m = defaultdict(set)
    for l in inp:
        left, right = l.rstrip().split(': ')
        right = right.split()
        dot.node(left)
        for r in right:
            dot.node(r)
            dot.edge(left, r)

            # These were added after inspecting the graph, see below.
            if (
                r == 'gbc'
                and left == 'hxr'
                or r == 'hxr'
                and left == 'gbc'
                or r == 'mvv'
                and left == 'xkz'
                or r == 'xkz'
                and left == 'mvv'
                or r == 'tmt'
                and left == 'pnz'
                or r == 'pnz'
                and left == 'tmt'
            ):
                continue
            m[r].add(left)
            m[left].add(r)

    # Store the graph as svg and identify nodes needed in Inkscape
    # dot.format = 'svg'
    # dot.render('25.dot')

    v = set()
    search('mvv', m, v)
    a = len(v)
    v = set()
    search('xkz', m, v)
    b = len(v)
    return a * b


DAY = 25
FILE = f"{DAY}.txt"
print(main(FILE))
