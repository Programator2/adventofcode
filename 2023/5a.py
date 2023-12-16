from aoc import *
from operator import itemgetter
import bisect


def main(input_file: str):
    inp = filerstrip(input_file)
    inp = inp.split('\n\n')
    seeds = [int(x) for x in inp[0][7:].split()]
    maps = []
    key = itemgetter(1)
    for i in range(1, 8):
        m = inp[i].split('\n')
        n = []
        for x in m[1:]:
            bisect.insort(n, tuple(int(y) for y in x.split()), key=lambda x: x[1])
        maps.append(n)
    mini = 999999999
    for s in seeds:
        for m in maps:
            aaa = bisect.bisect_left(m, s, key=key) - 1
            if aaa < 0:
                continue
            convert = m[aaa]
            if convert[1] <= s < convert[1] + convert[2]:
                s = s - convert[1] + convert[0]
        mini = min(mini, s)
    return mini


DAY = 5
FILE_TEST = f"{DAY}_test.txt"
FILE_EXP = f"{DAY}_exp.txt"
FILE = f"{DAY}.txt"
# test_and_submit(main, FILE_TEST, FILE_EXP, FILE)
print(main(FILE_TEST))
print(main(FILE))
