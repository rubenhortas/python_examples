#!/usr/bin/env python3

# noinspection PyShadowingNames
class LinkedList:
    def __init__(self, nodes=None):
        self.head = None

        if nodes:
            node = Node(nodes.pop(0))
            self.head = node

            for n in nodes:
                node.next = Node(n)
                node = node.next

    def add_first(self, node):
        node.next = self.head
        self.head = node

    def add_last(self, node):
        if self.head is None:
            self.head = node
            return

        for current_node in self:
            pass

        # noinspection PyUnboundLocalVariable
        current_node.next = node

    def add_after(self, target_node_data, new_node):
        if self.head is None:
            raise Exception('List is empty')

        for node in self:
            if node.data == target_node_data:
                new_node.next = node.next
                node.next = new_node
                return

        raise Exception(f"Node with data '{target_node_data}' not found")

    def add_before(self, target_node_data, new_node):
        if self.head is None:
            raise Exception('List is empty')

        if self.head.data == target_node_data:
            return self.add_first(new_node)

        prev_node = self.head

        for node in self:
            if node.data == target_node_data:
                prev_node.next = new_node
                new_node.next = node
                return

            prev_node = node

        raise Exception(f"Node with data '{target_node_data}' not found")

    def remove(self, target_node_data):
        if self.head is None:
            raise Exception('List is empty')

        if self.head.data == target_node_data:
            self.head = self.head.next
            return

        previous_node = self.head

        for node in self:
            if node.data == target_node_data:
                previous_node.next = node.next
                return

            previous_node = node

        raise Exception(f"Node with data '{target_node_data}' not found")

    def __repr__(self):
        node = self.head
        nodes = []

        while node is not None:
            nodes.append(node.data)
            node = node.next

        return " -> ".join(nodes)

    def __iter__(self):
        node = self.head

        while node is not None:
            yield node
            node = node.next


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data


if __name__ == '__main__':
    nodes = ['b', 'c', 'd', 'e']

    linked_list = LinkedList(nodes)
    print(linked_list)

    linked_list.add_first(Node('0'))
    print(linked_list)

    linked_list.add_last(Node('z'))
    print(linked_list)

    linked_list.add_after('e', Node('f'))
    print(linked_list)

    linked_list.add_before('b', Node('a'))
    print(linked_list)

    linked_list.remove('0')
    print(linked_list)
