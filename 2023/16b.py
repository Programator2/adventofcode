from aoc import *


def main(input_file: str):
    inp = load_map_dd(input_file)
    inp2 = load_map_ll(input_file)
    start = []
    for i in range(0, len(inp2)):
        start.append((i, 0, 'R'))
        start.append((i, len(inp2[0]) - 1, 'L'))
    for i in range(0, len(inp2[0])):
        start.append((0, i, 'D'))
        start.append((len(inp2) - 1, i, 'U'))
    maxx = 0
    for starting_position in start:
        light = [starting_position]
        states = defaultdict(set)
        states[(starting_position[0], starting_position[1])].add(starting_position[2])
        while light:
            new_light = []
            for x, y, direction in light:
                tile = inp[(x, y)]
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
            light = []
            for x, y, direction in new_light:
                if (x, y) not in inp:
                    continue
                if (x, y) in states:
                    if direction in states[(x, y)]:
                        continue
                states[(x, y)].add(direction)
                light.append((x, y, direction))
        maxx = max(maxx, sum(1 for i, row in enumerate(inp2) for j, c in enumerate(row) if (i, j) in states))
    return maxx


DAY = 16
FILE_TEST = f"{DAY}_test.txt"
FILE_EXP = f"{DAY}_expb.txt"
FILE = f"{DAY}.txt"
# test_and_submit(main, FILE_TEST, FILE_EXP, FILE)
print(main(FILE_TEST))
print(main(FILE))
