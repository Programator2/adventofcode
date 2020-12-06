def main():
    with open("1.txt") as f:
        lines = f.readlines()
        lines = map(lambda x: int(x.rstrip()), lines)
        lines = list(lines)
        for i in lines:
            for j in lines:
                for k in lines:
                    if i + j + k == 2020:
                        print(i * j * k)


main()
