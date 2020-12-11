import collections

PLAYERS = 400
LAST_MARBLE = 7186400  # points


class MarbleDesk(collections.UserList):
    def __getitem__(self, x):
        return self.data[x % len(self)]

    # def insert(self, i, x):
    #     " Insert before the i-th element "
    #     return self.data.insert(i % len(self), x)

    # def pop(self, i):
    #     return self.data.pop(i % len(self))


m = collections.deque([0])
current = 0
# I index players from zero, in the text they start at 1
player = 0
scoreboard = collections.defaultdict(int)

for next_marble in range(1, LAST_MARBLE + 1):
    if next_marble % 23:
        # normal run
        insert_index = (current + 2) % len(m)
        m.insert(insert_index, next_marble)
        current = insert_index
    else:
        # special case
        scoreboard[player] += next_marble
        pop_index = (current - 7) % len(m)
        scoreboard[player] += m.pop(pop_index)
        current = (pop_index) % len(m)
    player = (player + 1) % PLAYERS

print(max(scoreboard.values()))
