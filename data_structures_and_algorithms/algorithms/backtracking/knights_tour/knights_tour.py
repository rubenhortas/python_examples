from data_structures_and_algorithms.algorithms.backtracking.knights_tour.board import Board
from data_structures_and_algorithms.algorithms.backtracking.knights_tour.knight import Knight


def get_solution(board_size: int) -> Board | None:
    """
    Given an empty board of size n*n, with a knight placed in the first block,
    prints the order of each square visited (according to the rules of chess)
    if the knight can only visit each square once.

    :param board_size: board size
    :return: Board | None
    """
    # Time complexity: O(8*n^2)  (8 is the number of possible moves of the knight, n is the board size)
    # Auxiliary space: O(n^2)

    def has_solution(row: int, column: int, position: int) -> bool:
        if position == board.max_position:
            return True

        for move in Knight.MOVES:
            next_square = (row + move[0], column + move[1])

            if board.is_valid(next_square[0], next_square[1]):
                board.set_position(next_square[0], next_square[1], position)

                if has_solution(next_square[0], next_square[1], position + 1):
                    return True

                board.clear(next_square[0], next_square[1])  # Backtracking

        return False

    board = Board(board_size)
    board.set_position(0, 0, 0)  # The Knight placed on the first block of the empty board

    if has_solution(0, 0, 1):
        return board

    return None
