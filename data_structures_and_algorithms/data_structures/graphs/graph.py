class Graph:
    """
    Undirected and unweighted graph.
    """

    def __init__(self, num_nodes: int, edges: list):
        self.num_nodes = num_nodes
        self.data = [[] for _ in range(num_nodes)]

        for node1, node2 in edges:
            self.data[node1].append(node2)
            self.data[node2].append(node1)

    def __repr__(self):
        return '\n'.join([f"{node}: {neighbors}" for node, neighbors in enumerate(self.data)])

    def __str__(self):
        return self.__repr__()
