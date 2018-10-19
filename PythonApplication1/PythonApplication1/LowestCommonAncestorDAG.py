from collections import OrderedDict
from copy import copy, deepcopy

class DAGValidationError(Exception):
    pass


class DAG(object):
    """ Directed acyclic graph implementation. """

    def __init__(self):
        """ Construct a new DAG with no nodes or edges. """
        self.graph = OrderedDict()

    def addNode(self, node_name):
        """ Add a node if it does not exist yet, or error out. """
        if node_name in self.graph:
            return ('node %s already exists' % node_name)
        self.graph[node_name] = set()

    def deleteNode(self, node_name):
        """ Deletes this node and all edges referencing it. """
        if node_name not in self.graph:
            return ('node %s does not exist' % node_name)
        self.graph.pop(node_name)

        for node, edges in self.graph:
            if node_name in edges:
                edges.remove(node_name)

    def addEdge(self, indNode, depNode):
        """ Add an edge (dependency) between the specified nodes. """
        if indNode not in self.graph or depNode not in self.graph:
            return ('one or more nodes do not exist in graph')
        self.graph[indNode].add(depNode)

    def deleteEdge(self, indNode, depNode):
        """ Delete an edge from the graph. """
        if depNode not in self.graph.get(indNode, []):
            return ('this edge does not exist in graph')
        self.graph[indNode].remove(depNode)

    def LCA(self, firstNode, secondNode):
        firstDict = self.getAllPredecessors(firstNode)
        secondDict = self.getAllPredecessors(secondNode)

        shortestDist = -1
        lca = None

        while firstDict != {}:
            (key, value) = firstDict.popitem()
            if key in secondDict and (shortestDist > value or shortestDist == -1):
                shortestDist = value
                lca = key

        return lca

    def getAllPredecessors(self, node):
        predecessors = {node: 0}
        queue = {}
        return self.getAllPredecessorsR(node, predecessors, queue, 0)

    def getAllPredecessorsR(self, node, predecessors, queue, offset):
        res = self.predecessors(node)
        for item in res:
            if item not in predecessors:
                predecessors[item] = offset + 1
                queue[item] = offset + 1
        if queue == {}:
            return predecessors
        else:
            (key, value) = queue.popitem()
            return self.getAllPredecessorsR(key, predecessors, queue, value)

    def predecessors(self, node, graph=None):
        """ Returns a list of all predecessors of the given node """
        if graph is None:
            graph = self.graph
        return [key for key in graph if node in graph[key]]

    def size(self):
        return len(self.graph)

familyTree = DAG()
familyTree.addNode(1)
familyTree.addNode(2)
familyTree.addNode(3)
familyTree.addNode(4)
familyTree.addNode(5)
familyTree.addNode(6)
familyTree.addNode(7)
familyTree.addEdge(1, 2)
familyTree.addEdge(1, 3)
familyTree.addEdge(1, 4)
familyTree.addEdge(1, 5)
familyTree.addEdge(6, 2)
familyTree.addEdge(2, 7)
print(familyTree.getAllPredecessors(7))
print(familyTree.LCA(5, 7))