import unittest

from data_structures_and_algorithms.algorithms.graphs.dijkstra.dijkstra_dictionary import get_shortest_path


class Test(unittest.TestCase):
    def test_dikjstra_dictionary(self):
        graph = {
            '0': {'1': 3, '3': 2, '8': 4},
            '1': {'0': 3, '7': 4},
            '2': {'3': 6, '5': 1, '7': 2},
            '3': {'0': 2, '2': 6, '4': 1},
            '4': {'3': 1, '8': 8},
            '5': {'2': 1, '6': 8},
            '6': {'5': 8},
            '7': {'1': 4, '2': 2},
            '8': {'0': 4, '4': 8}
        }

        self.assertEqual((['2', '3', '0', '8'], 12), get_shortest_path(graph, '2', '8'))
