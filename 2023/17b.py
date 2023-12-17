from aoc import *
from heapq import *
import itertools
from collections import defaultdict, OrderedDict, deque, UserList


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
    inp = load_map_dd(input_file, init=int)
    max_x = max(x for x, _ in inp.keys())
    max_y = max(y for _, y in inp.keys())

    neighbours = defaultdict(set)

    # Inspiration for node form: https://www.reddit.com/r/adventofcode/comments/18k9ne5/comment/kdpwck3/?utm_source=share&utm_medium=web2x&context=3
    # Create all nodes
    nodes = [(x, y, d, l) for x in range(max_x + 1) for y in range(max_y + 1)
                for d in D for l in range(4, 11)]
    nodes.append((0, 0, 'R', 0))
    nodes.append((0, 0, 'L', 0))

    for x, y, d, l in nodes:
        for move in POSSIBLE_MOVEMENTS[d]:
            for posun in range(4, 11):
                dx, dy = D[move]
                new_pos = (x + dx * posun, y + dy * posun)
                if new_pos in inp and (l + posun < 11 or d != move):
                    neighbour = (new_pos[0], new_pos[1], move,
                                    (l + posun) if d == move else posun)
                    neighbours[(x, y, d, l)].add(neighbour)

    # Dijkstra from https://rosettacode.org/wiki/Dijkstra%27s_algorithm#Python
    # This is a modified dijkstra with one source and multiple destinations
    def dijkstra(source: tuple[int, int], dest: set[tuple[int, int]]):
        inf = float('inf')

        orig_dest = dest.copy()

        dist = {node: inf for node in nodes}
        previous = {node: None for node in nodes}
        dist[source] = 0
        q = PriorityQueue()
        [q.add_task(v, dist[v]) for v in nodes]

        while q:
            # pp(q)
            u = q.pop_task()
            if u in dest:
                dest.remove(u)
                if dest:
                    continue
                break
            for v in neighbours[u]:
                # full_range came in handy but how to do this more nicely?
                if u[0] == v[0]:
                    cost = sum(inp[(v[0], y)] for y in full_range(u[1], v[1]) if y != u[1])
                else:
                    cost = sum(inp[(x, v[1])] for x in full_range(u[0], v[0]) if x != u[0])
                alt = dist[u] + cost
                if alt < dist[v]:                                  # Relax (u,v,a)
                    dist[v] = alt
                    previous[v] = u
                    q.add_task(v, alt)
        # s, u = deque(), dest
        # while previous[u]:
            # s.appendleft(u)
            # u = previous[u]
        # s.appendleft(u)
        return min(dist[d] for d in orig_dest) # heat loss
        return s # trajectory

    return dijkstra((0, 0, 'R', 0), {(max_x, max_y, d, l) for d in D for l in range(4, 11)})
    # best_trajectory = {(x, y): v for x, y, v in best_trajectory}
    # for x in range(max_x):
    #     for y in range(max_y):
    #         if (x, y) in best_trajectory:
    #             print(best_trajectory[(x, y)], end='')
    #         else:
    #             print(inp[(x, y)], end='')
    #     print()


DAY = 17
FILE_TEST = f"{DAY}_test.txt"
FILE_EXP = f"{DAY}_expb.txt"
FILE = f"{DAY}.txt"
# test_and_submit(main, FILE_TEST, FILE_EXP, FILE, DAY)
print(main(FILE_TEST))
print(main(FILE))
