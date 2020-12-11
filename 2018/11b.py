SERIAL = 7511


def compute_power_level(x, y):
    id_ = x + 10
    level = id_ * y + SERIAL
    level *= id_
    level = level % 1000 // 100
    return level - 5


def sum_any(x, y, matrix, size):
    return sum(matrix[y_][x_] for x_ in range(x, x + size) for y_ in range(y, y + size))


def main():
    matrix = []
    for y in range(1, 301):
        matrix.append([compute_power_level(x, y) for x in range(1, 301)])

    remember = {(x, y, 1): matrix[y][x] for x in range(300) for y in range(300)}

    max_entry, max_size = max(remember.items(), key=lambda x: x[1])

    for x in range(300):
        for y in range(300):
            for size in range(2, 301):
                if x + size > 300 or y + size > 300:
                    continue
                entry = (
                    remember[(x, y, size - 1)]
                    + sum(matrix[y+size-1][x_] for x_ in range(x, x + size))
                    + sum(matrix[y_][x+size-1] for y_ in range(y, y + size - 1))
                )
                remember[(x, y, size)] = entry

                if entry > max_size:
                    max_size = entry
                    max_entry = (x, y, size)
        print(f'{x}')
    print(max_entry)


main()
