import heapq

from data_structures_and_algorithms.data_structures.graphs.graph import Graph


def get_shortest_path(graph: Graph, source_node: int, end_node: int) -> (list, float):
    def update_distances():
        neighbors = graph.nodes[current_node]
        weights = graph.weights[current_node]

        for i, node in enumerate(neighbors):
            weight = weights[i]

            if distances[current_node] + weight < distances[node]:
                distances[node] = distances[current_node] + weight
                predecessors[node] = current_node

    distances = [float('inf')] * graph.num_nodes
    visited = set()
    predecessors = [None] * graph.num_nodes
    # Use a priority queue (min-heap) to efficiently select the next node
    priority_queue = [(0, source_node)]  # (distance, node)
    distances[source_node] = 0
    path = []

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_node in visited:
            continue  # Skip if already visited

        visited.add(current_node)

        if current_node == end_node:
            break

        update_distances()

        for neighbor in graph.nodes[current_node]:
            if neighbor not in visited:
                heapq.heappush(priority_queue, (distances[neighbor], neighbor))

    current = end_node

    while current is not None:
        path.insert(0, current)
        current = predecessors[current]

    return path, distances[end_node]
