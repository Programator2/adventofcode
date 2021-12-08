from aoc import *


def analyse(inp):
    conv = {}
    inp = inp.split()
    one = set([x for x in inp if len(x) == 2][0])
    seven = set([x for x in inp if len(x) == 3][0])
    four = set([x for x in inp if len(x) == 4][0])
    a = (seven - one).pop()

    three = [x for x in inp if len(x) == 5]
    for x in three:
        if len(set(x) - seven) == 2:
            three = set(x)
            break

    b = (four - three).pop()
    fiv = [x for x in inp if len(x) == 5]
    for x in fiv:
        x = set(x)
        if b in x:
            five = x
        else:
            if x != three:
                two = x

    c = (four - five).pop()
    d = (four - one - set((b,))).pop()
    e = (two - three).pop()
    f = (seven - set((a,)) - set((c,))).pop()
    g = (three - four - set((a,))).pop()
    conv[a] = 'a'
    conv[b] = 'b'
    conv[c] = 'c'
    conv[d] = 'd'
    conv[e] = 'e'
    conv[f] = 'f'
    conv[g] = 'g'
    return conv


def get_number(digits: frozenset):
    ret = {
        frozenset('abcefg'): 0,
        frozenset('abcdefg'): 8,
        frozenset('abcdfg'): 9,
        frozenset('abdefg'): 6,
        frozenset('cf'): 1,
        frozenset('acf'): 7,
        frozenset('bdcf'): 4,
        frozenset('acdeg'): 2,
        frozenset('abdfg'): 5,
        frozenset('acdfg'): 3,
    }
    return ret[digits]


def main(input_file: str):
    # an = analyse('acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab')
    # print(an)
    # s = 'acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab'.split()
    # for x in s:
        # x = ''.join(an[y] for y in x)
        # print(f'{x}:{get_number(frozenset(x))}')
    # return
    inp = load_map(input_file)
    out = 0
    for l in inp:
        first = l[:l.index('|')-1:]
        search = l[l.index('|')+2:]
        words = search.split()
        con = analyse(first)
        out += int(''.join(str(get_number(frozenset(''.join(str(con[y]) for y in x)))) for x in words))
    return out

DAY = 8
FILE_TEST = f"{DAY}_test.txt"
FILE_EXP = f"{DAY}_exp.txt"
FILE = f"{DAY}.txt"
# test_and_submit(main, FILE_TEST, FILE_EXP, FILE)
print(main(FILE))
