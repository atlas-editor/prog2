from collections import deque


class NoPathError(Exception):
    pass


class Maze:

    def __init__(self, file, start) -> None:
        self.maze = self.read_input(file)
        self.maze_dim = len(self.maze)
        self.start = start

    def read_input(self, file):
        maze = []
        with open(file) as f:
            for line in f:
                line = line.strip()
                row = []
                for i in line:
                    row += [i]
                maze += [row]
        return maze

    def get_neighbors(self, coordinates):
        y1, x1 = coordinates
        possible_neighbors = [(y1, x1 + 1), (y1 + 1, x1),
                              (y1, x1 - 1), (y1 - 1, x1)]
        for y2, x2 in possible_neighbors:
            in_bounds = 0 <= x2 < self.maze_dim and 0 <= y2 < self.maze_dim
            if in_bounds and self.maze[y2][x2] != "X":
                yield (y2, x2)

    def _find_path(self, start, indicator):
        visited = set()
        visited.add(start)

        qq = deque()
        qq.appendleft(start)

        predecessor = {start: None}

        while qq:
            vertex = qq.pop()
            for nbr in self.get_neighbors(vertex):
                if nbr not in visited:
                    predecessor[nbr] = vertex
                    if self.maze[nbr[0]][nbr[1]] == indicator:
                        return nbr, self.path_from_predecessors(nbr, predecessor)
                    qq.appendleft(nbr)
                    visited.add(nbr)

        raise NoPathError(f'The maze contains no path from {start} to {indicator}')

    def path_from_predecessors(self, source, predecessor):
        v = source
        path = [v]
        while predecessor[v] != None:
            path.append(predecessor[v])
            v = predecessor[v]

        return path[::-1]

    def find_path(self):
        key, path_to_key = self._find_path(self.start, 'K')
        door, path_from_key_to_door = self._find_path(key, 'D')

        return self.start, key, door, path_to_key[:-1] + path_from_key_to_door

maze = Maze('maze.txt', (5,0))

for i in maze.find_path():
    print(i)

