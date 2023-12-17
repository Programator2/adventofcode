from aoc import *
from heapq import *
import itertools
from collections import defaultdict, deque, UserList


D = {'R': (0, 1), 'L': (0, -1), 'D': (1, 0), 'U': (-1, 0)}
POSSIBLE_MOVEMENTS = {'R': ('R', 'U', 'D'),
                      'L': ('L', 'D', 'U'),
                      'U': ('U', 'R', 'L'),
                      'D': ('D', 'R', 'L')}
TR = {'R': '>', 'L': '<', 'U': '^', 'D': 'v'}


# Priority queue implementation from
# https://docs.python.org/3.3/library/heapq.html#priority-queue-implementation-notes
class PriorityQueue(UserList):
    def __init__(self):
        self.entry_finder = {}               # mapping of tasks to entries
        self.REMOVED = '<removed-task>'      # placeholder for a removed task
        self.counter = itertools.count()     # unique sequence count
        UserList.__init__(self)

    def add_task(self, task, priority=0):
        'Add a new task or update the priority of an existing task'
        if task in self.entry_finder:
            self.remove_task(task)
        count = next(self.counter)
        entry = [priority, count, task]
        self.entry_finder[task] = entry
        heappush(self.data, entry)

    def remove_task(self, task):
        'Mark an existing task as REMOVED.  Raise KeyError if not found.'
        entry = self.entry_finder.pop(task)
        entry[-1] = self.REMOVED

    def pop_task(self):
        'Remove and return the lowest priority task. Raise KeyError if empty.'
        while self.data:
            priority, count, task = heappop(self.data)
            if task is not self.REMOVED:
                del self.entry_finder[task]
                return task
        raise KeyError('pop from an empty priority queue')


def main(input_file: str):
    inp = load_map_dd(input_file)
    max_x = max(x for x, _ in inp.keys())
    max_y = max(y for _, y in inp.keys())

    neighbours = defaultdict(set)

    # Create all nodes
    nodes = [(x, y, d, l) for x in range(max_x + 1) for y in range(max_y + 1)
                for d in D for l in range(1, 4)]
    nodes.append((0, 0, 'R', 0))
    nodes.append((0, 0, 'L', 0))

    for x, y, d, l in nodes:
        for move in POSSIBLE_MOVEMENTS[d]:
            dx, dy = D[move]
            new_pos = (x + dx, y + dy)
            if new_pos in inp and (l < 3 or d != move):
                neighbour = (new_pos[0], new_pos[1], move,
                             (l + 1) if d == move else 1)
                neighbours[(x, y, d, l)].add(neighbour)

    def dijkstra(source: tuple[int, int], dest: tuple[int, int]):
        inf = float('inf')

        dist = {node: inf for node in nodes}
        previous = {node: None for node in nodes}
        dist[source] = 0
        q = PriorityQueue()
        [q.add_task(v, dist[v]) for v in nodes]

        print('OK')

        while q:
            # pp(q)
            u = q.pop_task()
            if dist[u] == inf or u == dest:
                break
            for v in neighbours[u]:
                cost = inp[(v[0], v[1])]
                alt = dist[u] + cost
                if alt < dist[v]:                                  # Relax (u,v,a)
                    dist[v] = alt
                    previous[v] = u
                    q.add_task(v, alt)
        #pp(previous)
        # s, u = deque(), dest
        # while previous[u]:
            # s.appendleft(u)
            # u = previous[u]
        # s.appendleft(u)
        return dist[dest] # heat loss
        return s # trajectory

    return(min(dijkstra((0, 0, 'R', 0), (max_x, max_y, d, l)) for d in D for l in range(1, 4)))
    # best_trajectory = {(x, y): v for x, y, v in best_trajectory}
    # for x in range(max_x + 1):
        # for y in range(max_y + 1):
            # if (x, y) in best_trajectory:
                # print(best_trajectory[(x, y)], end='')
            # else:
                # print(inp[(x, y)], end='')
        # print()
    return total_loss[(max_x, max_y)]


DAY = 17
FILE_TEST = f"{DAY}_test.txt"
FILE_EXP = f"{DAY}_exp.txt"
FILE = f"{DAY}.txt"
# test_and_submit(main, FILE_TEST, FILE_EXP, FILE, DAY)
print(main(FILE_TEST))
print(main(FILE))
