from aoc import *
import re


CUBES = {
    'red': 12,
    'green': 13,
    'blue': 14
}


def main(input_file: str):
    inp = lines(input_file)
    suma = 0
    for i in inp:
        possible = True
        m = re.match(r'^Game (\d+): (.+)$', i)
        num = int(m[1])
        sets = m[2].split('; ')
        for s in sets:
            cubes = s.split(', ')
            for c in cubes:
                m = re.match(r'^(\d+) (red|green|blue)$', c)
                if int(m[1]) > CUBES[m[2]]:
                    possible = False
                    break
            if not possible:
                break
        if possible:
            suma += num
    return suma


DAY = 2
FILE_TEST = f"{DAY}_test.txt"
FILE_EXP = f"{DAY}_expa.txt"
FILE = f"{DAY}.txt"
# test_and_submit(main, FILE_TEST, FILE_EXP, FILE)
print(main(FILE_TEST))
print(main(FILE))
