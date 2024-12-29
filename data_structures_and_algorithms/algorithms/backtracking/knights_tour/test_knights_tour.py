import unittest

from data_structures_and_algorithms.algorithms.backtracking.knights_tour.board import Board
from data_structures_and_algorithms.algorithms.backtracking.knights_tour.knights_tour import get_solution


class Test(unittest.TestCase):
    def test_board(self):
        board = Board(8)
        board.set_position(0, 0, 0)
        board.print()

    def test_get_solution(self):
        games = [
            (3, None),
            (4, None),
            (5, [
                [' 0', ' 5', '14', ' 9', '20'],
                ['13', ' 8', '19', ' 4', '15'],
                ['18', ' 1', ' 6', '21', '10'],
                [' 7', '12', '23', '16', ' 3'],
                ['24', '17', ' 2', '11', '22']
            ]),
            (8, [
                [' 0', '59', '38', '33', '30', '17', ' 8', '63'],
                ['37', '34', '31', '60', ' 9', '62', '29', '16'],
                ['58', ' 1', '36', '39', '32', '27', '18', ' 7'],
                ['35', '48', '41', '26', '61', '10', '15', '28'],
                ['42', '57', ' 2', '49', '40', '23', ' 6', '19'],
                ['47', '50', '45', '54', '25', '20', '11', '14'],
                ['56', '43', '52', ' 3', '22', '13', '24', ' 5'],
                ['51', '46', '55', '44', '53', ' 4', '21', '12']
            ])
        ]

        for game in games:
            solution_board = get_solution(game[0])

            if solution_board:
                print(f"Solution for a {game[0]}x{game[0]} board:")
                solution_board.print()
                self.assertEqual(game[1], solution_board.squares)
            else:
                print(f"There is no solution for a {game[0]}x{game[0]} board.")
                self.assertIsNone(solution_board)

            print()
