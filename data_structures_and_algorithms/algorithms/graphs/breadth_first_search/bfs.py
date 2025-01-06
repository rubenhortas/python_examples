"""
Breadth First Search or BFS for a graph

Breadth First Search (BFS) is a fundamental algorithm for traversing graphs.
It starts with a node and then traverses all its adjacent nodes.
Once all the adjacent nodes have been visited, its adjacent node is traversed.

Popular graph algorithms such as Dijkstra's shortest path, Kahn's algorithm, and Prim's algorithm are based on BFS.

BFS can be used to detect cycles in a directed and undirected graph, find the shortest path in an unweighted graph, and many other problems.
"""
from collections import deque


def bfs(graph: list, source_node: int) -> list:
    bfs_tour = []
    queue = deque()
    visited = [False] * len(graph)
    visited[source_node] = True
    queue.append(source_node)

    while queue:
        current_node = queue.popleft()
        bfs_tour.append(current_node)

        for adjacent_node in graph[current_node]:
            if not visited[adjacent_node]:
                visited[adjacent_node] = True
                queue.append(adjacent_node)

    return bfs_tour
