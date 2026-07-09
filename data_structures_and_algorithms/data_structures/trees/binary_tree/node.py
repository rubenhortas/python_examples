class Node:
    def __init__(self, value: str) -> None:
        self.value = value
        self.left = None
        self.right = None

    def __str__(self) -> str:
        return self.value
