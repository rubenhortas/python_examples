"""
Hamiltonian Cycle or Circuit in a graph G is a cycle that visits every vertex of G exactly once and returns to the starting vertex.

* If graph contains a Hamiltonian cycle, it is called Hamiltonian graph otherwise it is non-Hamiltonian.
* Hamiltonian Path in a graph G is a path that visits every vertex of G exactly once and Hamiltonian Path doesn’t have to return to the starting vertex. It’s an open path.
* Hamiltonian Paths have applications in various fields, such as finding optimal routes in transportation networks, circuit design, and graph theory research.
"""


def get_hamiltonian_cycles(graph: list) -> list[list]:
    def get_cycles(node: int) -> list[list]:
        if len(path) == num_nodes and graph[node][start_node] == 1:
            return [path + [start_node]]

        cycles = []

        for neighbor in range(num_nodes):
            if graph[node][neighbor] == 1 and neighbor not in visited:
                visited.add(neighbor)
                path.append(neighbor)

                cycles.extend(get_cycles(neighbor))

                visited.remove(neighbor)
                path.pop()

        return cycles

    num_nodes = len(graph)
    start_node = 0
    path = [start_node]
    visited = {start_node}

    return get_cycles(start_node)
