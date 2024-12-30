# Consider a rat placed at (0, 0) in a square matrix of order N * N.
# It has to reach the destination at (N – 1, N – 1).
# Find all possible paths that the rat can take to reach from source to destination.
# The directions in which the rat can move are ‘U'(up), ‘D'(down), ‘L’ (left), ‘R’ (right).
# Value 0 at a cell in the matrix represents that it is blocked and rat cannot move to it
# while value 1 at a cell in the matrix represents that rat can be travel through it.
# Return the list of paths in lexicographically increasing order.
# Note: In a path, no cell can be visited more than one time. If the source cell is 0,
# the rat cannot move to any other cell.
import unittest

from data_structures_and_algorithms.algorithms.backtracking.rat_in_a_maze.maze import Maze
from data_structures_and_algorithms.algorithms.backtracking.rat_in_a_maze.rat_in_a_maze import get_paths


class Test(unittest.TestCase):
    def test_get_paths(self):
        mazes = [
            Maze([
                [1, 0, 0, 0],
                [1, 1, 0, 1],
                [0, 1, 0, 0],
                [1, 1, 1, 1]
            ], ['DRDDRR']),
            Maze([
                [1, 0, 0, 0],
                [1, 1, 0, 1],
                [1, 1, 0, 0],
                [0, 1, 1, 1]
            ], ['DDRDRR', 'DRDDRR'])
        ]

        for maze in mazes:
            maze.print()
            solutions = get_paths(maze)

            if solutions:
                print(solutions)
                self.assertEqual(maze.solutions, solutions)
            else:
                print("There is not solution.")
                self.assertIsNone(solutions)

            print()
