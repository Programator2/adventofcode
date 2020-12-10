from aoc import *



FILE = '10_test0.txt'
FILE = '10_test.txt'
FILE = '10.txt'


def main():
    inp = load_ints(FILE)
    out = 0
    cnt1 = 0
    cnt2 = 1
    inp.sort()
    print(inp)
    for i, j in enumerate(inp):
        if i == 0:
            prev = 0
        else:
            prev = inp[i-1]
        if j - prev == 1:
            cnt1 += 1
        elif j - prev == 3:
            cnt2 += 1
        else:
            print('something else')
    out = cnt1 * cnt2
    print(out)


main()
