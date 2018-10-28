import unittest
from LowestCOmmonAncestorDAG import DAG

class TestLCA(unittest.TestCase):

    def test_NormalInput(self):
        familyTree = DAG()
        for i in range(1, 10):
            familyTree.addNode(i)

        familyTree.addEdge(1, 2)
        familyTree.addEdge(1, 3)
        familyTree.addEdge(1, 4)
        familyTree.addEdge(1, 2)
        familyTree.addEdge(2, 5)
        familyTree.addEdge(3, 6)
        familyTree.addEdge(3, 7)
        familyTree.addEdge(5, 8)
        familyTree.addEdge(7, 9)
        familyTree.addEdge(8, 10)
        familyTree.addEdge(9, 10)

        self.assertEqual(familyTree.LCA(2, 7), 1, "LCA of 2 and 7 is 1")
        self.assertEqual(familyTree.LCA(8, 9), 1, "LCA of 8 and 9 is 1")
        self.assertEqual(familyTree.LCA(6, 7), 3, "LCA of 6 and 7 is 3")
  #     self.assertEqual(familyTree.LCA(3, 10), 3, "LCA of 3 and 10 is 3")

        #1
        #|___
        #2 3 4
        #| |_
        #5 6 7
        #| |
        #8 9
        #|___|
        #  |
        #  10

    #def test_SelfAncestor(self):
    #    root = Node(1)
    #    root.left = Node(2)
    #    root.right = Node(3)

    #    # 1
    #    # / \
    #    # 2 3

    #    self.assertEqual(findLCA(root, 2, 2), 2, "LCA of 2 and 2 is 2")


    #def test_NodeNotInTree(self):
    #    root = Node(1)
    #    root.left = Node(2)
    #    root.right = Node(3)

    #    # 1
    #    # / \
    #    # 2 3

    #    self.assertEqual(findLCA(root, 3, 6), -1, "6 is not in the tree, so
    #    returns -1")
    #    self.assertEqual(findLCA(root, 6, 2), -1, "6 is not in the tree, so
    #    returns -1")

    #def test_NullRoot(self):
    #    root = None

    #    # None

    #    self.assertEqual(findLCA(root, 2, 3), -1, "None root, so result is
    #    -1")
if __name__ == '__main__':
    unittest.main()
