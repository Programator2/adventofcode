SERIAL = 7511
# SERIAL = 57


def compute_power_level(x, y):
    id_ = x + 10
    level = id_ * y + SERIAL
    level *= id_
    level = level % 1000 // 100
    return level - 5


def sum_3x3(x, y, matrix):
    return sum(matrix[y_][x_] for x_ in range(x, x + 3) for y_ in range(y, y + 3))


def main():
    # print(compute_power_level(122,79))
    # return
    matrix = []
    for y in range(1, 301):
        matrix.append([compute_power_level(x, y) for x in range(1, 301)])
    # print(matrix)
    # return
    print(
        max(
            (
                (x, y, sum_3x3(x, y, matrix))
                for x in range(0, 298)
                for y in range(0, 298)
            ),
            key=lambda x: x[2],
        )[:2]
    )


main()
