def main():
    with open('1.txt') as f:
        lines = f.readlines()
        lines = map(lambda x: int(x.rstrip()), lines)
        total = sum(lines)
        print(total)


main()
