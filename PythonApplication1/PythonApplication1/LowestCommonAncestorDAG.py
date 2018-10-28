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
            return ('Node %s already exists' % node_name)
        self.graph[node_name] = set()

    def addEdge(self, indNode, depNode):
        """ Add an edge (dependency) between the specified nodes. """
        if indNode not in self.graph or depNode not in self.graph:
            return ('One or more nodes do not exist in graph')
        if depNode in self.graph[indNode]:
            return ('Edge from %s to %s already exists in graph' % (indNode, depNode))
        self.graph[indNode].add(depNode)

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