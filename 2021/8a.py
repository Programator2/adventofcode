from aoc import *


def main(input_file: str):
    inp = load_map(input_file)
    out = 0
    for l in inp:
        search = l[l.index('|')+2:]
        words = search.split()
        print(words)
        out += sum(1 for x in words if len(x) in [2,3,4,7])
    return out


DAY = 8
FILE_TEST = f"{DAY}_test.txt"
FILE_EXP = f"{DAY}_exp.txt"
FILE = f"{DAY}.txt"
# test_and_submit(main, FILE_TEST, FILE_EXP, FILE)
print(main(FILE))
