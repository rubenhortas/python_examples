#!/usr/bin/env python3

from __future__ import annotations

from typing import TYPE_CHECKING

from data_structures_and_algorithms.data_structures.trees.n_ary_tree.node import Node

if TYPE_CHECKING:
    from collections.abc import Iterator
from typing import TypeVar

T = TypeVar("T")


class NAryTree[T]:
    __slots__ = ("parent_node", "root")

    def __init__(self, root_value: T | None = None) -> None:
        self.root: Node | None = Node(root_value) if root_value is not None else None
        self.parent_node: Node

    def insert(self, value: T, parent_value: T | None = None) -> Node | None:
        new_node = Node(value)

        if self.root is None:
            if parent_value is not None:
                raise ValueError("Cannot specify parent_value when tree is empty.")  # noqa: TRY003

            self.root = new_node
            return new_node

        if parent_value is None:
            raise ValueError("parent_value must be provided for non-root insertion.")  # noqa: TRY003

        parent_node = self.find(parent_value)

        if parent_node is None:
            raise KeyError(f"Parent node with value '{parent_value}' not found.")  # noqa: TRY003

        return parent_node.add_child(new_node)

    def delete(self, value: T) -> bool:
        if self.root is None:
            return False

        if self.root.value == value:
            self.root = None
            return True

        target_node = self.find(value)
        parent = None if target_node is None else target_node.parent

        if target_node is None or parent is None:
            return False

        parent.remove_child(value)

        return True

    def find(self, value: T) -> Node | None:
        if self.root is None:
            return None

        for node in self.traverse_preorder():
            if node.value == value:
                return node

        return None

    def traverse_preorder(self) -> Iterator[Node]:
        if self.root is None:
            return

        stack: list[Node] = [self.root]

        while stack:
            current = stack.pop()
            yield current
            stack.extend(reversed(current.children))

    def traverse_postorder(self) -> Iterator[Node]:
        if self.root is None:
            return

        def _postorder(node: Node) -> Iterator[Node]:
            for child in node.children:
                yield from _postorder(child)

            yield node

        yield from _postorder(self.root)

    def traverse_inorder(self) -> Iterator[Node]:
        if self.root is None:
            return

        def _inorder(node: Node) -> Iterator[Node]:
            children = node.children
            num_children = len(children)
            mid = num_children // 2

            for i in range(mid):
                yield from _inorder(children[i])

            yield node

            for i in range(mid, num_children):
                yield from _inorder(children[i])

        yield from _inorder(self.root)

    def traverse_level_order(self) -> Iterator[Node]:
        if self.root is None:
            return

        queue: list[Node] = [self.root]

        while queue:
            current = queue.pop(0)
            yield current
            queue.extend(current.children)
