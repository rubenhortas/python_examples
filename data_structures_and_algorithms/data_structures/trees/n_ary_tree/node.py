from __future__ import annotations

from typing import TypeVar

T = TypeVar("T")


class Node:
    __slots__ = ("_children", "_parent", "value")

    def __init__(self, value: T) -> None:
        self.value: T = value
        self._children: dict[T, Node] = {}
        self._parent: Node | None = None

    @property
    def parent(self) -> Node | None:
        return self._parent

    @property
    def children(self) -> tuple[Node, ...]:
        return tuple(self._children.values())

    def is_leaf(self) -> bool:
        return len(self._children) == 0

    def add_child(self, child_node: Node) -> Node:
        if child_node.value in self._children:
            raise ValueError(f"Child with value '{child_node.value}' already exists.")  # noqa: TRY003

        if child_node._parent is not None:
            child_node._parent.remove_child(child_node.value)

        child_node._parent = self
        self._children[child_node.value] = child_node

        return child_node

    def remove_child(self, value: T) -> Node:
        if value not in self._children:
            raise KeyError(f"Child with value '{value}' not found.")  # noqa: TRY003

        removed_node = self._children.pop(value)
        removed_node._parent = None

        return removed_node
