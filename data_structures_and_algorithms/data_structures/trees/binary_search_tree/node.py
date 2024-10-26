class Node:
    def __init__(self, value: int):
        self.value = value
        self.count = 1
        self.left = None
        self.right = None

    def __str__(self):
        return f"{self.value} ({self.count})"
