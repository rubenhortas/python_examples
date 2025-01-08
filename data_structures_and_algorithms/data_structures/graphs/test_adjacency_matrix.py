import unittest

from data_structures_and_algorithms.data_structures.graphs.adjacency_matrix import AdjacencyMatrix


class Test(unittest.TestCase):
    def test_adjacency_matrix(self):
        nodes = 5
        edges = [(0, 1), (0, 4), (1, 2), (1, 3), (1, 4), (2, 3), (3, 4)]
        matrix = AdjacencyMatrix(nodes, edges)

        self.assertEqual([[0, 1, 0, 0, 1], [1, 0, 1, 1, 1], [0, 1, 0, 1, 0], [0, 1, 1, 0, 1], [1, 1, 0, 1, 0]],
                         matrix.data)
