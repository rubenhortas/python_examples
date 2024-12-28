import unittest

from data_structures_and_algorithms.algorithms.backtracking.n_queen.board import Board
from data_structures_and_algorithms.algorithms.backtracking.n_queen.n_queen import play


class Test(unittest.TestCase):
    def test_board(self):
        board = Board(4)
        board.place_queen(0, 0)
        safe_boxes = [
            ((0, 1), False),
            ((1, 0), False),
            ((1, 1), False),
            ((2, 1), True)
        ]

        for box in safe_boxes:
            self.assertEqual(box[1], board.is_safe(*box[0]))

    def test_play(self):
        result = [
            [' ', ' ', '♛', ' '],
            ['♛', ' ', ' ', ' '],
            [' ', ' ', ' ', '♛'],
            [' ', '♛', ' ', ' ']
        ]
        self.assertEqual(result, play(4))
