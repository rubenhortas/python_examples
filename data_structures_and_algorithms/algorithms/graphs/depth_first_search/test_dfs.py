import unittest

from data_structures_and_algorithms.algorithms.graphs.depth_first_search.dfs import dfs


class Test(unittest.TestCase):
    def test_dfs(self):
        nodes = 5
        edges = [(0, 1), (0, 4), (1, 2), (1, 3), (1, 4), (2, 3), (3, 4)]
        graph = [[] for _ in range(nodes)]

        for node1, node2 in edges:  # Adjacency matrix
            graph[node1].append(node2)
            graph[node2].append(node1)

        print(dfs(graph, 0))
        print(dfs(graph, 3))

        self.assertEqual([0, 4, 3, 2, 1], dfs(graph, 0))
        self.assertEqual([3, 4, 1, 2, 0], dfs(graph, 3))
