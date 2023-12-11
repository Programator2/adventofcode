from aoc import *


def main(input_file: str):
    m = {}
    inp = filerstrip(input_file)
    inst, inp = inp.split('\n\n')
    for i in inp.split('\n'):
        start, els = i.split(' = ')
        els = els[1:-1]
        first, sec = els.split(', ')
        m[start] = (first, sec)
    start = 'AAA'
    index = 0
    ii = 1
    while True:
        i = inst[index]
        if i == 'L':
            start = m[start][0]
        else:
            start = m[start][1]
        if start == 'ZZZ':
            return ii
        index += 1
        ii += 1
        if index >= len(inst):
            index = 0


DAY = 8
FILE_TEST = f"{DAY}_testa.txt"
FILE_EXP = f"{DAY}_expa.txt"
FILE = f"{DAY}.txt"
# test_and_submit(main, FILE_TEST, FILE_EXP, FILE)
print(main(FILE_TEST))
print(main(FILE))
