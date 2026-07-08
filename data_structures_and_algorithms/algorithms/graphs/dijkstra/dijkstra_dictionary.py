from collections import defaultdict

INF = 10**9


def get_shortest_path(graph: dict, start: str, end: str) -> tuple[list, int]:
    # Time complexity: O((nodes+edges)*log(nodes))
    # Auxiliary space: O(nodes)

    distances = defaultdict(lambda: INF)
    distances[start] = 0
    predecessors = {}
    unvisited = set(graph)
    path = []
    current = ""

    while current != end and unvisited:
        current = min(unvisited, key=lambda node: distances[node])
        unvisited.remove(current)

        for neighbor, weight in graph[current].items():
            alternative = distances[current] + weight

            if alternative < distances[neighbor]:
                distances[neighbor] = alternative
                predecessors[neighbor] = current

    node = end

    while node is not None:
        path.insert(0, node)
        node = predecessors.get(node)

    return path, distances[end]
