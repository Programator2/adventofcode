from more_itertools import chunked
from itertools import cycle


def main(a, b):
    scorea = 0
    scoreb = 0
    roll = 0
    i = chunked(cycle(range(1, 101)), 3)
    while True:
        points = sum(next(i))
        a = (a+points) % 10
        a = 10 if a == 0 else a
        roll += 3
        scorea += a
        if scorea >= 1000:
            return scoreb * roll
        h = next(i)
        points = sum(h)
        b = (b+points) % 10
        b = 10 if b == 0 else b
        roll += 3
        scoreb += b
        if scoreb >= 1000:
            return scorea * roll


# print(main(4, 8))
print(main(9, 3))
