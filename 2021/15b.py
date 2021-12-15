from aoc import *
from collections import namedtuple, deque, UserList
from heapq import *
import itertools


def main(input_file: str):
    inp = load_map_ll(input_file)
    d = {}
    edges = []
    for ri, r in enumerate(inp):
        for ei, e in enumerate(r):
            for rii in range(5):
                for eii in range(5):
                    el = int(e) + rii + eii
                    while el > 9:
                        el -= 9
                    d[(ei + len(inp[0]) * eii, ri + len(inp) * rii)] = int(el)

    for (ei, ri), e in d.items():
        if (ei, ri+1) in d:
            edges.append(((ei, ri), (ei, ri + 1), d[(ei, ri+1)]))
            edges.append(((ei, ri + 1), (ei, ri), d[(ei, ri)]))
        if (ei + 1, ri) in d:
            edges.append(((ei, ri), (ei + 1, ri), d[(ei + 1, ri)]))
            edges.append(((ei + 1, ri), (ei, ri), d[(ei, ri)]))
    g = Graph(edges)
    path = g.dijkstra((0, 0), (len(inp[0])*5 - 1, len(inp)*5 - 1))
    out = sum(d[e] for e in path)
    return out - d[(0, 0)]


inf = float('inf')
Edge = namedtuple('Edge', ['start', 'end', 'cost'])


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


class Graph():
    def __init__(self, edges):
        self.edges = [Edge(*edge) for edge in edges]
        # print(dir(self.edges[0]))
        self.vertices = {e.start for e in self.edges} | {e.end for e in self.edges}

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
                if alt < dist[v]:                                  # Relax (u,v,a)
                    dist[v] = alt
                    previous[v] = u
                    q.add_task(v, alt)
        s, u = deque(), dest
        while previous[u]:
            s.appendleft(u)
            u = previous[u]
        s.appendleft(u)
        return s

DAY = 15
FILE_TEST = f"{DAY}_test.txt"
FILE_EXP = f"{DAY}_exp.txt"
FILE = f"{DAY}.txt"
# test_and_submit(main, FILE_TEST, FILE_EXP, FILE)
# print(main(FILE_TEST))
print(main(FILE))
