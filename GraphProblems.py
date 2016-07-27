class Node():
    def __init__(self, node_name, visited=False, vertices=[]):
        self.name = node_name
        self.visited = False
        self.vertices = vertices

    def addEdge(self, vertex):
         self.vertices = self.vertices + [vertex]
         #self.vertices.append(vertex)

class Graph():
    def __init__(self, graph_name):
        # list of nodes
        self.name = graph_name
        self.nodes = []

    def addNode(self, node):
        self.nodes.append(node)


node0 = Node("0")
node1 = Node("1")
node2 = Node("2")
node3 = Node("3")
node4 = Node("4")
node5 = Node("5")

node0.addEdge(node1)
node0.addEdge(node4)
node0.addEdge(node5)

node1.addEdge(node3)
node1.addEdge(node4)

node2.addEdge(node1)

node3.addEdge(node2)
node3.addEdge(node4)

graph = Graph("Graph")
graph.addNode(node0)
graph.addNode(node1)
graph.addNode(node2)
graph.addNode(node3)
graph.addNode(node4)
graph.addNode(node5)

#print graph.name
#for node in graph.nodes:
#    print node.name

#print "Node:" + node0.name
#for node in node0.vertices:
#     print node.name

#print "Node:" + node1.name
#for node in node1.vertices:
#     print node.name

#print "Node:" + node2.name
#for node in node2.vertices:
#     print node.name

#print "Node:" + node3.name
#for node in node3.vertices:
#     print node.name


def depth_first_search():
    for node in graph.nodes:
        print node.name
        for child in node.vertices:
            print child.name

depth_first_search()