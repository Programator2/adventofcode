from aocd import submit


FILE = '3_test.txt'
FILE = '3.txt'


def main():
    with open(FILE) as f:
        lines = f.readlines()
        lines = list(map(lambda x: x.rstrip(), lines))
    posx = 3
    trees = 0
    nothing = 0
    for i in range(1, len(lines)):
        if lines[i][posx % len(lines[i])] == '#':
            trees += 1
        else:
            nothing += 1
        posx += 3
    print(trees, nothing)
    input()
    print('done')
    submit(trees)


main()
