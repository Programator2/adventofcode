from aoc import *
from statistics import median


errors = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
}

score_ = {
    '(': 1,
    '[': 2,
    '{': 3,
    '<': 4,
}


mir = {
    ']':'[',
    '}': '{',
    '>':'<',
    ')':'('}

def main(input_file: str):
    inp = load_map(input_file)
    er = 0
    correct = []
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
        else:
            correct.append(stack)

    scores = []
    for stack in correct:
        score = 0
        for c in reversed(stack):
            score = score*5+score_[c]
        scores.append(score)

    return median(scores)


DAY = 10
FILE_TEST = f"{DAY}_test.txt"
FILE_EXP = f"{DAY}_exp.txt"
FILE = f"{DAY}.txt"
# test_and_submit(main, FILE_TEST, FILE_EXP, FILE)
print(main(FILE))
