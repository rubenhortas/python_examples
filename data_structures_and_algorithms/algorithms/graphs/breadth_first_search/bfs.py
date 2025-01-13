"""
Breadth First Search or BFS for a graph

Breadth First Search (BFS) is a fundamental algorithm for traversing graphs.
It starts with a node and then traverses all its adjacent nodes.
Once all the adjacent nodes have been visited, its adjacent node is traversed.

Popular graph algorithms such as Dijkstra's shortest path, Kahn's algorithm, and Prim's algorithm are based on BFS.

BFS can be used to detect cycles in a directed and undirected graph, find the shortest path in an unweighted graph, and many other problems.

Main uses:
* Finding the shortest paths
* Level order traversal
* Bipartite graph check
"""
from collections import deque


def bfs(graph: list, source_node: int) -> list:
    bfs_tour = []
    queue = deque()
    visited = set()

    visited.add(source_node)
    queue.append(source_node)

    while queue:
        current_node = queue.popleft()
        bfs_tour.append(current_node)

        for neighbor in graph[current_node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return bfs_tour
