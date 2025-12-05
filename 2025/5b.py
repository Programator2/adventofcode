from aoc import *


def main(infi: str):
    inp = filerstrip(infi)
    ranges, _ = inp.split('\n\n')
    ranges = ranges.split('\n')
    rang = []
    for r in ranges:
        a, b = r.split('-')
        rang.append((int(a), int(b)))
    rang.sort(key=lambda x: x[0])
    s = 0
    cur_low = rang[0][0]
    cur_high = rang[0][1]
    for i, (low, high) in enumerate(rang[1:], 1):
        if low <= cur_high:
            cur_high = max(high, cur_high)
        else:
            s += cur_high - cur_low + 1
            cur_low = low
            cur_high = high
    s += cur_high - cur_low + 1
    return s


DAY = 5
FILE_TEST = f"{DAY}_testa.txt"
# FILE_TEST = f"{DAY}_testb.txt"
FILE_EXP = f"{DAY}_exp.txt"
FILE = f"{DAY}.txt"
# test_and_submit(main, FILE_TEST, FILE_EXP, FILE, DAY)
# print(main(FILE_TEST))
print(main(FILE))
