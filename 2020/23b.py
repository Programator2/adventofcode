from aocd import submit
from aoc import *


class Node:
    def __init__(self, data):
        self.n = data
        self.next = None
        self.prev = None

    def __str__(self):
        return str(self.n)


class Cups:
    def __init__(self):
        cups = [3,6,8,1,9,5,7,4,2]
        cups.extend(range(10, 1_000_001))

        self.cups = {}
        last = None
        for i, c in enumerate(cups):
            n = Node(c)
            self.cups[c] = n
            n.prev = last
            if last is not None:
                last.next = n
            last = n

        self.cups[cups[0]].prev = last
        last.next = self.cups[cups[0]]

    def remove_three(self, start_node):
        # These nodes will stay
        left = start_node.prev
        last = start_node.next.next
        right = last.next

        left.next = right
        start_node.prev = None

        right.prev = left
        last.next = None
        return start_node

    def insert_three(self, start_node, where):
        left = where
        right = where.next

        left.next = start_node
        start_node.prev = left

        last = start_node.next.next
        last.next = right
        right.prev = last

    def __getitem__(self, i):
        return self.cups[i]


def main():
    c = Cups()
    current_cup = c[3]
    for i in range(10_000_000):
        destination = current_cup.n - 1
        if destination < 1:
            destination = max(c.cups)
        three = c.remove_three(current_cup.next)
        three_numbers = set((three.n, three.next.n, three.next.next.n))
        three_numbers.add(current_cup.n)  # No longer three. Whatever...
        while destination in three_numbers:
            destination -= 1
            if destination < 1:
                destination = max(c.cups)
        c.insert_three(three, c[destination])
        current_cup = current_cup.next
        if i % 1_000_000 == 0:
            print(i)
    print(c[1].next)
    print(c[1].next.next)

    # Best run on pypy.
    # Multiplication is left for the reader.


main()
