class GameOfLife(object):
    def evolve(self, cells):
        next_gen = set()
        for cell in cells:
            if self.__should_survive(cell, cells):
                next_gen.add(cell)
            for neighbor in self.__get_neighbors(cell):
                if self.__should_become_alive(neighbor, cells):
                        next_gen.add(neighbor)
        print next_gen
        return next_gen

    def __should_survive(self, cell, cells):
        num_of_neighbors = self.__count_living_neighbors(cell, cells)
        return num_of_neighbors == 2 or num_of_neighbors == 3

    def __should_become_alive(self, cell, cells):
        three_neighbors = self.__count_living_neighbors(cell, cells)
        return (cell not in cells and three_neighbors == 3)

    def __count_living_neighbors(self, cell, cells):
        num_of_neighbors = 0
        for neighbor in self.__get_neighbors(cell):
            if neighbor in cells:
                num_of_neighbors += 1
        return num_of_neighbors

    def __get_neighbors(self, cell):
        neighbors = []
        (x, y) = cell
        for (dx, dy) in self.__get_neighbor_offset():
            neighbors.append((x + dx, y + dy))
        return neighbors

    def __get_neighbor_offset(self):
        return [(-1, -1), (0, -1), (1, -1),
                (-1,  0),          (1, 0),
                (-1,  1), (0,  1), (1, 1)]
