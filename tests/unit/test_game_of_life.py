from unittest import TestCase

from game_of_life import GameOfLife


class TestGameOfLife(TestCase):
    def setUp(self):
        self.game = GameOfLife()

    def test_any_live_cell_with_less_than_two_neighbors_dies(self):
        self.evolve([(0, 0)])
        self.assert_dead((0, 0))

        self.evolve([(0, 0), (0, 1)])
        self.assert_dead((0, 1))

    def test_any_live_cell_with_two_or_three_neighbors_survives(self):
        self.evolve([(1, 1), (2, 1),
                     (0, 2), (1, 2)])

        self.assert_alive((0, 2))
        self.assert_alive((1, 2))

    def test_any_live_cell_with_more_than_three_neighbors_dies(self):
        self.evolve([(0, 1), (1, 1), (2, 1),
                     (0, 2), (1, 2), (2, 2)])

        self.assert_dead((1, 1))
        self.assert_dead((1, 2))

    def test_any_dead_cell_with_three_neighbors_becomes_alive(self):
        self.evolve([(1, 1), (2, 1),
                     (0, 2)])

        self.assert_alive((1, 2))

    def evolve(self, cells):
        self.next_gen = self.game.evolve(cells)

    def assert_alive(self, cell):
        self.assertTrue(cell in self.next_gen)

    def assert_dead(self, cell):
        self.assertFalse(cell in self.next_gen)
