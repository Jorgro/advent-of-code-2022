
from collections import defaultdict
import sys

m = []

class Graph():

    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]

    def printNode(self, node):
        print(node)
        print(self.dist[node])

    def getAllNodes(self):
        distances = []
        for node in range(self.V):
            distances.append((node, self.dist[node]))

        return distances
    def getNodeDist(self, node):
        return self.dist[node]

    def printSolution(self, dist):
        print("Vertex \tDistance from Source")
        for node in range(self.V):
            print(node, "\t", dist[node])

    # A utility function to find the vertex with
    # minimum distance value, from the set of vertices
    # not yet included in shortest path tree
    def minDistance(self, dist, sptSet):

        # Initialize minimum distance for next node
        min = sys.maxsize

        min_index = None

        # Search not nearest vertex not in the
        # shortest path tree
        for u in range(self.V):
            if dist[u] < min and sptSet[u] == False:
                min = dist[u]
                min_index = u

        return min_index

    # Function that implements Dijkstra's single source
    # shortest path algorithm for a graph represented
    # using adjacency matrix representation
    def dijkstra(self, src):

        self.dist = [sys.maxsize] * self.V
        self.dist[src] = 0
        sptSet = [False] * self.V

        for cout in range(self.V):

            # Pick the minimum distance vertex from
            # the set of vertices not yet processed.
            # x is always equal to src in first iteration
            x = self.minDistance(self.dist, sptSet)
            if x == None:
                #self.printSolution(dist)
                return

            # Put the minimum distance vertex in the
            # shortest path tree
            sptSet[x] = True

            # Update dist value of the adjacent vertices
            # of the picked vertex only if the current
            # distance is greater than new distance and
            # the vertex in not in the shortest path tree
            for y in range(self.V):
                if self.graph[x][y] > 0 and sptSet[y] == False and \
                        self.dist[y] > self.dist[x] + self.graph[x][y]:
                    self.dist[y] = self.dist[x] + self.graph[x][y]

        self.printSolution(self.dist)

def index_2d(myList, v):
    for i, x in enumerate(myList):
        if v in x:
            return (i, x.index(v))


with open("day12/test.txt", "r") as f:

    for line in f:
        m.append(list(line.strip()))

#print(m)
e_ind = index_2d(m, "E")
s_ind = index_2d(m, "S")
m[e_ind[0]][e_ind[1]] = "z"
m[s_ind[0]][s_ind[1]] = "a"
#m[0][0] = "a"

g = Graph(len(m)*len(m[0]))
alph ='abcdefghijklmnopqrstuvwxyz'
for i in range(len(m)):
    for j in range(len(m[0])):
        if i+1 < len(m):
            if alph.index(m[i+1][j]) - alph.index(m[i][j]) <= 1:
                g.graph[i*len(m[0])+j][(i+1)*len(m[0]) + j] = 1
        if i-1 >= 0:
            if alph.index(m[i-1][j]) - alph.index(m[i][j]) <= 1:
                 g.graph[i*len(m[0])+j][(i-1)*len(m[0])+j] = 1
        if j+1 < len(m[0]):
            if alph.index(m[i][j+1]) - alph.index(m[i][j]) <= 1:
                g.graph[i*len(m[0])+j][i*len(m[0])+ j + 1] = 1
        if j-1 >= 0:
            if  alph.index(m[i][j-1]) - alph.index(m[i][j]) <= 1:
                 g.graph[i*len(m[0])+j][i*len(m[0])+j - 1] = 1


print(g.graph[21][20])

g.dijkstra(e_ind[0]*len(m[0])+e_ind[1])
distances = g.getAllNodes()

flatten_list = [j for sub in m for j in sub]
distances = sorted(
    distances,
    key=lambda x: x[1],
    reverse=True
)
print(distances)
for n in distances:
    if flatten_list[n[0]] == 'a':
        print(n[1])
        break;

#g.printNode(e_ind[0]*len(m[0])+e_ind[1])
#g.printNode(14)
