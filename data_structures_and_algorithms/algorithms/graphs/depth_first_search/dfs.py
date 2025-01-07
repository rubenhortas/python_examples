"""
Depth-first search (DFS) is an algorithm for traversing or searching tree or graph data structures.
The algorithm starts at the root node and explores as far as possible along each branch before backtracking.
"""
from collections import deque


def dfs(graph: list, source_node: int) -> list:
    dfs_tour = []
    stack = deque()
    visited_nodes = [False] * len(graph)
    stack.append(source_node)

    while stack:
        current_node = stack.pop()

        if not visited_nodes[current_node]:
            visited_nodes[current_node] = True
            dfs_tour.append(current_node)

            for adjacent_node in graph[current_node]:
                stack.append(adjacent_node)

    return dfs_tour
