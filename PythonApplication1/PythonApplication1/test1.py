import unittest
from LowestCommonAncestorBinaryTree import findLCA
from LowestCommonAncestorBinaryTree import Node

class TestFindLCA(unittest.TestCase):

    def test_A(self):
        root = Node(1)
        root.left = Node(2)
        root.right = Node(3)
        root.left.left = Node(4)
        root.left.right = Node(5)
        root.right.left = Node(6)
        root.right.right = Node(7)

        self.assertEqual(findLCA(root, 4, 5), 2, "LCA of 4 and 5 is 2")
        self.assertEqual(findLCA(root, 4, 6), 1, "LCA of 4 and 6 is 1")
        self.assertEqual(findLCA(root, 3, 4), 1, "LCA of 3 and 4 is 1")
        self.assertEqual(findLCA(root, 2, 4), 2, "LCA of 2 and 4 is 2")

if __name__ == '__main__':
    unittest.main()