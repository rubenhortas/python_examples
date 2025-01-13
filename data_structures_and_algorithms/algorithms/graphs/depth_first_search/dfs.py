"""
Depth-first search (DFS) is an algorithm for traversing or searching tree or graph data structures.
The algorithm starts at the root node and explores as far as possible along each branch before backtracking.

Main uses:
* Finding connected components
* Topological sort
* Cycle detection
* Maze solving
* Web crawling
* Social network analysis
* AI decision-making (game AI)
"""


def dfs(graph: list, source_node: int) -> list:
    dfs_tour = []
    stack = [source_node]  # For simple stack operations (push and pop) a list is more efficient than deque
    visited = set()

    while stack:
        current_node = stack.pop()

        if current_node not in visited:
            visited.add(current_node)
            dfs_tour.append(current_node)

            for neighbor in graph[current_node]:
                stack.append(neighbor)

    return dfs_tour
