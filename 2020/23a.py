from aoc import *
from collections import deque


def remove_three(cups, n):
    ret = deque()
    cups.rotate(-n)
    ret.append(cups.popleft())
    ret.append(cups.popleft())
    ret.append(cups.popleft())
    cups.rotate(n)
    return ret


def insert_three(cups, three, n):
    for i in range(3):
        cups.insert(n+i, three[i])


def main():
    cups = deque([3,6,8,1,9,5,7,4,2])
    # cups = deque([3,8,9,1,2,5,4,6,7])
    current = 0
    for i in range(100):
        current_cup = cups[current]
        destination = current_cup - 1
        if destination < 1:
            destination = max(cups)
        three = remove_three(cups, current+1)
        while destination not in cups or destination == current_cup:
            destination -= 1
            if destination < 1:
                destination = max(cups)
        destination_i = cups.index(destination)
        insert_three(cups, three, destination_i+1)
        current = cups.index(current_cup)
        current = (current + 1) % len(cups)
    cups.rotate(-(cups.index(1)+1))
    [print(x, end='') for x in cups]


main()
