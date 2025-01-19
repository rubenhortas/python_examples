from collections import defaultdict


def get_shortest_path(graph: dict, start: str, end: str) -> (list, int):
    # Time complexity: O((nodes+edges)*log(nodes))
    # Auxiliary space: O(nodes)
    distances = defaultdict(lambda: float('inf'))
    distances[start] = 0
    predecessors = {}
    unvisited = set(graph)
    path = []
    current = ''

    while current != end and unvisited:
        current = min(unvisited, key=lambda node: distances[node])
        unvisited.remove(current)

        for neighbor, weight in graph[current].items():
            alternative = distances[current] + weight

            if alternative < distances[neighbor]:
                distances[neighbor] = alternative
                predecessors[neighbor] = current

    current = end

    while current is not None:
        path.insert(0, current)
        current = predecessors.get(current, None)

    return path, distances[end]
