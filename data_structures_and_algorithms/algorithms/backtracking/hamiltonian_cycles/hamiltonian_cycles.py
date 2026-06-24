"""
Hamiltonian Cycle or Circuit in a graph G is a cycle that visits every vertex of G exactly once and returns to the starting vertex.

* If graph contains a Hamiltonian cycle, it is called Hamiltonian graph otherwise it is non-Hamiltonian.
* Hamiltonian Path in a graph G is a path that visits every vertex of G exactly once and Hamiltonian Path doesn't have to return to the starting vertex. It's an open path.
* Hamiltonian Paths have applications in various fields, such as finding optimal routes in transportation networks, circuit design, and graph theory research.
"""


def get_hamiltonian_cycles(graph: list[list[int]]) -> list[list[int]]:
    num_nodes = len(graph)

    if num_nodes == 0:
        return []

    all_cycles: list[list[int]] = []
    start_node = 0

    # Pre-calculate adjacency list to optimize neighbor lookups from O(V) to O(deg(V))
    adj_list = {u: [v for v, connected in enumerate(graph[u]) if connected == 1] for u in range(num_nodes)}

    path = [start_node]
    visited = {start_node}

    def backtrack(current_node: int) -> None:
        # Base Case: All nodes visited
        if len(path) == num_nodes:
            # Check if there is an edge back to the start_node to complete the cycle
            if start_node in adj_list[current_node]:
                # Snapshot the current path in O(N) and append the closing node
                snapshot = list(path)
                snapshot.append(start_node)
                all_cycles.append(snapshot)
            return

        # Pruning & exploration
        for neighbor in adj_list[current_node]:
            if neighbor not in visited:
                # 1. Mutate state (In-place operation: O(1))
                visited.add(neighbor)
                path.append(neighbor)

                # 2. Recurse down the decision tree
                backtrack(neighbor)

                # 3. Undo mutation (Backtrack: O(1))
                visited.remove(neighbor)
                path.pop()

    backtrack(start_node)

    return all_cycles
