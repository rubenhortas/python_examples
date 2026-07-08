from typing import Iterable


class Board:
    def __init__(self, size: int) -> None:
        self.squares = [[" "] * size for _ in range(size)]
        self.size = len(self.squares)

    def print(self) -> None:
        for row, columns in zip(self.squares, self.squares, strict=True):
            for column in columns:
                print(f"[{column}]", end="")
            print()
        print()

    def is_safe(self, row: int, column: int) -> bool:
        return self._is_row_safe(row) and self._is_column_safe(column) and self._are_diagonals_safe(row, column)

    def place_queen(self, row: int, column: int) -> None:
        self.squares[row][column] = "♛"

    def clear_square(self, row: int, column: int) -> None:
        self.squares[row][column] = " "

    def _is_row_safe(self, row: int) -> bool:
        return all(square != "♛" for square in self.squares[row])

    def _is_column_safe(self, column: int) -> bool:
        return all(row_[column] != "♛" for row_ in self.squares)

    def _are_diagonals_safe(self, row: int, column: int) -> bool:
        return (
            self._is_safe_diagonal(reversed(range(row)), reversed(range(column)))  # Upper left diagonal
            and self._is_safe_diagonal(range(row + 1, self.size), range(column + 1, self.size))  # Bottom right diagonal
            and self._is_safe_diagonal(reversed(range(row)), range(column + 1, self.size))  # Upper right diagonal
            and self._is_safe_diagonal(range(row + 1, self.size), reversed(range(column)))
        )  # Bottom left diagonal

    def _is_safe_diagonal(self, rows_range: Iterable, columns_range: Iterable) -> bool:
        return all(self.squares[row][column] != "♛" for row, column in zip(rows_range, columns_range, strict=False))
