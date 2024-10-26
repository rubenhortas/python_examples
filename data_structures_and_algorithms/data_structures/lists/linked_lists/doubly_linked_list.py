class Node:
    def __init__(self, data: str):
        self.data = data
        self.prev = None
        self.next = None

    def __repr__(self):
        prev = 'None' if self.prev is None else self.prev.data
        next = 'None' if self.next is None else self.next.data

        return f"{prev} <- {self.data} -> {next}"


# noinspection PyShadowingNames
class DoublyLinkedList:
    def __init__(self, nodes: list = None):
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

        return ' <-> '.join(nodes)

    def __iter__(self):
        node = self.head

        while node is not None:
            yield node
            node = node.next

    def add_first(self, node: Node):
        node.next = self.head
        self.head = node

    def add_last(self, node: Node):
        if self.head is None:
            self.head = node
            return

        n = self.head

        while n.next is not None:
            n = n.next

        n.next = node

    def add_after(self, target_node_data: str, new_node: Node):
        if self.head is None:
            raise Exception('List is empty')

        for node in self:
            if node.data == target_node_data:
                new_node.next = node.next
                new_node.prev = node
                node.next = new_node
                return

        raise Exception(f"Node with data '{target_node_data}' not found")

    def add_before(self, target_node_data: str, new_node: Node):
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

    def remove(self, target_node_data: str):
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


if __name__ == '__main__':
    nodes = ['b', 'c', 'd', 'e']

    doubly_linked_list = DoublyLinkedList(nodes)
    print(doubly_linked_list)
    # return: b <-> c <-> d <-> e

    doubly_linked_list.add_first(Node('a'))
    print(doubly_linked_list)
    # return: a <-> b <-> c <-> d <-> e

    doubly_linked_list.add_last(Node('z'))
    print(doubly_linked_list)
    # return: a <-> b <-> c <-> d <-> e <-> z

    doubly_linked_list.add_after('e', Node('y'))
    print(doubly_linked_list)
    # return: a <-> b <-> c <-> d <-> e <-> y <-> z

    doubly_linked_list.add_before('a', Node('0'))
    print(doubly_linked_list)
    # return: 0 <-> a <-> b <-> c <-> d <-> e <-> y <-> z

    doubly_linked_list.remove('a')
    print(doubly_linked_list)
    # return: 0 <-> b <-> c <-> d <-> e <-> y <-> z
