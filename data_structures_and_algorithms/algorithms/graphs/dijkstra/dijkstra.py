from data_structures_and_algorithms.data_structures.graphs.graph import Graph


def get_shortest_path(graph: Graph, source_node: int, end_node: int) -> (list, float):
    distances = [float('inf')] * graph.num_nodes  # float('inf') represents positive infinity as a floating-point number
    visited_nodes = [False] * graph.num_nodes
    parents = [None] * graph.num_nodes
    queue = []
    distances[source_node] = 0
    queue.append(source_node)
    visited_nodes[source_node] = True
    index = 0

    while index < len(queue) and not visited_nodes[end_node]:
        current_node = queue[index]
        index += 1

        # Update neighbors' distances
        _update_distances(graph, current_node, distances, parents)

        # Find the first unvisited node with at the shortest distance
        next_node = _pick_next_node(distances, visited_nodes)

        if next_node:
            queue.append(next_node)

        visited_nodes[current_node] = True

    return _get_path(parents, source_node, end_node), distances[end_node]


def _update_distances(graph: Graph, current_node: int, distances: list, parents: list):
    neighbors = graph.nodes[current_node]
    weights = graph.weights[current_node]

    for i, node in enumerate(neighbors):
        weight = weights[i]

        if distances[current_node] + weight < distances[node]:
            distances[node] = distances[current_node] + weight
            parents[node] = current_node


def _pick_next_node(distances: list, visited_nodes: list) -> int:
    min_distance = float('inf')
    min_node = None

    for node in range(len(distances)):
        if not visited_nodes[node] and distances[node] < min_distance:
            min_node = node
            min_distance = distances[node]

    return min_node


def _get_path(parents: list, source_node, end_node: int) -> list:
    path = []

    if parents:
        path.append(end_node)
        current_node = end_node

        while current_node != source_node:
            path.append(parents[current_node])
            current_node = parents[current_node]

        return path[::-1]
