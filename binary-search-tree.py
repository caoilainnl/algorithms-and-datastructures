class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert_recursive(self.root, key)

    def _insert_recursive(self, node, key):
        if key < node.key:
            if node.left is None:
                node.left = Node(key)
            else:
                self._insert_recursive(node.left, key)
        elif key > node.key:
            if node.right is None:
                node.right = Node(key)
            else:
                self._insert_recursive(node.right, key)

    def inorder_traversal(self):
        return self._inorder_recursive(self.root, [])

    def _inorder_recursive(self, node, result):
        if node:
            self._inorder_recursive(node.left, result)
            result.append(node.key)
            self._inorder_recursive(node.right, result)
        return result

    def search(self, key):
        return self._search_recursive(self.root, key)

    def _search_recursive(self, node, key):
        if node is None or node.key == key:
            return node
        if key < node.key:
            return self._search_recursive(node.left, key)
        return self._search_recursive(node.right, key)


def main():
    # Initialize the BST
    bst = BinarySearchTree()

    # Test case 1: Insert and traverse
    print("Test Case 1: Insert and Inorder Traversal")
    keys = [50, 30, 70, 20, 40, 60, 80]
    for key in keys:
        bst.insert(key)
    expected_traversal = [20, 30, 40, 50, 60, 70, 80]
    result_traversal = bst.inorder_traversal()
    print("Expected Traversal:", expected_traversal)
    print("Result Traversal:  ", result_traversal)
    assert result_traversal == expected_traversal, "Inorder traversal does not match expected output."

    # Test case 2: Search for existing keys
    print("\nTest Case 2: Search for Existing Keys")
    search_keys = [20, 40, 50, 80]
    for key in search_keys:
        assert bst.search(key) is not None, f"Key {key} should be found in the BST."
        print(f"Key {key} found successfully.")

    # Test case 3: Search for non-existing keys
    print("\nTest Case 3: Search for Non-Existing Keys")
    non_existing_keys = [10, 90, 35, 100]
    for key in non_existing_keys:
        assert bst.search(key) is None, f"Key {key} should not be found in the BST."
        print(f"Key {key} not found as expected.")

    # Test case 4: Insert duplicate keys
    print("\nTest Case 4: Insert Duplicate Keys")
    bst.insert(50)  # Duplicate key
    bst.insert(30)  # Duplicate key
    result_traversal_after_duplicates = bst.inorder_traversal()
    print("Traversal After Attempting Duplicates:", result_traversal_after_duplicates)
    assert result_traversal_after_duplicates == expected_traversal, "Duplicates should not affect the BST structure."

    print("\nAll test cases passed!")


main()