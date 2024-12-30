from data_structures_and_algorithms.algorithms.backtracking.rat_in_a_maze.maze import Maze
from data_structures_and_algorithms.algorithms.backtracking.rat_in_a_maze.rat import Rat


def get_paths(maze: Maze) -> list | None:
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
