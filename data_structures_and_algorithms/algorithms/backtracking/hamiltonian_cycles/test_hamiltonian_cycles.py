import unittest

from data_structures_and_algorithms.algorithms.backtracking.hamiltonian_cycles.hamiltonian_cycles import \
    get_hamiltonian_cycles


class Test(unittest.TestCase):
    def test_get_hamiltonian_cycles(self):
        graphs = [
            ([[0, 1, 0, 1, 0], [1, 0, 1, 1, 1], [0, 1, 0, 0, 1], [1, 1, 0, 0, 1], [0, 1, 1, 1, 0]],
             [[0, 1, 2, 4, 3, 0], [0, 3, 4, 2, 1, 0]]),
            ([[0, 1, 0, 1, 0], [1, 0, 1, 1, 1], [0, 1, 0, 0, 1], [1, 1, 0, 0, 0], [0, 1, 1, 0, 0]], [])
        ]

        for graph, result in graphs:
            self.assertEqual(result, get_hamiltonian_cycles(graph))
