#!/usr/bin/env python3


class Node:
    def __init__(self, data: str):
        self.data = data
        self.prev = None
        self.next = None

    def __repr__(self):
        return self.data


# noinspection PyShadowingNames
class CircularLinkedList:
    def __init__(self, nodes: list = None):
        self.head = None

        if nodes:
            node = Node(nodes.pop(0))
            self.head = node
            self.head.next = node

            prev = self.head

            for n in nodes:
                node.prev = prev
                node.next = Node(n)
                prev = node
                node = node.next

            self.head.prev = node
            node.prev = prev
            node.next = self.head

    def __repr__(self):
        nodes = []

        if self.head is not None:
            node = self.head
            nodes.append(self.head.data)

            while node.next != self.head:
                nodes.append(node.next.data)
                node = node.next

        return f"<- {' <-> '.join(nodes)} ->"

    def __iter__(self):
        if self.head is not None:
            node = self.head
            yield node

            while node.next != self.head:
                yield node.next
                node = node.next

    # noinspection PyUnboundLocalVariable
    def add_first(self, node: Node):
        if self.head is None:
            self.head = node
            self.head.prev = node
            self.head.next = node
            return

        node.next = self.head
        node.prev = self.head.prev
        self.head.prev.next = node
        self.head.prev = node
        self.head = node

    def add_last(self, node: Node):
        if self.head is None:
            self.head = node
            self.head.prev = node
            self.head.next = node
            return

        n = self.head

        while n.next != self.head:
            n = n.next

        n.next = node
        node.prev = n
        node.next = self.head

    def add_after(self, target_node_data: str, new_node: Node):
        if self.head is None:
            raise Exception('List is empty')

        for node in self:
            if node.data == target_node_data:
                new_node.prev = node
                new_node.next = node.next
                node.next = new_node
                return

        raise Exception(f"Node with data '{target_node_data}' not found")

    def add_before(self, target_node_data: str, new_node: Node):
        if self.head is None:
            raise Exception('List is empty')

        if self.head.data == target_node_data:
            self.add_first(new_node)

        prev_node = self.head

        for node in self:
            if node.data == target_node_data:
                prev_node.next = new_node
                new_node.prev = prev_node
                new_node.next = node
                node.prev = new_node
                return

            prev_node = node

        raise Exception(f"Node with data '{target_node_data}' not found")


if __name__ == '__main__':
    nodes = ['1', '2', '3', '4', '5']

    circular_linked_list = CircularLinkedList(nodes)
    print(circular_linked_list)
    # return: <- 1 <-> 2 <-> 3 <-> 4 <-> 5 ->

    circular_linked_list.add_first(Node('0'))
    print(circular_linked_list)
    # return: <- 0 <-> 1 <-> 2 <-> 3 <-> 4 <-> 5 ->

    circular_linked_list.add_last(Node('100'))
    print(circular_linked_list)
    # return: <- 0 <-> 1 <-> 2 <-> 3 <-> 4 <-> 5 <-> 100 ->

    circular_linked_list.add_after('5', Node('6'))
    print(circular_linked_list)
    # return: <- 0 <-> 1 <-> 2 <-> 3 <-> 4 <-> 5 <-> 6 <-> 100 ->

    circular_linked_list.add_before('100', Node('99'))
    print(circular_linked_list)
    # return: <- 0 <-> 1 <-> 2 <-> 3 <-> 4 <-> 5 <-> 6 <-> 99 <-> 100 ->
