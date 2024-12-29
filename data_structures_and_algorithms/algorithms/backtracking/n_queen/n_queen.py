from data_structures_and_algorithms.algorithms.backtracking.n_queen.board import Board


def get_solution(board_size: int) -> Board | None:
    """
    Places N chess queens on an n*n chessboard such that none of them attack each other.
    :param board_size:
    :return: Board | None
    """

    # Time complexity: O(n!) (n = board_size)
    # Auxiliary space: O(n^2)
    def has_solution(column: int) -> bool:
        if column == board.size:
            return True

        for row in range(board.size):
            if board.is_square_safe(row, column):
                board.place_queen(row, column)

                if has_solution(column + 1):
                    return True

                # If placing the queen in the square doesn't lead to a solution:
                # Remove the queen from the square
                board.clear_square(row, column)  # Backtracking

        return False

    board = Board(board_size)

    if has_solution(0):
        return board

    return None
