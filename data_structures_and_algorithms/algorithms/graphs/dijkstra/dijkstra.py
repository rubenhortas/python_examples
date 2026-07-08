import heapq

from data_structures_and_algorithms.data_structures.graphs.graph import Graph

INF = 10**9


def get_shortest_path(graph: Graph, start: int, end: int) -> tuple[list, int]:
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

    distances = [INF] * graph.num_nodes
    visited = set()

    # Use a priority queue (min-heap) to efficiently select the next node
    predecessors: list[None | int] = [None] * graph.num_nodes

    priority_queue: list[tuple[int, int]] = [(0, start)]  # (distance, node)
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

    node = end

    while node is not None:
        path.insert(0, node)
        node = predecessors[node]

    return path, distances[end]
