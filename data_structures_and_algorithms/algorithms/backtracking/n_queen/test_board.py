import unittest

from data_structures_and_algorithms.algorithms.backtracking.n_queen.board import Board


class Test(unittest.TestCase):
    def setUp(self):
        self.board = Board(4)
        self.board.place_queen(0, 0)
        self.safe_boxes = [
            ((0, 1), False),
            ((1, 0), False),
            ((1, 1), False),
            ((2, 1), True)
        ]

    def test_board(self):
        for box in self.safe_boxes:
            self.assertEqual(box[1], self.board.is_safe(*box[0]))
