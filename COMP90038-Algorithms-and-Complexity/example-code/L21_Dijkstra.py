# Licensing Information: You are free to use or extend this file for 
# educational purposes provided that (1) you retain this notice, and 
# (2) you provide clear attribution to the University of Melbourne, 
# including a link to https://cis.unimelb.edu.au.
#
# This file was created as part of teaching material for COMP90038
# January, 2020

from L21_PriorityQueue import PriorityQueue

def Dijkstra(G, v0):
    inf = float("+inf")
    dist = [inf] * len(G)
    prev = [None] * len(G)
    dist[v0] = 0
    Q = PriorityQueue()
    for i in range(len(dist)):
        Q.put(i, dist[i])
    while not Q.empty():
        u, d = Q.get()
        for w in range(len(G)):
            if G[u][w] and w in Q and dist[u] + G[u][w] < dist[w]:
                dist[w] = dist[u] + G[u][w]
                prev[w] = u
                Q.update(w, dist[w])
    return dist

def test():
    G = [ [0, 2, 4, 1, 0, 0, 0],
          [2, 0, 0, 3, 9, 0, 0],
          [4, 0, 0, 2, 0, 5, 0],
          [1, 3, 2, 0, 7, 8, 4],
          [0, 9, 0, 7, 0, 0, 6],
          [0, 0, 5, 8, 0, 0, 1],
          [0, 0, 0, 4, 6, 1, 0] ]
    print(Dijkstra(G, 4))
    
if __name__ == "__main__":
    test()
