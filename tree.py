class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root_value):
        self.root = TreeNode(root_value)

    def insert(self, value):
        self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = TreeNode(value)
            else:
                self._insert_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = TreeNode(value)
            else:
                self._insert_recursive(node.right, value)

    # def search(self, value):
    #     return self._search_recursive(self.root, value)

    # def _search_recursive(self, node, value):
    #     if node is None:
    #         return False
    #     if node.value == value:
    #         return True
    #     elif value < node.value:
    #         return self._search_recursive(node.left, value)
    #     else:
    #         return self._search_recursive(node.right, value)

    # def inorder_traversal(self):
    #     result = []
    #     self._inorder_traversal_recursive(self.root, result)
    #     return result

    # def _inorder_traversal_recursive(self, node, result):
    #     if node:
    #         self._inorder_traversal_recursive(node.left, result)
    #         result.append(node.value)
    #         self._inorder_traversal_recursive(node.right, result)

# Example usage:
tree = BinaryTree(5)
tree.insert(3)
tree.insert(8)
tree.insert(1)
tree.insert(4)
tree.insert(7)
tree.insert(9)

# print(tree.search(7))  # Output: True
# print(tree.search(2))  # Output: False

# inorder_result = tree.inorder_traversal()
# print(inorder_result)  # Output: [1, 3, 4, 5, 7, 8, 9]
