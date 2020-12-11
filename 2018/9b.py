import collections

PLAYERS = 400
LAST_MARBLE = 7186400  # points


class Node:
    def __init__(self, num):
        self.num = num
        self.prev = None
        self.next = None

    def insert_after(self, n, new_node):
        node = self
        for i in range(n):
            node = node.next
        old_next = node.next
        node.next = new_node
        old_next.prev = new_node
        new_node.next = old_next
        new_node.prev = node

    def prev_n(self, n):
        node = self
        for i in range(n):
            node = node.prev
        return node

    def remove(self):
        self.prev.next = self.next
        self.next.prev = self.prev
        after_this = self.next
        self.next = None
        self.prev = None
        return self.num, after_this


m = Node(0)
m.prev = m
m.next = m
current = m
# I index players from zero, in the text they start at 1
player = 0
scoreboard = collections.defaultdict(int)

for next_marble in range(1, LAST_MARBLE + 1):
    if next_marble % 23:
        # normal run
        n = Node(next_marble)
        current.insert_after(1, n)
        current = n
    else:
        # special case
        scoreboard[player] += next_marble
        score, current = current.prev_n(7).remove()
        scoreboard[player] += score
    player = (player + 1) % PLAYERS

print(max(scoreboard.values()))
