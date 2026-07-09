class Node:
    def __init__(self, value: int) -> None:
        self.value: int = value
        self.left: Node | None = None
        self.right: Node | None = None
        self.height: int = 1

    def __repr__(self) -> str:
        return f"{self.value}, Left: {self.left!s}, Right: {self.right!s}, Height: {self.height}"

    def __str__(self) -> str:
        return f"{self.value}"
