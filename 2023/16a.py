from aoc import *


def main(input_file: str):
    inp = load_map_dd(input_file)
    inp2 = load_map_ll(input_file)
    # pp(inp)
    light = [(0, 0, 'R')]
    states = defaultdict(set)
    states[(0, 0)].add('R')
    new = True
    while new:
        new_light = []
        for x, y, direction in light:
            if (x, y) not in inp:
                continue
            tile = inp[(x, y)]
            # print(tile, direction)
            if direction == 'R':
                if tile in ['.', '-']:
                    new_light.append((x, y + 1, 'R'))
                elif tile == '/':
                    new_light.append((x - 1, y, 'U'))
                elif tile == '\\':
                    new_light.append((x + 1, y, 'D'))
                elif tile == '|':
                    new_light.append((x - 1, y, 'U'))
                    new_light.append((x + 1, y, 'D'))
            elif direction == 'L':
                if tile in ['.', '-']:
                    new_light.append((x, y - 1, 'L'))
                elif tile == '/':
                    new_light.append((x + 1, y, 'D'))
                elif tile == '\\':
                    new_light.append((x - 1, y, 'U'))
                elif tile == '|':
                    new_light.append((x - 1, y, 'U'))
                    new_light.append((x + 1, y, 'D'))
            elif direction == 'U':
                if tile in ['.', '|']:
                    new_light.append((x - 1, y, 'U'))
                elif tile == '/':
                    new_light.append((x, y + 1, 'R'))
                elif tile == '\\':
                    new_light.append((x, y - 1, 'L'))
                elif tile == '-':
                    new_light.append((x, y + 1, 'R'))
                    new_light.append((x, y - 1, 'L'))
            elif direction == 'D':
                if tile in ['.', '|']:
                    new_light.append((x + 1, y, 'D'))
                elif tile == '/':
                    new_light.append((x, y - 1, 'L'))
                elif tile == '\\':
                    new_light.append((x, y + 1, 'R'))
                elif tile == '-':
                    new_light.append((x, y + 1, 'R'))
                    new_light.append((x, y - 1, 'L'))
        light = new_light
        num_states = sum(1 for s in states.values() for _ in s)
        for x, y, direction in light:
            states[(x, y)].add(direction)
        new_num_states = sum(1 for s in states.values() for _ in s)
        if new_num_states == num_states:
            new = False
    # for i, row in enumerate(inp2):
    #     for j, c in enumerate(row):
    #         print('#' if (i, j) in states else '.', end='')
    #     print()
    return sum(1 for i, row in enumerate(inp2) for j, c in enumerate(row) if (i, j) in states)


DAY = 16
FILE_TEST = f"{DAY}_test.txt"
FILE_EXP = f"{DAY}_expa.txt"
FILE = f"{DAY}.txt"
# test_and_submit(main, FILE_TEST, FILE_EXP, FILE)
print(main(FILE_TEST))
print(main(FILE))
