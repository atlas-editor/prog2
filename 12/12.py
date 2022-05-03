from collections import defaultdict


class Graph:

    def __init__(self, directed=False):
        self._graph = defaultdict(set)
        self._directed = directed

    def add_edge(self, node1, node2, weight=None):
        self._graph[node1].add((node2, weight))
        if not self._directed:
            self._graph[node2].add((node1, weight))

    def add_edges(self, edges):
        for e in edges:
            self.add_edge(e[0], e[1], e[2])

    def get_vertices(self):
        return self._graph.keys()

    def get_edges(self):
        edges = set()
        for u in self._graph.keys():
            for j in self._graph[u]:
                v, w = j
                edges.add((u, v, w))
        return edges


class DFU:

    def __init__(self, graph):
        self.graph = graph
        self.factors = {u: i for i, u in enumerate(self.graph._graph.keys())}

    def find(self, u):
        return self.factors[u]

    def union(self, u, v):
        v_factor = self.factors[v]
        for k in self.factors.keys():
            if self.factors[k] == v_factor:
                self.factors[k] = self.factors[u]

    def kruskal_mst(self):
        result = []
        sorted_edges = sorted(self.graph.get_edges(), key=lambda x: x[2])
        for e in sorted_edges:
            u, v, w = e
            if self.find(u) != self.find(v):
                self.union(u, v)
                result.append((u, v, w))
                if len(result) == len(self.graph.get_vertices()) - 1:
                    return result


edges = [('A', 'B', 100), ('A', 'C', 100), ('A', 'D', 1), ('C', 'B', 100),
         ('C', 'D', 1), ('D', 'B', 1), ('D', 'E', 1), ('B', 'E', 100)]

g = Graph()
g.add_edges(edges)

dfu = DFU(g)

print(dfu.kruskal_mst())
