import unittest

from data_structures_and_algorithms.algorithms.graphs.breadth_first_search.bfs import bfs


class Test(unittest.TestCase):
    def test_bfs(self):
        nodes = 5
        edges = [(0, 1), (0, 4), (1, 2), (1, 3), (1, 4), (2, 3), (3, 4)]
        graph = [[] for _ in range(nodes)]

        for node1, node2 in edges:  # Adjacency matrix
            graph[node1].append(node2)
            graph[node2].append(node1)

        self.assertCountEqual([0, 1, 4, 2, 3], bfs(graph, 0))
