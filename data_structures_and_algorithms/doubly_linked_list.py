#!/usr/bin/env python3

# noinspection PyShadowingNames
class DoublyLinkedList:
    def __init__(self, nodes=None):
        self.head = None

        if nodes:
            node = Node(nodes.pop(0))
            self.head = node

            for n in nodes:
                node.next = Node(n)
                node.next.prev = node
                node = node.next

    def __repr__(self):
        node = self.head
        nodes = []

        while node is not None:
            nodes.append(node.data)
            node = node.next

        return " <-> ".join(nodes)

    def __iter__(self):
        node = self.head

        while node is not None:
            yield node
            node = node.next

    def add_first(self, node):
        node.next = self.head
        self.head = node

    # noinspection PyUnboundLocalVariable
    def add_last(self, node):
        if self.head is None:
            self.head = node
            return

        for current_node in self:
            print(current_node)

        current_node.next = node

    def add_after(self, target_node_data, new_node):
        if self.head is None:
            raise Exception('List is empty')

        for node in self:
            if node.data == target_node_data:
                new_node.next = node.next
                new_node.prev = node
                node.next = new_node
                return

        raise Exception(f"Node with data '{target_node_data}' not found")

    def add_before(self, target_node_data, new_node):
        if self.head is None:
            raise Exception('List is empty')

        if self.head.data == target_node_data:
            self.add_first(new_node)
            return

        for node in self:
            if node.data == target_node_data:
                new_node.next = node
                new_node.prev = node.prev
                node.prev.next = new_node
                node.prev = new_node
                return

        raise Exception(f"Node with data '{target_node_data}' not found")

    def remove(self, target_node_data):
        if self.head is None:
            raise Exception('List is empty')

        if self.head.data == target_node_data:
            self.head = self.head.next
            return

        prev_node = self.head

        for node in self:
            if node.data == target_node_data:
                prev_node.next = node.next
                node.next.prev = prev_node
                return

            prev_node = node

        raise Exception(f"Node with data '{target_node_data}' not found")


# noinspection PyShadowingBuiltins
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

    def __repr__(self):
        prev = "None" if self.prev is None else self.prev.data
        next = "None" if self.next is None else self.next.data

        return f"{prev} <- {self.data} -> {next}"


if __name__ == '__main__':
    nodes = ['b', 'c', 'd', 'e']

    doubly_linked_list = DoublyLinkedList(nodes)
    print(doubly_linked_list)

    doubly_linked_list.add_first(Node('a'))
    print(doubly_linked_list)

    doubly_linked_list.add_last(Node('z'))
    print(doubly_linked_list)

    doubly_linked_list.add_after('e', Node('z'))
    print(doubly_linked_list)

    doubly_linked_list.add_before('a', Node('0'))
    print(doubly_linked_list)

    doubly_linked_list.remove('a')
    print(doubly_linked_list)
