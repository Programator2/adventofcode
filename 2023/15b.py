from aoc import *
from collections import defaultdict, OrderedDict


def hash(l):
    val = 0
    for i in l:
        if i in ['\n']:
            continue
        val = ((val + ord(i)) * 17) % 256
    return val


def main(input_file: str):
    inp = filerstrip(input_file)
    inp = inp.split(',')
    full = 0
    d = defaultdict(OrderedDict)
    for l in inp:
        if l[-1] == '-':
            full = hash(l[:-1])
            if l[:-1] in d[full]:
                del d[full][l[:-1]]
        else:
            label, slot = l.split('=')
            full = hash(label)
            slot = int(slot)
            d[full][label] = slot
    full = 0
    for a, b in d.items():
        for i, (c, d) in enumerate(b.items()):
            full += (a + 1) * (i + 1) * d
    return full


DAY = 15
FILE_TEST = f"{DAY}_test.txt"
FILE_EXP = f"{DAY}_expb.txt"
FILE = f"{DAY}.txt"
# test_and_submit(main, FILE_TEST, FILE_EXP, FILE)
print(main(FILE_TEST))
print(main(FILE))
