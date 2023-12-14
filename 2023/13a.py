from aoc import *


def main(input_file: str):
    inp = filerstrip(input_file).split('\n\n')
    suma = 0
    for iii, i in enumerate(inp):
        m = i.split('\n')
        #rows
        for ri in range(len(m)-1):
            original = ri
            opposite = ri + 1
            while ri >= 0 and opposite < len(m):
                if m[ri] != m[opposite]:
                    break
                ri -= 1
                opposite += 1
            else:
                suma += 100 * (original + 1)
                break
        #cols
        i_trans = ['' for _ in m[0]]
        for r in m:
            for ii, c in enumerate(r):
                i_trans[ii] += c
        for ri in range(len(i_trans)-1):
            original = ri
            opposite = ri + 1
            while ri >= 0 and opposite < len(i_trans):
                if i_trans[ri] != i_trans[opposite]:
                    break
                ri -= 1
                opposite += 1
            else:
                suma += original + 1
                break
    return suma


DAY = 13
FILE_TEST = f"{DAY}_test.txt"
FILE_EXP = f"{DAY}_exp.txt"
FILE = f"{DAY}.txt"
# test_and_submit(main, FILE_TEST, FILE_EXP, FILE)
print(main(FILE_TEST))
print(main(FILE))
