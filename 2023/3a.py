from aoc import *


def search(inp, ii, jj, searched):
    numbers = []
    for iii in (-1, 0, 1):
        for jjj in (-1, 0, 1):
            if (ii + iii, jj + jjj) in searched:
                continue
            if not iii and not jjj:
                continue
            if ii + iii < 0:
                continue
            if jj + jjj < 0:
                continue
            if ii + iii >= len(inp):
                continue
            if jj + jjj >= len(inp[0]):
                continue
            x = ii + iii
            y = jj + jjj
            if inp[x][y] not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                continue
            xx = x
            yy = y
            while yy >= 0 and inp[xx][yy] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                yy -= 1
            starty = yy + 1
            yy = y
            while yy < len(inp[0]) and inp[xx][yy] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                yy += 1
            endy = yy - 1
            num = ''
            for yyy in range(starty, endy + 1):
                num += inp[xx][yyy]
                searched.add((xx, yyy))
            # print(f'number is {num}, {starty}, {endy}')
            numbers.append(int(num))
    return numbers


def main(input_file: str):
    inp = load_map_ll(input_file)
    searched = set()
    numbers = []
    for ii, i in enumerate(inp):
        for jj, j, in enumerate(i):
            if j != '.' and j not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                numbers.extend(search(inp, ii, jj, searched))
    return sum(numbers)


DAY = 3
FILE_TEST = f"{DAY}_test.txt"
FILE_EXP = f"{DAY}_expa.txt"
FILE = f"{DAY}.txt"
# test_and_submit(main, FILE_TEST, FILE_EXP, FILE)
print(main(FILE_TEST))
print(main(FILE))
