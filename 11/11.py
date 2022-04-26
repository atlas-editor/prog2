from collections import defaultdict, deque


class Graph(object):
    """ Graph data structure, undirected by default. """

    def __init__(self, edges, directed=False):
        self._graph = defaultdict(set)
        self._directed = directed
        self.add_edges(edges)

    def add_edges(self, edges):
        """ Add edges (list of tuple pairs) to graph """

        for e in edges:
            node1, node2 = e
            self.add(node1, node2)

    def add(self, node1, node2):
        """ Add edge between node1 and node2 """

        self._graph[node1].add(node2)
        if not self._directed:
            self._graph[node2].add(node1)

    def remove(self, node):
        """ Remove node from the graph """

        for _, nbrs in self._graph.items():
            if node in nbrs:
                nbrs.remove(node)
        if node in self._graph:
            del self._graph[node]

    def bfs_generator(self, source):
        """ Returns a generator object of a BFS traversal """

        seen = set()
        seen.add(source)

        q = deque()
        q.append(source)

        yield source

        while q:
            current = q.popleft()
            for nbr in self._graph[current]:
                if nbr not in seen:
                    yield nbr
                    seen.add(nbr)
                    q.append(nbr)

    def is_connected(self):
        """ Is graph connected """

        v = list(self._graph.keys())[0]
        component_of_v = set(self.bfs_generator(v))

        if component_of_v == self._graph.keys():
            return True

        return False

    def is_bipartite(self):
        """ Is graph bipartite (2-colorable) """

        if self._directed:
            raise NotImplemented

        color = dict()

        for source in self._graph.keys():

            if source in color:
                continue

            color[source] = 0

            q = deque()
            q.append(source)

            while q:
                current = q.popleft()
                for nbr in self._graph[current]:
                    if nbr not in color:
                        color[nbr] = 1 - color[current]
                        q.append(nbr)
                    elif color[current] == color[nbr]:
                        return False

        return True


edges = [('A', 'B'), ('B', 'C'), ('B', 'D'),
         ('C', 'D'), ('E', 'F'), ('F', 'C')]  # connected, non-bipartite graph
g = Graph(edges)

print(g._graph)
print(f"g is connected: {g.is_connected()}")
print(f"g is bipartite: {g.is_bipartite()}")


def fib(max):
    """ Fibonacci generator function """
    
    a, b = 0, 1
    while a < max:
        yield a
        a, b = b, a+b


f = fib(20)
# print(f)
# print(type(f))
# for i in f:
#     print(i)
