from aoc import *
import re


def main(input_file: str):
    inp = lines(input_file)
    suma = 0
    for i in inp:
        possible = True
        m = re.match(r'^Game (\d+): (.+)$', i)
        num = int(m[1])
        sets = m[2].split('; ')
        maxx = {
            'red': 0,
            'green': 0,
            'blue': 0
        }
        for s in sets:
            cubes = s.split(', ')
            for c in cubes:
                m = re.match(r'^(\d+) (red|green|blue)$', c)
                maxx[m[2]] = max(maxx[m[2]], int(m[1]))
        suma += maxx['red'] * maxx['green'] * maxx['blue']
    return suma


DAY = 2
FILE_TEST = f"{DAY}_test.txt"
FILE_EXP = f"{DAY}_exp.txt"
FILE = f"{DAY}.txt"
# test_and_submit(main, FILE_TEST, FILE_EXP, FILE)
print(main(FILE_TEST))
print(main(FILE))
