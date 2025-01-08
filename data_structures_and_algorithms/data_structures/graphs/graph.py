class Graph:
    def __init__(self, num_nodes: int, edges: list, directed: bool = False):
        self.num_nodes = num_nodes
        self.directed = directed
        self.weighted = len(edges) > 0 and len(edges[0]) == 3
        self.nodes = [[] for _ in range(num_nodes)]
        self.weights = [[] for _ in range(num_nodes)]

        for edge in edges:  # edge =  (node1, node2)|(node1, node2, weight)
            self.nodes[edge[0]].append(edge[1])

            if self.weighted:
                self.weights[edge[0]].append(edge[2])

            if not directed:
                self.nodes[edge[1]].append(edge[0])

                if self.weighted:
                    self.weights[edge[1]].append(edge[2])

    def __repr__(self):
        result = ''

        if self.weighted:
            print('# node1: [(node2, weight), ..., (node_n, weight)]')

            for i, (nodes, weights) in enumerate(zip(self.nodes, self.weights)):
                result += f"{i}: {list(zip(nodes, weights))}\n"
        else:
            print('# node1: [node2, ..., node_n]')

            for i, nodes in enumerate(self.nodes):
                result += f"{i}: {nodes}\n"
        return result

    def __str__(self):
        return self.__repr__()
