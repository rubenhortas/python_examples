from data_structures_and_algorithms.data_structures.graphs.graph import Graph


def get_shortest_path(graph: Graph, source_node: int, end_node: int) -> (list, float):
    distances = [float('inf')] * graph.num_nodes  # float('inf') represents positive infinity as a floating-point number
    visited = {source_node}
    parents = [None] * graph.num_nodes
    queue = [source_node]
    distances[source_node] = 0
    index = 0

    while index < len(queue) and end_node not in visited:
        current_node = queue[index]
        index += 1

        # Update neighbors' distances
        _update_distances(graph, current_node, distances, parents)

        # Find the first unvisited node at the shortest distance
        next_node = _pick_next_node(distances, visited)

        if next_node:
            queue.append(next_node)

        visited.add(current_node)

    return _get_path(parents, source_node, end_node), distances[end_node]


def _update_distances(graph: Graph, current_node: int, distances: list, parents: list):
    neighbors = graph.nodes[current_node]
    weights = graph.weights[current_node]

    for i, node in enumerate(neighbors):
        weight = weights[i]

        if distances[current_node] + weight < distances[node]:
            distances[node] = distances[current_node] + weight
            parents[node] = current_node


def _pick_next_node(distances: list, visited: set) -> int:
    min_distance = float('inf')
    min_node = None

    for node in range(len(distances)):
        if node not in visited and distances[node] < min_distance:
            min_node = node
            min_distance = distances[node]

    return min_node


def _get_path(parents: list, source_node, end_node: int) -> list:
    if not parents:
        return []

    path = [end_node]
    current_node = end_node

    while current_node != source_node:
        path.append(parents[current_node])
        current_node = parents[current_node]

    return path[::-1]
