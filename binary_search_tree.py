class TreeNode:
    def __init__(self, value: int):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value: int) -> None:
        if self.root is None:
            self.root = TreeNode(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, current: TreeNode, value: int) -> None:
        if value < current.value:
            if current.left is None:
                current.left = TreeNode(value)
            else:
                self._insert_recursive(current.left, value)
        elif value > current.value:
            if current.right is None:
                current.right = TreeNode(value)
            else:
                self._insert_recursive(current.right, value)

    def search(self, value: int) -> bool:
        return self._search_recursive(self.root, value)

    def _search_recursive(self, current: TreeNode | None, value: int) -> bool:
        if current is None:
            return False
        if value == current.value:
            return True
        if value < current.value:
            return self._search_recursive(current.left, value)
        return self._search_recursive(current.right, value)

    def inorder_traversal(self) -> list[int]:
        result: list[int] = []
        self._inorder_recursive(self.root, result)
        return result

    def _inorder_recursive(self, current: TreeNode | None, result: list[int]) -> None:
        if current is not None:
            self._inorder_recursive(current.left, result)
            result.append(current.value)
            self._inorder_recursive(current.right, result)


if __name__ == "__main__":
    bst = BinarySearchTree()
    for num in [50, 30, 70, 20, 40, 60, 80]:
        bst.insert(num)

    print("In-order traversal (sorted):", bst.inorder_traversal())
    print("Search 40:", bst.search(40))
    print("Search 99:", bst.search(99))
