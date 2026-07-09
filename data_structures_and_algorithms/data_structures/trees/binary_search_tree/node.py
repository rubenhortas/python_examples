class Node:
    def __init__(self, value: int) -> None:
        self.value = value
        self.count = 1
        self.left = None
        self.right = None

    def __str__(self) -> str:
        return f"{self.value} ({self.count})"
