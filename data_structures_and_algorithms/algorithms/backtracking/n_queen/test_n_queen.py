import unittest

from data_structures_and_algorithms.algorithms.backtracking.n_queen.board import Board
from data_structures_and_algorithms.algorithms.backtracking.n_queen.n_queen import get_solution


class Test(unittest.TestCase):
    def test_board(self):
        boards = [
            # (board_size, safe_squares)
            (4, [((0, 1), False), ((0, 2), False), ((0, 3), False),
                 ((1, 0), False), ((1, 1), False), ((1, 2), True), ((1, 3), True),
                 ((2, 0), False), ((2, 1), True), ((2, 2), False), ((2, 3), True),
                 ((3, 0), False), ((3, 1), True), ((3, 2), True), ((3, 3), False), ]),
            (2, [((0, 1), False),
                 ((1, 0), False), ((1, 1), False)])
        ]

        for board in boards:
            board_ = Board(board[0])
            board_.place_queen(0, 0)

            for square in board[1]:
                self.assertEqual(square[1], board_.is_safe(*square[0]))

    def test_get_solutions(self):
        board_4_solution = Board(4)
        board_4_solution.place_queen(0, 2)
        board_4_solution.place_queen(1, 0)
        board_4_solution.place_queen(2, 3)
        board_4_solution.place_queen(3, 1)

        games = [
            # (board_size, solution)
            (2, None),  # There is no solution
            (3, None),  # There is no solution
            (4, board_4_solution.squares)
        ]

        for game in games:
            solution_board = get_solution(game[0])

            if solution_board:
                solution = solution_board.squares
                solution_board.print()
            else:
                solution = None
                print(f"There is no solution for a {game[0]}x{game[0]} board.")

            print()
            self.assertEqual(game[1], solution)
