from random import randrange
import time
from datetime import datetime
import re

my_list = [ randrange(0, 15) for i in range(10) ]

max = len( my_list )
def Adj(V, G):
    adj = []

i = 0
while i < max:

    for i in range(0, V):
        adj.append([])
        for j in range(0, V):
            adj[i].append(0)

    j = 0
    while j < max-i-1:

    for i in range(0, len(G)):
         adj[G[i][0]][G[i][1]] = G[i][2]
        adj[G[i][1]][G[i][0]] = G[i][2]

        if my_list[ j ] > my_list[ j + 1 ]:
    return adj

            my_list[ j ], my_list[ j + 1] = my_list[ j + 1], my_list[ j ]
        j+=1
    i += 1

print( my_list )
def prim(V, G):

    adj = Adj(V, G)


    vertex = 0


    MST = []
    edges = []
    visited = []
    minEdge = [None, None, float('inf')]


    while len(MST) != V - 1:


        visited.append(vertex)


        for r in range(0, V):
            if adj[vertex][r] != 0:
                edges.append([vertex, r, adj[vertex][r]])

        for e in range(0, len(edges)):
            if edges[e][2] < minEdge[2] and edges[e][1] not in visited:
                minEdge = edges[e]

        edges.remove(minEdge)


        MST.append(minEdge)

        vertex = minEdge[1]
        minEdge = [None, None, float('inf')]

    return MST


graph = [
    [0, 1, 6],
    [0, 3, 2],
    [0, 4, 7],
    [1, 2, 3],
    [1, 5, 6],
    [2, 5, 10],
    [2, 7, 6],
    [3, 5, 7],
    [3, 6, 10],
    [4, 6, 1],
    [4, 7, 1],
    [5, 7, 4],
    [6, 7, 7]
]
print("MST of Prim's algorithm: ")
print(prim(8, graph))


class Graph:
    def graf(a, b):
        a.V = b
        a.graph = []

    def add(a, u, v, w):
        a.graph.append([u, v, w])

    def find(a, parent, i):
        if parent[i] == i:
            return i
        return a.find(parent, parent[i])

    def union(a, parent, rank, x, y):
        xRoot = a.find(parent, x)
        yRoot = a.find(parent, y)
        if rank[xRoot] < rank[yRoot]:
            parent[xRoot] = yRoot
        elif rank[xRoot] > rank[yRoot]:
            parent[yRoot] = xRoot
        else:
            parent[yRoot] = xRoot
            rank[xRoot] += 1

    def kruskal(a):
        result = []
        i, e = 0, 0
        a.graph = sorted(a.graph, key=lambda item: item[2])
        parent = []
        rank = []
        for node in range(a.V):
            parent.append(node)
            rank.append(0)
        while e < a.V - 1:
            u, v, w = a.graph[i]
            i = i + 1
            x = a.find(parent, u)
            y = a.find(parent, v)
            if x != y:
                e = e + 1
                result.append([u, v, w])
                a.union(parent, rank, x, y)
        print("\ Kruskal ")
        print("Vertex A   Vertex B  Weight")
        for u, v, weight in result:
            print("%5d %9d %10d" % (u, v, weight))


g = Graph(8)
g.add(0, 1, 6)
g.add(0, 3, 2)
g.add(0, 4, 7)
g.add(1, 2, 3)
g.add(1, 5, 6)
g.add(2, 5, 10)
g.add(2, 7, 6)
g.add(3, 5, 7)
g.add(3, 6, 10)
g.add(4, 6, 1)
g.add(4, 7, 1)
g.add(5, 7, 4)
g.add(6, 7, 7)

g.kruskal()

from datetime import datetime
start_time = datetime.now()

end_time = datetime.now()
print('Duration: {}'.format(end_time - start_time))
