class Graph:
    def __init__(self):
        self.numberOfNodes = 0
        self.adjacentList = {}

    def addNodes(self, node):
        self.adjacentList[node] = []
        self.numberOfNodes += 1

    def addEdge(self, node1, node2):
        self.adjacentList[node1].append(node2)
        self.adjacentList[node2].append(node1)

    def showConnection(self):
        for node in self.adjacentList:
            print(node, end="--->")
            for adjNode in self.adjacentList[node]:
                print(adjNode, end=" ")
            print()


myGraph = Graph()
myGraph.addNodes('0')
myGraph.addNodes('1')
myGraph.addNodes('2')
myGraph.addNodes('3')
myGraph.addNodes('4')
myGraph.addNodes('5')
myGraph.addNodes('6')
myGraph.addEdge('3', '1')
myGraph.addEdge('3', '4')
myGraph.addEdge('4', '2')
myGraph.addEdge('4', '5')
myGraph.addEdge('1', '2')
myGraph.addEdge('1', '0')
myGraph.addEdge('0', '2')
myGraph.addEdge('6', '5')
myGraph.showConnection()
