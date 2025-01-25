import heapq
from typing import Tuple

from data_structures_and_algorithms.data_structures.graphs.graph import Graph


def get_shortest_path(graph: Graph, start: int, end: int) -> (list, float):
    # Time complexity: O((nodes+edges)*log(nodes))
    # Auxiliary space: O(nodes)

    def update_distances() -> None:
        neighbors = graph.nodes[current]
        weights = graph.weights[current]

        for i, node in enumerate(neighbors):
            weight = weights[i]

            if distances[current] + weight < distances[node]:
                distances[node] = distances[current] + weight
                predecessors[node] = current

    distances = [float('inf')] * graph.num_nodes
    visited = set()
    predecessors = [None] * graph.num_nodes
    # Use a priority queue (min-heap) to efficiently select the next node
    priority_queue: list[Tuple[float, float]] = [(0, start)]  # (distance, node)
    distances[start] = 0
    path = []

    while priority_queue:
        distance, current = heapq.heappop(priority_queue)

        if current in visited:
            continue  # Skip if already visited

        visited.add(current)

        if current == end:
            break

        update_distances()

        for neighbor in graph.nodes[current]:
            if neighbor not in visited:
                heapq.heappush(priority_queue, (distances[neighbor], neighbor))

    current = end

    while current is not None:
        path.insert(0, current)
        current = predecessors[current]

    return path, distances[end]
