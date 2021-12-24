from aoc import *
from collections import defaultdict


def main(input_file: str):
    inp = load_map(input_file)
    d = []
    state = defaultdict(bool)
    for l in inp:
        ins, rest = l.split(' ')
        x, y, z = rest.split(',')
        xa, xb = x.split('..')
        xa = int(xa.split('=')[1])
        xb = int(xb)
        ya, yb = y.split('..')
        ya = int(ya.split('=')[1])
        yb = int(yb)
        za, zb = z.split('..')
        za = int(za.split('=')[1])
        zb = int(zb)
        d.append(((xa, xb), (ya, yb), (za, zb)))
        for x in range(max(xa, -50), min(xb+1, 51)):
            for y in range(max(ya, -50), min(yb+1, 51)):
                for z in range(max(za, -50), min(zb+1, 51)):
                    if ins == 'on':
                        state[x, y, z] = True
                    else:
                        state[x, y, z] = False
    out = sum(1 for v in state.values() if v)
    return out


DAY = 22
FILE_TEST = f"{DAY}_test.txt"
FILE_EXP = f"{DAY}_exp.txt"
FILE = f"{DAY}.txt"
# test_and_submit(main, FILE_TEST, FILE_EXP, FILE)
# print(main(FILE_TEST))
print(main(FILE))
