from aoc import *
from collections import namedtuple, deque


def main(input_file: str):
    inp = load_map_ll(input_file)
    edges = []
    d = {}
    for ri, r in enumerate(inp):
        for ei, e in enumerate(r):
            d[(ei, ri)] = int(e)
    for (ei, ri), e in d.items():
        if (ei, ri+1) in d:
            edges.append(((ei, ri), (ei, ri + 1), d[(ei, ri+1)]))
        if (ei + 1, ri) in d:
            edges.append(((ei, ri), (ei + 1, ri), d[(ei + 1, ri)]))
    g = Graph(edges)
    path = g.dijkstra((0, 0), (len(inp[0]) - 1, len(inp) - 1))
    out = sum(d[e] for e in path)
    return out - d[(0, 0)]


# Dijkstra from https://rosettacode.org/wiki/Dijkstra%27s_algorithm#Python
inf = float('inf')
Edge = namedtuple('Edge', ['start', 'end', 'cost'])

class Graph():
    def __init__(self, edges):
        self.edges = [Edge(*edge) for edge in edges]
        self.vertices = {e.start for e in self.edges} | {e.end for e in self.edges}

    def dijkstra(self, source, dest):
        assert source in self.vertices
        dist = {vertex: inf for vertex in self.vertices}
        previous = {vertex: None for vertex in self.vertices}
        dist[source] = 0
        q = self.vertices.copy()
        neighbours = {vertex: set() for vertex in self.vertices}
        for start, end, cost in self.edges:
            neighbours[start].add((end, cost))
            # neighbours[end].add((start, cost))

        while q:
            u = min(q, key=lambda vertex: dist[vertex])
            q.remove(u)
            if dist[u] == inf or u == dest:
                break
            for v, cost in neighbours[u]:
                alt = dist[u] + cost
                if alt < dist[v]:                                  # Relax (u,v,a)
                    dist[v] = alt
                    previous[v] = u
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
