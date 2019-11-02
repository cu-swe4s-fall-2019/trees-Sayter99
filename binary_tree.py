class Node:
    # basic data structure of binary tree
    def __init__(self, key, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
        self.key = key


class BinaryTree:
    # binary tree with insert and search methods
    def __init__(self):
        self.root = None

    def insert(self, key, value=None):
        # recursively find a position to insert
        if (self.root == None):
            self.root = Node(key, value)
        else:
            self.add(key, value, self.root)

    def add(self, key, value, node):
        if (key < node.key):
            if (not node.left is None):
                self.add(key, value, node.left)
            else:
                node.left = Node(key, value)
        else:
            if (not node.right is None):
                self.add(key, value, node.right)
            else:
                node.right = Node(key, value)

    def search(self, key):
        # recursively find the specific key and return the node
        if (self.root is None):
            return None
        else:
            return self.find(key, self.root)

    def find(self, key, node):
        if (key == node.key):
            return node
        elif (node.right is None and node.left is None):
            return None
        elif (key < node.key and (not node.left is None)):
            return self.find(key, node.left)
        elif (key > node.key and (not node.right is None)):
            return self.find(key, node.right)
