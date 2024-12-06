from aoc import *


U = 1
R = 2
D = 3
L = 4
newoff = {U: (-1, 0), R: (0, 1), D: (1, 0), L: (0, -1)}
newdir = {U: R, R: D, D: L, L: U}


def end(i, j, dir, maxi, maxj):
    return (
        (dir == U and i == 0)
        or (dir == D and i == maxi - 1)
        or (dir == L and j == 0)
        or (dir == R and j == maxj - 1)
    )


def main(infi: str):
    inp = load_map_dd(infi)
    maxi = max(i for i, _ in inp) + 1
    maxj = max(j for _, j in inp) + 1
    pos = None
    for i in range(maxi):
        for j in range(maxj):
            if inp[i,j] == '^':
                inp[i,j] = '.'
                pos = (i,j)
                break
        if pos:
            break
    dir = U
    coords = {pos}
    while not end(*pos, dir, maxi, maxj):
        off = newoff[dir]
        new_pos = pos[0] + off[0], pos[1] + off[1]
        if inp[new_pos] == '#':
            dir = newdir[dir]
            pos = pos[0] + newoff[dir][0], pos[1] + newoff[dir][1]
        else:
            pos = new_pos
        coords.add(pos)
    return len(coords)


DAY = 6
FILE_TEST = f"{DAY}_testa.txt"
# FILE_TEST = f"{DAY}_testb.txt"
FILE_EXP = f"{DAY}_exp.txt"
FILE = f"{DAY}.txt"
# test_and_submit(main, FILE_TEST, FILE_EXP, FILE, DAY)
# print(main(FILE_TEST))
print(main(FILE))
