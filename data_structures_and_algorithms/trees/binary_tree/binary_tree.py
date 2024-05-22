from collections import deque
from queue import Queue

from binary_tree_node import BinaryTreeNode


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, new_value: str) -> None:
        """
        Insertion in level order traversal.

        Time complexity: O(n)
        Auxiliary space: O(n)
        """
        new_node = BinaryTreeNode(new_value)

        if self.root:
            queue = Queue()
            queue.put(self.root)

            while not queue.empty():
                node = queue.get()

                if node:
                    if node.left:
                        queue.put(node.left)
                    else:
                        node.left = new_node
                        break

                    if node.right:
                        queue.put(node.right)
                    else:
                        node.right = new_node
                        break
        else:
            self.root = new_node

    def delete(self, value: str) -> None:
        """
        Deletion of a node using level order traversal.
        The deleted node is replaced by the bottom-most and rightmost node.

        Time complexity: O(n)
        Auxiliary Space: O(n)
        """

        def delete_node(node_to_delete: BinaryTreeNode) -> None:
            queue = Queue()
            queue.put(self.root)

            while not queue.empty():
                node = queue.get()

                if node.left == node_to_delete:
                    node.left = None
                    return
                else:
                    queue.put(node.left)

                if node.right == node_to_delete:
                    node.right = None
                    return
                else:
                    queue.put(node.right)

        if self.root:
            queue = Queue()
            queue.put(self.root)
            deepest_rightmost_node = None
            node_to_delete = None

            while not queue.empty():
                node = queue.get()

                if node:
                    deepest_rightmost_node = node

                    if str(node.value) == value:
                        node_to_delete = node

                    queue.put(node.left)
                    queue.put(node.right)

            if node_to_delete:
                if node_to_delete != deepest_rightmost_node:
                    node_to_delete.value = deepest_rightmost_node.value

                delete_node(deepest_rightmost_node)

    def get_height(self) -> int:
        def get_node_height(node: BinaryTreeNode) -> int:
            if not node:
                return 0

            left_height = get_node_height(node.left)
            right_height = get_node_height(node.right)

            return 1 + (left_height if left_height > right_height else right_height)

        return get_node_height(self.root)

    def get_inorder_traversal(self) -> list:
        """
        1. Traverse the left subtree
        2. Visit the root
        3. Traverse the right subtree

        Time complexity: O(n)
        Auxiliary space: O(1)
        """

        def traverse_inorder(node: BinaryTreeNode) -> None:
            if node:
                traverse_inorder(node.left)
                values.append(str(node))
                traverse_inorder(node.right)

        values = []
        traverse_inorder(self.root)
        return values

    def get_inorder_traversal_iterative_stack(self) -> list:
        """
        Iterative Inorder Tree Traversal using a stack.

        Time complexity: O(n)
        Auxiliary space: O(n)
        """
        values = []

        if self.root:
            node = self.root
            stack = deque()

            while True:
                if node:
                    stack.append(node)
                    node = node.left
                elif stack:
                    node = stack.pop()
                    values.append(node.value)
                    node = node.right
                else:
                    break

        return values

    def get_inorder_traversal_morris(self) -> list:
        """
        Inorder Tree Traversal using Morris Traversal.

        Time complexity: O(n)
        Auxiliary space: O(1)
        """
        values = []
        node = self.root

        while node:
            if node.left is None:
                values.append(node.value)
                node = node.right
            else:
                predecessor = node.left

                # Find the rightmost node in current left subtree or the node whose right child == current
                while predecessor.right and predecessor.right != node:
                    predecessor = predecessor.right

                if predecessor.right is None:
                    predecessor.right = node
                    node = node.left
                else:
                    predecessor.right = None
                    values.append(node.value)
                    node = node.right

        return values

    def get_preorder_traversal(self) -> list:
        """
        1. Visit the root
        2. Traverse the left subtree
        3. Traverse the right subtree

        Time complexity: O(n)
        Auxiliary space: O(1)
        """

        def traverse_preorder(node: BinaryTreeNode) -> None:
            if node:
                values.append(str(node))
                traverse_preorder(node.left)
                traverse_preorder(node.right)

        values = []
        traverse_preorder(self.root)
        return values

    def get_preorder_traversal_iterative_stack(self) -> list:
        """
        Iterative Preorder Tree Traversal using a stack.

        Time complexity: O(n)
        Auxiliary space: O(h) *the height of the tree
        """
        values = []

        if self.root:
            stack = deque()
            stack.append(self.root)

            while stack:
                node = stack.pop()
                values.append(node.value)

                if node.right:
                    stack.append(node.right)

                if node.left:
                    stack.append(node.left)

        return values

    def get_preorder_traversal_morris(self) -> list:
        """
        Preordedr Tree Traversal using Morris Traversal.

        Time complexity: O(n)
        Auxiliary space: O(1)
        """
        values = []
        node = self.root

        while node:
            if node.left is None:
                values.append(node.value)
                node = node.right
            else:
                predecessor = node.left

                # Find the rightmost node in current left subtree or the node whose right child == current
                while predecessor.right and predecessor.right is not node:
                    predecessor = predecessor.right

                if predecessor.right is node:
                    predecessor.right = None
                    node = node.right
                else:
                    predecessor.right = node
                    values.append(node.value)
                    node = node.left

        return values

    def get_postorder_traversal(self) -> list:
        """
        1. Traverse the left subtree
        2. Traverse the right subtree
        3. Visit the root

        Time complexity: O(n)
        Auxiliary space: O(1)
        """

        def traverse_postorder(node: BinaryTreeNode) -> None:
            if node:
                traverse_postorder(node.left)
                traverse_postorder(node.right)
                values.append(str(node))

        values = []
        traverse_postorder(self.root)
        return values

    def get_postorder_traversal_iterative(self) -> list:
        """
        Iterative Postorder Traversal (Using two stacks)

        Time complexity: O(n)
        Auxiliary space: O(1)
        """
        values = []

        if self.root:
            stack1 = deque()
            stack2 = deque()
            stack1.append(self.root)

            while stack1:
                node = stack1.pop()
                stack2.append(node)

                if node.left:
                    stack1.append(node.left)

                if node.right:
                    stack1.append(node.right)

            while stack2:
                node = stack2.pop()
                values.append(node.value)

        return values

    def get_level_order_traversal(self) -> list:
        """
        Level order tree traversal algorithm is a breadth-first tree traversal algorithm.
        It means that while traversing a tree, we first traverse all the elements at the current level before moving to the next level.

        Time complexity: O(n)
        Auxiliary space: O(1)
        """
        values = []

        if self.root:
            queue = Queue()
            queue.put(self.root)

            while not queue.empty():
                node = queue.get()

                if node:
                    values.append(str(node))
                    queue.put(node.left)
                    queue.put(node.right)

        return values

    def get_lot_spiral(self) -> list:
        """
        Level order traversal in spiral form.

        Time complexity: O(n^2)
        Auxiliary space: O(n)
        """

        def get_level(node: BinaryTreeNode, level: int, left_to_right: bool) -> None:
            if node:
                if level == 1:
                    values.append(node.value)
                else:
                    if left_to_right:
                        get_level(node.left, level - 1, left_to_right)
                        get_level(node.right, level - 1, left_to_right)
                    else:
                        get_level(node.right, level - 1, left_to_right)
                        get_level(node.left, level - 1, left_to_right)

        values = []

        if self.root:
            left_to_right = False

            for i in range(1, self.get_height() + 1):
                get_level(self.root, i, left_to_right)
                left_to_right = not left_to_right

        return values

    def get_level_order_traversal_spiral_stacks(self) -> list:
        """
        Level order traversal in spiral form using stacks.

        Time complexity: O(n)
        Auxiliary space: O(n)
        """
        values = []

        if self.root:
            stack1 = deque()
            stack2 = deque()
            stack1.append(self.root)

            while stack1 or stack2:
                while stack1:
                    node = stack1.pop()

                    if node:
                        values.append(node.value)
                        stack2.append(node.right)
                        stack2.append(node.left)

                while stack2:
                    node = stack2.pop()

                    if node:
                        values.append(node.value)
                        stack1.append(node.left)
                        stack1.append(node.right)

        return values

    def get_reverse_level_order_traversal(self) -> list:
        """
        Reverse level order traversal.

        Time complexity:  O(n^2)
        Auxiliary space: O(h)
        """

        def get_level(node: BinaryTreeNode, level: int) -> None:
            if node:
                if level == 0:
                    values.append(node.value)
                    return

                get_level(node.left, level - 1)
                get_level(node.right, level - 1)

        values = []

        for i in reversed(range(self.get_height())):
            get_level(self.root, i)

        return values

    def get_reverse_level_order_traversal_queue_stack(self) -> list:
        """
        Reverse level order traversal using queue and stack.

        Time complexity:  O(n)
        Auxiliary space: O(h)
        """
        stack = deque()

        if self.root:
            queue = deque()
            queue.append(self.root)

            while queue:
                node = queue.popleft()

                if node:
                    stack.appendleft(node.value)
                    queue.append(node.right)
                    queue.append(node.left)

        return list(stack)

    def get_reverse_level_order_traversal_dictionary(self) -> list:
        """
        Reverse level order traversal using a dictionary.

        Time complexity:  O(n)
        Auxiliary space: O(h)
        """

        def map_node(node: BinaryTreeNode, level: int) -> None:
            if node:
                if level not in map:
                    map[level] = []

                map[level].append(node.value)
                map_node(node.left, level + 1)
                map_node(node.right, level + 1)

        values = []

        if self.root:
            map = {}
            map_node(self.root, 1)

            for level in reversed(range(1, len(map) + 1)):
                values.extend(map[level])

        return values

    def get_diagonal_traversal(self) -> list:
        """
        Diagonal Traversal of binary tree

        Time complexity:  O(n*log(n))
        Auxiliary space: O(n)
        """

        def map_node(node: BinaryTreeNode, distance: int, map: dict) -> None:
            if node:
                # distance of current line from rightmost-topmost slope
                if distance in map:
                    map[distance].append(node.value)
                else:
                    map[distance] = [node.value]

                map_node(node.left, distance + 1, map)
                map_node(node.right, distance, map)  # Same distance

        values = []

        if self.root:
            map = {}
            map_node(self.root, 0, map)

            for k in map:
                values.extend(map[k])

        return values

    def get_diagonal_traversal_iterative(self) -> list:
        """
        Iterative Diagonal Traversal of binary tree (Using a queue)

        Time complexity:  O(n)
        Auxiliary space: O(n)
        """
        values = []

        if self.root:
            queue = deque()
            queue.append(self.root)

            while queue:
                node = queue.popleft()

                while node:
                    values.append(node.value)
                    queue.append(node.left)
                    node = node.right

        return values

    def get_boundary_traversal(self):
        """
        Get boundary nodes of the binary tree Anti-Clockwise starting from the root.

        Time complexity:  O(n)
        Auxiliary space: O(n)
        """

        def get_left_boundary(node: BinaryTreeNode) -> None:
            if node:
                if node.left:
                    values.append(node.value)
                    get_left_boundary(node.left)
                elif node.right:
                    values.append(node.value)
                    get_left_boundary(node.right)

        def get_leaves(node: BinaryTreeNode) -> None:
            if node:
                get_leaves(node.left)

                if not node.left and not node.right:
                    values.append(node.value)

                get_leaves(node.right)

        def get_right_boundary(node: BinaryTreeNode) -> None:
            if node:
                if node.right:
                    values.append(node.value)
                    get_right_boundary(node.right)
                elif node.left:
                    values.append(node.value)
                    get_right_boundary(node.left)

        values = []

        if self.root:
            values.append(self.root.value)

            get_left_boundary(self.root.left)
            get_leaves(self.root.left)
            get_leaves(self.root.right)
            get_right_boundary(self.root.right)

        return values
