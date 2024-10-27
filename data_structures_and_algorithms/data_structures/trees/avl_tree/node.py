class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1

    def __repr__(self):
        return f"{self.value}, Left: {str(self.left)}, Right: {str(self.right)}, Height: {self.height}"

    def __str__(self):
        return f"{self.value}"
