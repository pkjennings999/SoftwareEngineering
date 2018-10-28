import unittest
from LowestCommonAncestorDAG import DAG

class TestLCA(unittest.TestCase):

    def test_NormalInput(self):
        familyTree = DAG()
        for i in range(0, 10):
            familyTree.addNode(i + 1)

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
        self.assertEqual(familyTree.LCA(3, 10), 3, "LCA of 3 and 10 is 3")

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

    def test_SelfAncestor(self):
        familyTree = DAG()
        for i in range(0, 3):
            familyTree.addNode(i + 1)
        familyTree.addEdge(1, 2)
        familyTree.addEdge(1, 3)

        self.assertEqual(familyTree.LCA(2, 2), 2, "LCA of 2 and 2 is 2")


    def test_NodeNotInGraph(self):
        familyTree = DAG()
        for i in range(0, 3):
            familyTree.addNode(i + 1)
        familyTree.addEdge(1, 2)
        familyTree.addEdge(1, 3)

        self.assertEqual(familyTree.LCA(3, 6), None, "6 is not in the tree, returns None")
        self.assertEqual(familyTree.LCA(6, 2), None, "6 is not in the tree, returns -1")

        self.assertEqual(familyTree.addEdge(1, 7), "One or more nodes do not exist in graph", "Node 7 does not exist in the graph")

    def test_AlreadyExists(self):
        familyTree = DAG()
        for i in range(0, 3):
            familyTree.addNode(i + 1)
        familyTree.addEdge(1, 2)
        familyTree.addEdge(1, 3)

        # None

        self.assertEqual(familyTree.addNode(1), "Node 1 already exists", "Node 1 already exits in the graph")
        self.assertEqual(familyTree.addEdge(1, 2), "Edge from 1 to 2 already exists in graph", "Edge from 1 to 2 already exists in graph")

if __name__ == '__main__':
    unittest.main()