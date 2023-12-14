from aoc import *


def main(input_file: str):
    inp = load_map_ll(input_file)
    # print(inp)
    for i, row in enumerate(inp):
        for j, col in enumerate(row):
            if col == 'O':
                for k in range(i - 1, -1, -1):
                    if inp[k][j] in ['O', '#']:
                        if k != i - 1:
                            inp[k + 1][j] = 'O'
                            inp[i][j] = '.'
                        break
                    elif k == 0:
                        inp[k][j] = 'O'
                        inp[i][j] = '.'
    suma = 0
    for i, row in enumerate(inp):
        for j, col in enumerate(row):
            if col == 'O':
                suma += len(inp) - i
    return suma


DAY = 14
FILE_TEST = f"{DAY}_test.txt"
FILE_EXP = f"{DAY}_expa.txt"
FILE = f"{DAY}.txt"
# test_and_submit(main, FILE_TEST, FILE_EXP, FILE)
print(main(FILE_TEST))
print(main(FILE))
