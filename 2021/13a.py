from aoc import *


def main(input_file: str):
    inp = filerstrip(input_file)
    pos, ins = inp.split('\n\n')
    paper = {}
    for p in pos.split():
        x, y = p.split(',')
        paper[(int(x), int(y))] = '#'
    folds = []
    for p in ins.split('\n'):
        if (len(p)) < 13:
            continue
        folds.append((p[11], int(p[13:])))
    for how, much in folds:
        new_paper = {}
        for x, y in paper.keys():
            if how == 'x':
                if x > much:
                    new_paper[(much-(x-much), y)] = '#'
                else:
                    new_paper[(x, y)] = '#'
            elif how == 'y':
                if y > much:
                    new_paper[(x, much-(y-much))] = '#'
                else:
                    new_paper[(x, y)] = '#'
        paper = new_paper
        break
    out = len(paper)
    return out

DAY = 13
FILE_TEST = f"{DAY}_test.txt"
FILE_EXP = f"{DAY}_exp.txt"
FILE = f"{DAY}.txt"
# test_and_submit(main, FILE_TEST, FILE_EXP, FILE)
print(main(FILE))
