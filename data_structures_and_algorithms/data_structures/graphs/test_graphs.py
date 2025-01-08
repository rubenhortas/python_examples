import unittest

from data_structures_and_algorithms.data_structures.graphs.graph import Graph


class Test(unittest.TestCase):
    def test_undirected_unweighted_graph(self):
        nodes = 5
        edges = [(0, 1), (0, 4), (1, 2), (1, 3), (1, 4), (2, 3), (3, 4)]
        graph = Graph(nodes, edges)

        self.assertEqual([[1, 4], [0, 2, 3, 4], [1, 3], [1, 2, 4], [0, 1, 3]], graph.nodes)

    def test_undirected_weighted_graph(self):
        num_nodes = 9
        edges = [(0, 1, 3), (0, 3, 2), (0, 8, 4), (1, 7, 4), (2, 7, 2), (2, 3, 6), (2, 5, 1), (3, 4, 1), (4, 8, 8),
                 (5, 6, 8)]  # (node1, node2, weight)
        graph = Graph(num_nodes, edges)

        self.assertEqual([[1, 3, 8], [0, 7], [7, 3, 5], [0, 2, 4], [3, 8], [2, 6], [5], [1, 2], [0, 4]],
                         graph.nodes)

    def test_directed_unweighted_graph(self):
        num_nodes = 5
        edges = [(0, 1), (1, 2), (2, 3), (2, 4), (4, 2), (3, 0)]
        graph = Graph(num_nodes, edges, directed=True)

        self.assertEqual([[1], [2], [3, 4], [0], [2]], graph.nodes)

    def test_directed_weighted_graph(self):
        num_nodes = 6
        edges = [(0, 1, 4), (0, 2, 2), (1, 3, 10), (1, 2, 5), (2, 4, 3), (3, 5, 11),
                 (4, 3, 4)]  # (node1, node2, weight)
        graph = Graph(num_nodes, edges, directed=True)

        self.assertEqual([[1, 2], [3, 2], [4], [5], [3], []], graph.nodes)
