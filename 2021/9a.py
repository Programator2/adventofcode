from aoc import *


def main(input_file: str):
    inp = load_map_ll(input_file)
    out = 0
    m = []
    for i, row in enumerate(inp):
        for j, e in enumerate(row):
            a = []
            if i != 0:
                a.append(int(inp[i-1][j]))
            if i != len(inp) -1:
                a.append(int(inp[i+1][j]))
            if j != len(row) -1:
                a.append(int(inp[i][j+1]))
            if j != 0:
                a.append(int(inp[i][j-1]))
            if min(a) > int(e):
                out +=1+int(e)
    return out

DAY = 9
FILE_TEST = f"{DAY}_test.txt"
FILE_EXP = f"{DAY}_exp.txt"
FILE = f"{DAY}.txt"
# test_and_submit(main, FILE_TEST, FILE_EXP, FILE)
print(main(FILE))
