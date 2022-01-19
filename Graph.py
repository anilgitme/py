class Graph:
    def __init__(self):
        self.graph = {}
    def __repr__(self):
        return str(self.graph)
    def addNode(self, value):
        if value not in self.graph:
            self.graph[value] = set()
    
    def removeNode(self, value):
        if value in self.graph:
            self.graph.pop(value)
            for vals in self.graph:
                if value in self.graph[vals]:
                    self.graph[vals].remove(value)
    
    def addEdge(self, fromNode, toNode):
        self.graph[fromNode].add(toNode)
    
    def removeEdge(self, fromNode, toNode):
        self.graph[fromNode].remove(toNode)
        
    def edgeExists(self, fromNode, toNode):
        return toNode in self.graph[fromNode]
        
G = Graph()
G.addNode(0)
G.addNode(1)
G.addNode(2)
G.addNode(3)
G.addNode(4)
print(G)
G.removeNode(0)
G.addEdge(1,2)
G.addEdge(1,3)
G.addEdge(2,4)
G.addEdge(3,4)
G.addEdge(4,1)
G.removeNode(4)
print(G)
print(G.edgeExists(1,2))
print(G.edgeExists(2,1))
G.removeEdge(1,3)
print(G)