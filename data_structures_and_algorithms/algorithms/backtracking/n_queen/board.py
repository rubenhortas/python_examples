class Board:
    size = 0

    def __init__(self, size):
        self.board = [[' '] * size for _ in range(size)]
        self.size = len(self.board)

    def print(self) -> None:
        for row in self.board:
            for column in row:
                print(f"[{column}]", end='')

            print()
        print()

    def is_safe(self, row: int, column: int) -> bool:
        for box in self.board[row]:  # Check row
            if box == '♛':
                return False

        # Check column
        for row_ in self.board:
            if row_[column] == '♛':
                return False

        # Check upper left diagonal
        for i, j in zip(reversed(range(row + 1)), reversed(range(column + 1))):
            if self.board[i][j] == '♛':
                return False

        # Check bottom right diagonal
        for i, j in zip(range(row + 1, self.size), range(column + 1, self.size)):
            if self.board[i][j] == '♛':
                return False

        return True

    def place_queen(self, row: int, column: int) -> None:
        self.board[row][column] = '♛'

    def clear_square(self, row: int, column: int) -> None:
        self.board[row][column] = ' '
