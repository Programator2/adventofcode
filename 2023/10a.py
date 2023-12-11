from aoc import *


def analyse(m, start, d):
    x, y = start
    price = d[start]
    todo = []
    # up
    a, b = (start[0] - 1, start[1])
    if a >= 0 and b >= 0 and a < len(m) and b < len(m[0]):
        if m[a][b] in ['|', '7', 'F']:
            if (a, b) not in d:
                todo.append((a, b))
            d[a, b] = min(d.get((a, b), 999999999), price + 1)
            if d[a, b] != price + 1:
                todo.append((a, b))
    # right
    a, b = (start[0], start[1] + 1)
    if a >= 0 and b >= 0 and a < len(m) and b < len(m[0]):
        if m[a][b] in ['-', '7', 'J']:
            if (a, b) not in d:
                todo.append((a, b))
            d[a, b] = min(d.get((a, b), 999999999), price + 1)
            if d[a, b] != price + 1:
                todo.append((a, b))
    # down
    a, b = (start[0] + 1, start[1])
    if a >= 0 and b >= 0 and a < len(m) and b < len(m[0]):
        if m[a][b] in ['|', 'L', 'J']:
            if (a, b) not in d:
                todo.append((a, b))
            d[a, b] = min(d.get((a, b), 999999999), price + 1)
            if d[a, b] != price + 1:
                todo.append((a, b))
    # left
    a, b = (start[0], start[1] - 1)
    if a >= 0 and b >= 0 and a < len(m) and b < len(m[0]):
        if m[a][b] in ['-', 'F', 'L']:
            if (a, b) not in d:
                todo.append((a, b))
            d[a, b] = min(d.get((a, b), 999999999), price + 1)
            if d[a, b] != price + 1:
                todo.append((a, b))
    return todo


def main(input_file: str):
    inp = load_map(input_file)
    d = {}
    for ri, r in enumerate(inp):
        for ci, c in enumerate(r):
            if c == 'S':
                s_pos = (ri, ci)
                d[s_pos] = 0
                break
        if c == 'S':
            break
    todo = [s_pos]
    while todo:
        new_todo = []
        for pos in todo:
            new_todo.extend(analyse(inp, pos, d))
        todo = new_todo
    # for ri, _ in enumerate(inp):
    #     for ci, _ in enumerate(r):
    #         print(d.get((ri, ci), '.'), end='')
    #     print()
    return max(d.values())


DAY = 10
FILE_TEST = f"{DAY}_test.txt"
FILE_EXP = f"{DAY}_exp.txt"
FILE = f"{DAY}.txt"
# test_and_submit(main, FILE_TEST, FILE_EXP, FILE)
print(main(FILE_TEST))
print(main(FILE))
