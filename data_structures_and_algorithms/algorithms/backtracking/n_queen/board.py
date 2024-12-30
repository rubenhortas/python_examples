from typing import Iterable


class Board:
    size = 0

    def __init__(self, size):
        self.squares = [[' '] * size for _ in range(size)]
        self.size = len(self.squares)

    def print(self) -> None:
        for row, columns in zip(self.squares, self.squares):
            for column in columns:
                print(f"[{column}]", end='')
            print()
        print()

    def is_safe(self, row: int, column: int) -> bool:
        return self._is_row_safe(row) and self._is_column_safe(column) and self._are_diagonals_safe(row, column)

    def place_queen(self, row: int, column: int) -> None:
        self.squares[row][column] = '♛'

    def clear_square(self, row: int, column: int) -> None:
        self.squares[row][column] = ' '

    def _is_row_safe(self, row: int) -> bool:
        for square in self.squares[row]:
            if square == '♛':
                return False

        return True

    def _is_column_safe(self, column: int) -> bool:
        for row_ in self.squares:
            if row_[column] == '♛':
                return False

        return True

    def _are_diagonals_safe(self, row: int, column: int) -> bool:
        return (self._is_safe_diagonal(reversed(range(row)), reversed(range(column))) and  # Upper left diagonal
                self._is_safe_diagonal(range(row + 1, self.size),
                                       range(column + 1, self.size)) and  # Bottom right diagonal
                self._is_safe_diagonal(reversed(range(row)), range(column + 1, self.size)) and  # Upper right diagonal
                self._is_safe_diagonal(range(row + 1, self.size), reversed(range(column))))  # Bottom left diagonal

    def _is_safe_diagonal(self, rows_range: Iterable, columns_range: Iterable) -> bool:
        for row, column in zip(rows_range, columns_range):
            if self.squares[row][column] == '♛':
                return False

        return True
