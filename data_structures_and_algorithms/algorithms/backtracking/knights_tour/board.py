class Board:
    _BLANK = '  '

    def __init__(self, size):
        self.squares = [[self._BLANK] * size for _ in range(size)]
        self.size = len(self.squares)
        self.max_position = self.size ** 2

    def print(self) -> None:
        for row, columns in zip(self.squares, self.squares):
            for column in columns:
                print(f"[{column}]", end='')
            print()
        print()

    def is_valid(self, row: int, column: int) -> bool:
        return self._is_in_range(row, column) and self._is_empty(row, column)

    def set_position(self, row: int, column: int, position: int) -> None:
        self.squares[row][column] = f"{position:2d}"

    def clear(self, row: int, column: int) -> None:
        self.squares[row][column] = self._BLANK

    def _is_in_range(self, row: int, column: int) -> bool:
        return 0 <= row < self.size and 0 <= column < self.size

    def _is_empty(self, row: int, column: int) -> bool:
        return self.squares[row][column] == self._BLANK
