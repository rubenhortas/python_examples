from data_structures_and_algorithms.algorithms.backtracking.rat_in_a_maze.maze import Maze
from data_structures_and_algorithms.algorithms.backtracking.rat_in_a_maze.rat import Rat


def get_paths(maze: Maze) -> list | None:
    """
    Consider a rat placed at (0, 0) in a square matrix of order N*N.
    Returns all possible paths (in increasing lexicographically order) that the rat can take
    to get from (0,0) to (N-1, N-1).
    
    The directions in which the rat can move are 'U' (Up), 'D' (Down), 'L' (Left), 'R' (Right).

    The value 0 in a cell of the matrix represents that it is blocked and rat cannot move to it.
    The value 1 in a cell of the matrix represents that rat can be travel through it.

    In a path, no cell can be visited more than once.

    :param maze: [[1, 0, 0, 0],[1, 1, 0, 1],[0, 1, 0, 0],[1, 1, 1, 1]]
    :return: ['DRDDRR']
    """

    def get_path(row: int, column: int, position: int, path: str) -> None:
        if row == maze.last_row and column == maze.last_column:
            paths.append(path)
            return

        maze.block(row, column)

        for move in Rat.MOVES:
            next_row = row + move[0]
            next_column = column + move[1]

            if maze.is_valid(next_row, next_column):
                path += Rat.MOVES[move]
                get_path(next_row, next_column, position + 1, path)
                path = path[:-1]

        maze.unblock(row, column)
        return

    paths = []

    get_path(0, 0, 0, '')

    if paths:
        return paths

    return None
