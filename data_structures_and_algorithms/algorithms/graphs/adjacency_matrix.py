"""
Adjacency Matrix is a square matrix used to represent a finite graph by storing the relationships between the nodes in their respective cells.

Advantages of Adjacency Matrix:

    Simple: Simple and Easy to implement.
    Space Efficient for Dense Graphs: Space efficient when the graph is dense as it requires V * V space to represent the entire graph.
    Faster access to Edges: Adjacency Matrix allows constant look up to check whether there exists an edge between a pair of vertices.

Disadvantages of Adjacency Matrix:

    Space inefficient for Sparse Graphs: Takes up O(V* V) space even if the graph is sparse.
    Costly Insertions and Deletions: Adding or deleting a vertex can be costly as it requires resizing the matrix.
    Slow Traversals: Graph traversals like DFS, BFS takes O(V * V) time to visit all the vertices whereas Adjacency List takes only O(V + E).
"""


class AdjacencyMatrix:
    def __init__(self, nodes, edges):
        self.data = [[0] * nodes for _ in range(nodes)]

        # ꝏ
        for node1, node2 in edges:
            # In an adjacency matrix for a directed and weighted graph, we will replace the '1' with:
            # * 'ꝏ' (infinite, -1, etc.) if there is no edge
            # * 'weight_value' if there is an edge
            self.data[node1][node2] = 1
            self.data[node2][node1] = 1

    def __repr__(self):
        return '\n'.join(str(row) for row in self.data)

    def __str__(self):
        return self.__repr__()
