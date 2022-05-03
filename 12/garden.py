class Garden:

    def __init__(self, file) -> None:
        self.orchard = self.read_input(file)
        self.orchard_dim = len(self.orchard)
        self.start = (self.orchard_dim-1, 0)
        self.matrix_of_optimal_values = [[None]*self.orchard_dim for _ in range(self.orchard_dim)]

    def read_input(self, file):
        orchard = []
        with open(file) as f:
            for line in f:
                line = line.strip().split()
                row = []
                for i in line:
                    row += [int(i)]
                orchard += [row]
        return orchard

    def find_optimal_route(self):
        # TODO
        pass

garden = Garden('orchard.txt')

print(garden.orchard)