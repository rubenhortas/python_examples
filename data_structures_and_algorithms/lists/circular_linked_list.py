#!/usr/bin/env python3


class Node:
    def __init__(self, data: str):
        self.data = data
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

            for n in nodes:
                node.next = Node(n)
                node = node.next

            node.next = self.head

    def __repr__(self):
        nodes = []

        if self.head is not None:
            node = self.head
            nodes.append(self.head.data)

            while node.next != self.head:
                nodes.append(node.next.data)
                node = node.next

            return f'<- {" -> ".join(nodes)} ->'
        else:
            return ''

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
            self.head.next = node
            return

        for current_node in self:
            pass

        current_node.next = node
        node.next = self.head
        self.head = node

    def add_last(self, node: Node):
        if self.head is None:
            self.head = node
            self.head.next = node
            return

        n = self.head

        while n.next != self.head:
            n = n.next

        n.next = node
        node.next = self.head

    def add_after(self, target_node_data: str, new_node: Node):
        if self.head is None:
            raise Exception('List is empty')

        for node in self:
            if node.data == target_node_data:
                new_node.next = node.next
                node.next = new_node
                return

        raise Exception(f'Node with data \'{target_node_data}\' not found')

    def add_before(self, target_node_data: str, new_node: Node):
        if self.head is None:
            raise Exception('List is empty')

        if self.head.data == target_node_data:
            self.add_first(new_node)

        prev_node = self.head

        for node in self:
            if node.data == target_node_data:
                prev_node.next = new_node
                new_node.next = node
                return

            prev_node = node

        raise Exception(f'Node with data \'{target_node_data}\' not found')


if __name__ == '__main__':
    nodes = ['1', '2', '3', '4', '5']

    circular_linked_list = CircularLinkedList(nodes)
    print(circular_linked_list)
    # return: <- 1 -> 2 -> 3 -> 4 -> 5 ->

    circular_linked_list.add_first(Node('0'))
    print(circular_linked_list)
    # return: <- 0 -> 1 -> 2 -> 3 -> 4 -> 5 ->

    circular_linked_list.add_last(Node('100'))
    print(circular_linked_list)
    # return: <- 0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 100 ->

    circular_linked_list.add_after('5', Node('6'))
    print(circular_linked_list)
    # return: <- 0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 100 ->

    circular_linked_list.add_before('100', Node('99'))
    print(circular_linked_list)
    # return: <- 0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 99 -> 100 ->
