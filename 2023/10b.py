from aoc import *


def search_loop(start, m, direction):
    pos = start
    trajectory = []
    if direction == 'UP':
        a, b = pos[0] - 1, pos[1]
    elif direction == 'RIGHT':
        a, b = pos[0], pos[1] + 1
    elif direction == 'DOWN':
        a, b = pos[0] + 1, pos[1]
    elif direction == 'LEFT':
        a, b = pos[0], pos[1] - 1
    if a >= 0 and b >= 0 and a < len(m) and b < len(m[0]):
        pos = a, b
        trajectory.append(pos)
        while pos != start:
            if direction == 'UP':
                if m[pos[0]][pos[1]] == '|':
                    pos = pos[0] - 1, pos[1]
                elif m[pos[0]][pos[1]] == '7':
                    pos = pos[0], pos[1] - 1
                    direction = 'LEFT'
                elif m[pos[0]][pos[1]] == 'F':
                    pos = pos[0], pos[1] + 1
                    direction = 'RIGHT'
                else:
                    return
            elif direction == 'RIGHT':
                if m[pos[0]][pos[1]] == '-':
                    pos = pos[0], pos[1] + 1
                elif m[pos[0]][pos[1]] == '7':
                    pos = pos[0] + 1, pos[1]
                    direction = 'DOWN'
                elif m[pos[0]][pos[1]] == 'J':
                    pos = pos[0] - 1, pos[1]
                    direction = 'UP'
                else:
                    return
            elif direction == 'DOWN':
                if m[pos[0]][pos[1]] == '|':
                    pos = pos[0] + 1, pos[1]
                elif m[pos[0]][pos[1]] == 'J':
                    pos = pos[0], pos[1] - 1
                    direction = 'LEFT'
                elif m[pos[0]][pos[1]] == 'L':
                    pos = pos[0], pos[1] + 1
                    direction = 'RIGHT'
                else:
                    return
            elif direction == 'LEFT':
                if m[pos[0]][pos[1]] == '-':
                    pos = pos[0], pos[1] - 1
                elif m[pos[0]][pos[1]] == 'F':
                    pos = pos[0] + 1, pos[1]
                    direction = 'DOWN'
                elif m[pos[0]][pos[1]] == 'L':
                    pos = pos[0] - 1, pos[1]
                    direction = 'UP'
                else:
                    return
            trajectory.append(pos)
    return trajectory


def main(input_file: str):
    inp = load_map(input_file)
    for ri, r in enumerate(inp):
        for ci, c in enumerate(r):
            if c == 'S':
                s_pos = (ri, ci)
                break
        if c == 'S':
            break

    # This is not a generic solution, you have to manually check, that the loop
    # starts by going UP
    positions = set(search_loop(s_pos, inp, 'UP'))
    suma = 0
    for ri, r in enumerate(inp):
        state = 0
        for ci, c in enumerate(r):
            if (ri, ci) in positions:
                if c in ['|', 'L', 'J', 'S']:
                    state = 1 if not state else 0
            else:
                if state:
                    suma += 1
    return suma


DAY = 10
FILE_TEST = f"{DAY}_testb.txt"
FILE_EXP = f"{DAY}_expb.txt"
FILE = f"{DAY}.txt"
# test_and_submit(main, FILE_TEST, FILE_EXP, FILE)
# print(main(FILE_TEST))
print(main(FILE))
