"""
Implementations of a graph with a dictionary.
"""

# Undirected and weighted graph
graph = {
    '0': {'1': 3, '3': 2, '8': 4},
    '1': {'0': 3, '7': 4},
    '2': {'3': 6, '5': 1, '7': 2},
    '3': {'0': 2, '2': 6, '4': 1},
    '4': {'3': 1, '8': 8},
    '5': {'2': 1, '6': 8},
    '6': {'5': 8},
    '7': {'1': 4, '2': 2},
    '8': {'0': 4, '1': 8}
}

# Directed and weighted graph
graph2 = {
    '0': {'1': 8},
    '1': {'2': 3},
    '2': {'3': 5, '4': 6},
    '3': {'2': 5, '5': 9},
    '4': {}
}

# Undirected and unweighted graph
graph3 = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D'],
    'D': ['B', 'C']
}
