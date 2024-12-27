class Board:
    size = 0

    def __init__(self, size):
        self.squares = [[' '] * size for _ in range(size)]
        self.size = len(self.squares)

    def print(self) -> None:
        for row in self.squares:
            for column in row:
                print(f"[{column}]", end='')

            print()
        print()

    def is_safe(self, row: int, column: int) -> bool:
        # Check row
        for box in self.squares[row]:
            if box == '♛':
                return False

        # Check column
        for row_ in self.squares:
            if row_[column] == '♛':
                return False

        # Check upper left diagonal
        for i, j in zip(reversed(range(row)), reversed(range(column))):
            if self.squares[i][j] == '♛':
                return False

        # Check bottom right diagonal
        for i, j in zip(range(row + 1, self.size), range(column + 1, self.size)):
            if self.squares[i][j] == '♛':
                return False

        return True

    def place_queen(self, row: int, column: int) -> None:
        self.squares[row][column] = '♛'

    def clear_square(self, row: int, column: int) -> None:
        self.squares[row][column] = ' '
