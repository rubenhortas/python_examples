import unittest

from data_structures_and_algorithms.algorithms.graphs.dijkstra.dijkstra import get_shortest_path
from data_structures_and_algorithms.data_structures.graphs.graph import Graph


class Test(unittest.TestCase):
    def test_dijkstra(self):
        # graph = Graph(6, [(0, 1, 4), (0, 2, 2), (1, 2, 5), (1, 3, 10), (2, 4, 3), (3, 5, 11), (4, 3, 4)], True)
        # self.assertEqual(([0, 2, 4, 3, 5], 20), get_shortest_path(graph, 0, 5))

        graph = Graph(9, [(0, 1, 3), (0, 3, 2), (0, 8, 4), (1, 7, 4), (2, 7, 2), (2, 3, 6), (2, 5, 1), (3, 4, 1),
                          (4, 8, 8), (5, 6, 8)])

        # self.assertEqual(([0, 1, 7], 7), get_shortest_path(graph, 0, 7))
        self.assertEqual(([2, 3, 4, 8], 15), get_shortest_path(graph, 2, 8))  # TODO: Check this result
