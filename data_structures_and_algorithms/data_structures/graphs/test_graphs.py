import unittest

from data_structures_and_algorithms.data_structures.graphs.adjacency_matrix import AdjacencyMatrix
from data_structures_and_algorithms.data_structures.graphs.graph import Graph


class Test(unittest.TestCase):
    def setUp(self):
        self.num_nodes = 5
        self.edges = [(0, 1), (0, 4), (1, 2), (1, 3), (1, 4), (2, 3), (3, 4)]

    def test_graph(self):
        graph = Graph(self.num_nodes, self.edges)

        self.assertEqual([[1, 4], [0, 2, 3, 4], [1, 3], [1, 2, 4], [0, 1, 3]], graph.data)

    def test_adjacency_matrix(self):
        matrix = AdjacencyMatrix(self.num_nodes, self.edges)

        self.assertEqual([[0, 1, 0, 0, 1], [1, 0, 1, 1, 1], [0, 1, 0, 1, 0], [0, 1, 1, 0, 1], [1, 1, 0, 1, 0]],
                         matrix.data)
