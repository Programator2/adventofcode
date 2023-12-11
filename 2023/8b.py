from aoc import *
import math


def main(input_file: str):
    m = {}
    inp = filerstrip(input_file)
    inst, inp = inp.split('\n\n')
    for i in inp.split('\n'):
        start, els = i.split(' = ')
        els = els[1:-1]
        first, sec = els.split(', ')
        m[start] = (first, sec)
    start = list(filter(lambda x: x[2] == 'A', m))
    cycles = []
    for s in start:
        i = 0
        while True:
            ins = inst[i % len(inst)]
            if ins == 'L':
                s = m[s][0]
            else:
                s = m[s][1]
            i += 1
            if s[2] == 'Z':
                cycles.append(i)
                break
    return math.lcm(*cycles)


DAY = 8
FILE_TEST = f"{DAY}_testb.txt"
FILE_EXP = f"{DAY}_expb.txt"
FILE = f"{DAY}.txt"
# test_and_submit(main, FILE_TEST, FILE_EXP, FILE)
print(main(FILE_TEST))
print(main(FILE))
