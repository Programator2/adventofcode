from aoc import *


errors = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
}

mir = {
    ']':'[',
    '}': '{',
    '>':'<',
    ')':'('}

def main(input_file: str):
    inp = load_map(input_file)
    er = 0
    for l in inp:
        stack = []
        for c in l:
            if c in '[({<':
                stack.append(c)
                continue
            if stack[-1] != mir[c]:
                er += errors[c]
                break
            del stack[-1]
    return er

DAY = 10
FILE_TEST = f"{DAY}_test.txt"
FILE_EXP = f"{DAY}_exp.txt"
FILE = f"{DAY}.txt"
# test_and_submit(main, FILE_TEST, FILE_EXP, FILE)
print(main(FILE))
