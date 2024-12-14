from aoc import *


# This one required manual inspection of the output. If we take a look at first
# 100 states, states 38 and 98 stand out because they contain prominent vertical
# and horizontal incomplete lines containing many robots (see 14_38.txt and
# 14_98.txt). If we continue watching later states, we can see that similar
# patterns emerge every 101 and 103 states, respectively.
#
# Let's find a state, where they occur at the same time. We'll be solving CRT as
print(crt([101, 103], [38, 98]))
# The output is 7411. If we check this state, the Chrsitmas tree is there. The
# answer os *7412*, since indexing starts at zero.


def main(infi: str):
    inp = lines_stripped(infi)
    width = 101
    height = 103
    # width = 11
    # height = 7
    m = [[' '] * 101 for _ in range(height)]
    robots = []
    for l in inp:
        match = re.fullmatch(r'^p=(.*),(.*) v=(.*),(.*)$', l)
        robot = tuple(map(int, match.groups()))
        robots.append([(robot[0], robot[1]), (robot[2], robot[3])])
    for r in robots:
        newpos = (
            (r[0][0] + 7412 * r[1][0]) % width,
            (r[0][1] + 7412 * r[1][1]) % height,
        )
        r[0] = newpos
        m[r[0][1]][r[0][0]] = 'x'
    pmat(m)


DAY = 14
FILE_TEST = f"{DAY}_testa.txt"
# FILE_TEST = f"{DAY}_testb.txt"
FILE_EXP = f"{DAY}_exp.txt"
FILE = f"{DAY}.txt"
# test_and_submit(main, FILE_TEST, FILE_EXP, FILE, DAY)
# print(main(FILE_TEST))
print(main(FILE))
