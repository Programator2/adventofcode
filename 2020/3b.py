from aocd import submit
import re


FILE = '3_test.txt'
FILE = '3.txt'


slopes = [
    (1, 1),
    (3, 1),
    (5, 1),
    (7, 1),
    (1, 2),
]


def main():
    with open(FILE) as f:
        lines = f.readlines()
        lines = list(map(lambda x: x.rstrip(), lines))
    multiplied = 1
    for incx, incy in slopes:
        posx = incx
        i = incy
        trees = 0
        nothing = 0
        while i < len(lines):
            print('posx', posx)
            print('i', i)
            if lines[i][posx % len(lines[i])] == '#':
                trees += 1
                print('tree')
            else:
                nothing += 1
            posx += incx
            i += incy
        multiplied *= trees
        print('trees', trees)
    print(multiplied, nothing)
    input()
    print('done')
    submit(multiplied)


main()
