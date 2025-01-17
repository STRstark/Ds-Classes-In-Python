class Node:
    def __init__(self, key):
        self.key = key
        self.parent = None
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
        
    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert(self.root, key)
    def _insert(self, current_node:Node, key):
        if key < current_node.key:
            if current_node.left is None:
                current_node.left = Node(key)
            else:
                self._insert(current_node.left, key)
        elif key > current_node.key:
            if current_node.right is None:
                current_node.right = Node(key)
            else:
                self._insert(current_node.right, key)
        else:
            print(f"Key {key} already exists in the BST.")

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, current_node:Node, key):
        if current_node is None:
            return False
        if current_node.key == key:
            return True
        elif key < current_node.key:
            return self._search(current_node.left, key)
        else:
            return self._search(current_node.right, key)

    def inorder_traversal(self):
        result = []
        self._inorder_traversal(self.root, result)
        return result

    def _inorder_traversal(self, current_node:Node, result:list):
        if current_node:
            self._inorder_traversal(current_node.left, result)
            result.append(current_node.key)
            self._inorder_traversal(current_node.right, result)
    
    def postorder_traversal(self):
        result = []
        self._postorder_traversal(self.root , result)
        return result
    def _postorder_traversal(self, current_node:Node, result:list):
        if current_node:
            self._postorder_traversal(current_node.left, result)
            self._postorder_traversal(current_node.right, result)
            result.append(current_node.key)
    
    def preorder_traversal(self):
        result = []
        self._preorder_traversal(self.root , result)
        return result
    def _preorder_traversal(self, current_node:Node, result:list):
        if current_node:
            result.append(current_node.key)
            self._preorder_traversal(current_node.left, result)
            self._preorder_traversal(current_node.right, result)
    
    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, current_node:Node, key) -> Node:
        if current_node is None:
            return current_node

        if key < current_node.key:
            current_node.left = self._delete(current_node.left, key)
        elif key > current_node.key:
            current_node.right = self._delete(current_node.right, key)
        else:
            
            if current_node.left is None:
                return current_node.right
            elif current_node.right is None:
                return current_node.left

            
            successor = self._min_value_node(current_node.right)
            current_node.key = successor.key
            current_node.right = self._delete(current_node.right, successor.key)

        return current_node

    def _min_value_node(self, node:Node) -> Node:
        current = node
        while current.left is not None:
            current = current.left
        return current
    