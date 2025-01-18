#!/usr/bin/env python3

from collections import defaultdict


def dijkstra(graph, start):
    """
    Finds the shortest paths from a given start node to all other nodes in a weighted graph.

    Args:
        graph: A dictionary representing the graph.
               Keys are nodes, values are dictionaries of adjacent nodes and their weights.
        start: The starting node.

    Returns:
        A tuple containing:
            - distances: A dictionary of shortest distances from the start node to each node.
            - predecessors: A dictionary of the predecessor node for each node on the shortest path.
    """

    distances = defaultdict(lambda: float('inf'))
    distances[start] = 0
    predecessors = {}
    unvisited = set(graph)

    while unvisited:
        current = min(unvisited, key=lambda node: distances[node])
        unvisited.remove(current)

        for neighbor, weight in graph[current].items():
            alternative = distances[current] + weight

            if alternative < distances[neighbor]:
                distances[neighbor] = alternative
                predecessors[neighbor] = current

    return distances, predecessors


graph = {
    '0': {'1': 3, '3': 2, '8': 4},
    '1': {'0': 3, '7': 4},
    '2': {'3': 6, '5': 1, '7': 2},
    '3': {'0': 2, '2': 6, '4': 1},
    '4': {'3': 1, '8': 8},
    '5': {'2': 1, '6': 8},
    '6': {'5': 8},
    '7': {'1': 4, '2': 2},
    '8': {'0': 4, '4': 8}
}

distances, predecessors = dijkstra(graph, '2')

print("Distances from A:")
for node, distance in distances.items():
    print(f"{node}: {distance}")

print("\nPredecessors:")
for node, predecessor in predecessors.items():
    print(f"{node}: {predecessor}")
