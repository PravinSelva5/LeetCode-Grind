from collections import defaultdict

from numpy import matrix

# Directed Graph using an adjacency LIST
class DirectedGraphList:
    def __init__(self):
        self.graph = defaultdict(list)

    def insertEdge(self, v1, v2):
        self.graph[v1].append(v2)

    def printGraph(self):
        for node in self.graph:
            for v in self.graph[node]:
                print(node, "=>", v)


class DirectGraphMatrix:
    def __init__(self, numberOfNodes):
        self.numberOfNodes = numberOfNodes + 1
        self.graph = [
            [0 for x in range(numberOfNodes + 1)] for y in range(numberOfNodes)
        ]  # +1 to include all nodes because lists count from 0

    def withInBounds(self, v1, v2):
        # Using this method, to make sure the elements used to insert an edge follows the matrix length restriction
        return (v1 >= 0 and v1 < self.numberOfNodes) and (v2 < self.numberOfNodes)

    def insertEdgeMatrix(self, v1, v2):
        if self.withInBounds(v1, v2):
            self.graph[v1][v2] = 1

    def printMatrixGraph(self):
        for i in range(self.numberOfNodes):
            for j in range(len(self.graph[i])):
                if self.graph[i][j]:
                    print(i, "->", j)


g = DirectedGraphList()
g.insertEdge(1, 5)
g.insertEdge(5, 2)
g.insertEdge(2, 7)
g.insertEdge(7, 1)

print("Directed Graph using adjacent lists")
print("------------------------------------")
g.printGraph()

print(" ")
print("Directed Graph using adjacent matrix")
print("------------------------------------")
matrixg = DirectGraphMatrix(5)

matrixg.insertEdgeMatrix(1, 2)
matrixg.insertEdgeMatrix(2, 3)
matrixg.insertEdgeMatrix(4, 5)

matrixg.printMatrixGraph()
