from collections import defaultdict


class UndirectedGraphList:
    def __init__(self):
        self.graph = defaultdict(list)

    def insertEdge(self, v1, v2):
        self.graph[v1].append(v2)
        self.graph[v2].append(v1)

    def printGraph(self):
        for node in self.graph:
            for v in self.graph[node]:
                print(node, "=>", v)


class UndirectedGraphMatrix:
    def __init__(self, numberOfNodes):
        self.numberOfNodes = numberOfNodes + 1
        self.graph = [
            [0 for x in range(numberOfNodes + 1)] for y in range(numberOfNodes + 1)
        ]

    def withInBounds(self, v1, v2):
        return (v1 >= 0 and v1 < self.numberOfNodes) and (
            v2 >= 0 and v2 < self.numberOfNodes
        )

    def insertEdges(self, v1, v2):
        if self.withInBounds(v1, v2):
            self.graph[v1][v2] = 1
            self.graph[v2][v1] = 1

    def printGraph(self):
        for i in range(self.numberOfNodes):
            for j in range(len(self.graph[i])):
                if self.graph[i][j]:
                    print(i, "->", j)


g = UndirectedGraphList()

print("Undirected Graph with Adjacent Lists")
print("------------------------------------")

g.insertEdge(1, 5)
g.insertEdge(1, 100)
g.insertEdge(5, 2)
g.insertEdge(2, 7)
g.insertEdge(7, 1)

g.printGraph()

gMatrix = UndirectedGraphMatrix(5)
print("")
print("Undirected Graph with Adjacent Matrix")
print("------------------------------------")

gMatrix.insertEdges(1, 4)
gMatrix.insertEdges(2, 3)
gMatrix.insertEdges(4, 5)

gMatrix.printGraph()
