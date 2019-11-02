import binary_tree
import unittest
import avl
import os


class TestBinaryTree(unittest.TestCase):
    def test_insert(self):
        tree = binary_tree.BinaryTree()
        tree.insert('b', 'b_val')
        self.assertEqual(tree.root.value, 'b_val')
        tree.insert('c', 'c_val')
        self.assertEqual(tree.root.right.key, 'c')
        tree.insert('a', 'a_val')
        self.assertEqual(tree.root.left.value, 'a_val')

    def test_search(self):
        tree = binary_tree.BinaryTree()
        tree.insert('b', 'b_val')
        tree.insert('c', 'c_val')
        tree.insert('a', 'a_val')
        search_a = tree.search('a')
        self.assertEqual(search_a.value, 'a_val')
        search_a = tree.search('b')
        self.assertEqual(search_a.value, 'b_val')
        search_a = tree.search('c')
        self.assertEqual(search_a.value, 'c_val')

    def test_avl_insert(self):
        tree = avl.AVL()
        tree.insert('b', 'b_val')
        self.assertEqual(tree.root.value, 'b_val')
        tree.insert('c', 'c_val')
        self.assertEqual(tree.root.right.key, 'c')
        tree.insert('a', 'a_val')
        self.assertEqual(tree.root.left.value, 'a_val')

    def test_avl_search(self):
        tree = avl.AVL()
        tree.insert('b', 'b_val')
        tree.insert('c', 'c_val')
        tree.insert('a', 'a_val')
        search_a = tree.search('a')
        self.assertEqual(search_a.value, 'a_val')
        search_a = tree.search('b')
        self.assertEqual(search_a.value, 'b_val')
        search_a = tree.search('c')
        self.assertEqual(search_a.value, 'c_val')


if __name__ == '__main__':
    unittest.main()
