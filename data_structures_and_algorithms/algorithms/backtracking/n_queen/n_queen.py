#!/usr/bin/env python3

"""
Place N chess queens on an N×N chessboard such that none of them attack each other.
"""
from data_structures_and_algorithms.algorithms.backtracking.n_queen.board import Board


def play(board_size: int) -> list:
    def place_queen(column: int) -> bool:
        if column == board.size:
            return True

        for row in range(board.size):
            if board.is_safe(row, column):
                board.place_queen(row, column)

                if place_queen(column + 1):
                    return True

                # If placing queen in the square doesn't lead to a solution:
                # Remove the queen from the square
                board.clear_square(row, column)  # Backtracking

        return False

    board = Board(board_size)

    if place_queen(0):
        board.print()
        return board.squares
    else:
        print('There is no solution')
