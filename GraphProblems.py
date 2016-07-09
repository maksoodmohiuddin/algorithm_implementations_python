class Node():
    def __init__(self, node_name, visited=False, vertices=[]):
        self.name = node_name
        self.visited = False
        self.vertices = vertices

    def addEdge(self, vertex):
         self.vertices.append(vertex)

class Graph():
    def __init__(self, graph_name):
        # list of nodes
        self.name = graph_name
        self.nodes = []

    def addNode(self, node):
        self.nodes.append(node)


nodeA = Node("A")
nodeB = Node("B")
nodeC = Node("C")

nodeA.addEdge(nodeB)
nodeA.addEdge(nodeC)

graph = Graph("Maksood")
graph.addNode(nodeA)
graph.addNode(nodeB)
graph.addNode(nodeC)

for node in graph.nodes:
    print node.name

for node in nodeA.vertices:
     print node.name




