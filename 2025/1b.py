from aoc import *


def main(infi: str):
    inp = lines_stripped(infi)
    start = 50
    zeros = 0
    for a in inp:
        way = a[0]
        num = int(a[1:])
        if way == 'L':
            # turning the knob to the left
            if (start != 0 and (start - num) <= 0):
                # we have just traversed at least one zero, any other zero will
                # show up as multiples of 100 (+ 1 is the first zero)
                zeros += abs(start - num) // 100 + 1
            elif (start - num) <= -100:
                # we have started from zero, so any other zero will show up as
                # multiples of 100
                zeros += abs(start - num) // 100
            start = (start - num) % 100
        else:
            # turning the knob to the right
            if (start + num) >= 100:
                zeros += (start + num) // 100
            start = (start + num) % 100
    return zeros


DAY = 1
FILE_TEST = f"{DAY}_testa.txt"
# FILE_TEST = f"{DAY}_testb.txt"
FILE_EXP = f"{DAY}_exp.txt"
FILE = f"{DAY}.txt"
# test_and_submit(main, FILE_TEST, FILE_EXP, FILE, DAY)
# print(main(FILE_TEST))
print(main(FILE))
