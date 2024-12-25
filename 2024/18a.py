from aoc import *
from itertools import product
from collections import namedtuple, deque, UserList
from heapq import *
import itertools


# Priority queue implementation from
# https://docs.python.org/3.3/library/heapq.html#priority-queue-implementation-notes
class PriorityQueue(UserList):
    def __init__(self):
        self.entry_finder = {}  # mapping of tasks to entries
        self.REMOVED = '<removed-task>'  # placeholder for a removed task
        self.counter = itertools.count()  # unique sequence count
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


# Dijkstra from https://rosettacode.org/wiki/Dijkstra%27s_algorithm#Python
inf = float('inf')
Edge = namedtuple('Edge', ['start', 'end', 'cost'])


class Graph:
    def __init__(self, edges):
        self.edges = [Edge(*edge) for edge in edges]
        # print(dir(self.edges[0]))
        self.vertices = {e.start for e in self.edges} | {
            e.end for e in self.edges
        }

    def dijkstra(self, source, dest):
        assert source in self.vertices

        dist = {vertex: inf for vertex in self.vertices}
        dist[source] = 0
        previous = {vertex: None for vertex in self.vertices}

        q = PriorityQueue()
        [q.add_task(v, dist[v]) for v in self.vertices]

        neighbours = {vertex: set() for vertex in self.vertices}
        for start, end, cost in self.edges:
            neighbours[start].add((end, cost))

        while q:
            u = q.pop_task()
            if dist[u] == inf or u == dest:
                break
            for v, cost in neighbours[u]:
                alt = dist[u] + cost
                if alt < dist[v]:  # Relax (u,v,a)
                    dist[v] = alt
                    previous[v] = u
                    q.add_task(v, alt)
        s, u = deque(), dest
        while previous[u]:
            s.appendleft(u)
            u = previous[u]
        s.appendleft(u)
        return s, dist[dest]


DIRS = ((-1, 0), (0, 1), (1, 0), (0, -1))


def main(infi: str):
    inp = lines_stripped(infi)
    coords = set()
    for b in range(1025, len(inp)):
        for x in inp[:b]:
            nums = x.split(',')
            coords.add((int(nums[0]), int(nums[1])))
        maxi = 71
        # maxi = 7 # for test input
        maxj = maxi
        edges = []
        for i, j in product(range(maxi), range(maxj)):
            for d in DIRS:
                if (
                    (i, j) not in coords
                    and 0 <= i + d[0] < maxi
                    and 0 <= j + d[1] < maxj
                    and (i + d[0], j + d[1]) not in coords
                ):
                    edges.append(((i, j), (i + d[0], j + d[1]), 1))
                    edges.append(((i + d[0], j + d[1]), (i, j), 1))
        g = Graph(edges)
        path, shortest_length = g.dijkstra((0, 0), (maxi - 1, maxj - 1))
        return shortest_length


DAY = 18
FILE_TEST = f"{DAY}_testa.txt"
# FILE_TEST = f"{DAY}_testb.txt"
FILE_EXP = f"{DAY}_exp.txt"
FILE = f"{DAY}.txt"
# test_and_submit(main, FILE_TEST, FILE_EXP, FILE, DAY)
# print(main(FILE_TEST))
print(main(FILE))
