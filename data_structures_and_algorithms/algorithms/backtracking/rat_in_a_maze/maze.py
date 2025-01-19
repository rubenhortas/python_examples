class Maze:

    def __init__(self, squares: list, solutions: list):
        self.squares = squares
        self.solutions = solutions
        self.last_row = len(squares) - 1
        self.last_column = self.last_row
        self._length = len(squares)

    def is_valid(self, row: int, column: int) -> bool:
        return 0 <= row < self._length and 0 <= column < self._length and self.squares[row][column] == 1

    def block(self, row: int, colum: int) -> None:
        self.squares[row][colum] = 0

    def unblock(self, row: int, colum: int) -> None:
        self.squares[row][colum] = 1

    def print(self) -> None:
        for row, columns in zip(self.squares, self.squares):
            for column in columns:
                print(f"[{column}]", end='')
            print()
        print()
