from aoc import *


def flood(pos, m, loop, flooded):
    if pos in loop:
        return
    todo = [pos]
    while todo:
        new_todo = []
        for pos in todo:
            a, b = pos[0] - 1, pos[1]
            if a >= 0 and b >= 0 and a < len(m) and b < len(m[0]):
                if (a, b) not in loop and (a, b) not in flooded:
                    flooded.add((a, b))
                    new_todo.append((a, b))
            a, b = pos[0], pos[1] + 1
            if a >= 0 and b >= 0 and a < len(m) and b < len(m[0]):
                if (a, b) not in loop and (a, b) not in flooded:
                    flooded.add((a, b))
                    new_todo.append((a, b))
            a, b = pos[0] + 1, pos[1]
            if a >= 0 and b >= 0 and a < len(m) and b < len(m[0]):
                if (a, b) not in loop and (a, b) not in flooded:
                    flooded.add((a, b))
                    new_todo.append((a, b))
            a, b = pos[0], pos[1] - 1
            if a >= 0 and b >= 0 and a < len(m) and b < len(m[0]):
                if (a, b) not in loop and (a, b) not in flooded:
                    flooded.add((a, b))
                    new_todo.append((a, b))
        todo = new_todo


def search_loop_with_flood(start, m, direction, loop):
    pos = start
    flooded = set()
    if direction == 'UP':
        flood((pos[0], pos[1] - 1), m, loop, flooded)
        a, b = pos[0] - 1, pos[1]
        # flood((a, b + 1), m, loop, flooded)
    elif direction == 'RIGHT':
        flood((pos[0] - 1, pos[1]), m, loop, flooded)
        a, b = pos[0], pos[1] + 1
    elif direction == 'DOWN':
        flood((pos[0], pos[1] + 1), m, loop, flooded)
        a, b = pos[0] + 1, pos[1]
    elif direction == 'LEFT':
        a, b = pos[0], pos[1] - 1
    if a >= 0 and b >= 0 and a < len(m) and b < len(m[0]):
        pos = a, b
        while pos != start:
            if direction == 'UP':
                if m[pos[0]][pos[1]] == '|':
                    flood((pos[0], pos[1] - 1), m, loop, flooded)
                    pos = pos[0] - 1, pos[1]
                elif m[pos[0]][pos[1]] == '7':
                    pos = pos[0], pos[1] - 1
                    direction = 'LEFT'
                elif m[pos[0]][pos[1]] == 'F':
                    flood((pos[0], pos[1] - 1), m, loop, flooded)
                    flood((pos[0] - 1, pos[1]), m, loop, flooded)
                    pos = pos[0], pos[1] + 1
                    direction = 'RIGHT'
                else:
                    return
            elif direction == 'RIGHT':
                if m[pos[0]][pos[1]] == '-':
                    flood((pos[0] - 1, pos[1]), m, loop, flooded)
                    pos = pos[0], pos[1] + 1
                elif m[pos[0]][pos[1]] == '7':
                    flood((pos[0] - 1, pos[1]), m, loop, flooded)
                    flood((pos[0], pos[1] + 1), m, loop, flooded)
                    pos = pos[0] + 1, pos[1]
                    direction = 'DOWN'
                elif m[pos[0]][pos[1]] == 'J':
                    pos = pos[0] - 1, pos[1]
                    direction = 'UP'
                else:
                    return
            elif direction == 'DOWN':
                if m[pos[0]][pos[1]] == '|':
                    flood((pos[0], pos[1] + 1), m, loop, flooded)
                    pos = pos[0] + 1, pos[1]
                elif m[pos[0]][pos[1]] == 'J':
                    flood((pos[0], pos[1] + 1), m, loop, flooded)
                    flood((pos[0] + 1, pos[1]), m, loop, flooded)
                    pos = pos[0], pos[1] - 1
                    direction = 'LEFT'
                elif m[pos[0]][pos[1]] == 'L':
                    pos = pos[0], pos[1] + 1
                    direction = 'RIGHT'
                else:
                    return
            elif direction == 'LEFT':
                if m[pos[0]][pos[1]] == '-':
                    flood((pos[0] + 1, pos[1]), m, loop, flooded)
                    pos = pos[0], pos[1] - 1
                elif m[pos[0]][pos[1]] == 'F':
                    pos = pos[0] + 1, pos[1]
                    direction = 'DOWN'
                elif m[pos[0]][pos[1]] == 'L':
                    flood((pos[0] + 1, pos[1]), m, loop, flooded)
                    flood((pos[0], pos[1] - 1), m, loop, flooded)
                    pos = pos[0] - 1, pos[1]
                    direction = 'UP'
                else:
                    return
    return flooded


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
    d = {}
    all_positions = set()
    dots = set()
    for ri, r in enumerate(inp):
        for ci, c in enumerate(r):
            all_positions.add((ri, ci))
            if c == 'S':
                s_pos = (ri, ci)
                d[s_pos] = 0
            if c == '.':
                dots.add((ri, ci))
    # print('UP', bool(search_loop(s_pos, inp, 'UP')))
    # print('RIGHT', bool(search_loop(s_pos, inp, 'RIGHT')))
    # print('DOWN', bool(search_loop(s_pos, inp, 'DOWN')))
    # print('LEFT', bool(search_loop(s_pos, inp, 'LEFT')))

    positions = set(search_loop(s_pos, inp, 'UP'))
    # positions = set(search_loop(s_pos, inp, 'DOWN'))
    # flooded = search_loop_with_flood(s_pos, inp, 'UP', positions)
    # pp(positions)
    # flooded = set(filter(lambda x: x[0] >= 0 and x[1] >= 0 and x[0] < len(inp) and x[1] < len(inp[0]),
                         # flooded))
    # pp(flooded)
    # print(len(all_positions - flooded - positions - (dots - flooded)))
    # print(len(all_positions - flooded - positions))
    # print(flooded & positions)
    suma = 0
    for ri, r in enumerate(inp):
        state = 0
        for ci, c in enumerate(r):
            if (ri, ci) in positions:
                if c in ['|', 'L', 'J', 'S']:
                    state = 1 if not state else 0
                # print('.', end = '')
            else:
                if state:
                    suma += 1
                    # print('X', end = '')
                # else:
                    # print('.', end = '')
            # print('X' if (ri, ci) in positions else '.', end='')
            # print(c if (ri, ci) in positions else '.', end='')
            # print(c if (ri, ci) in flooded else '.', end='')
            # print('X' if ((ri, ci) not in flooded and (ri, ci) not in positions) else '.', end='')
        # print()
    # print()
    # for ri, r in enumerate(inp):
    #     for ci, c in enumerate(r):
    #         print(c if (ri, ci) in positions else '.', end='')
    #     print()
    # print(suma)
    return suma


DAY = 10
FILE_TEST = f"{DAY}_testb.txt"
FILE_EXP = f"{DAY}_expb.txt"
FILE = f"{DAY}.txt"
# test_and_submit(main, FILE_TEST, FILE_EXP, FILE)
print(main(FILE_TEST))
print(main(FILE))
