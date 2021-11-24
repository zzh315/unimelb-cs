# Licensing Information: You are free to use or extend this file for 
# educational purposes provided that (1) you retain this notice, and 
# (2) you provide clear attribution to the University of Melbourne, 
# including a link to https://cis.unimelb.edu.au.
#
# This file was created as part of teaching material for COMP90038
# January, 2020

from L21_PriorityQueue import PriorityQueue

def Prim(G):
    inf = float("+inf")
    cost = [inf] * len(G)
    prev = [None] * len(G)
    v0 = 0
    cost[v0] = 0
    Q = PriorityQueue()
    for i in range(len(cost)):
        Q.put(i, cost[i])
    while not Q.empty():
        u, c = Q.get()
        for w in range(len(G)):
            if G[u][w] and w in Q and G[u][w] < cost[w]:
                cost[w] = G[u][w]
                prev[w] = u
                Q.update(w, cost[w])
    return prev

def test():
    G = [ [0, 2, 4, 1, 0, 0, 0],
          [2, 0, 0, 3, 9, 0, 0],
          [4, 0, 0, 2, 0, 5, 0],
          [1, 3, 2, 0, 7, 8, 4],
          [0, 9, 0, 7, 0, 0, 6],
          [0, 0, 5, 8, 0, 0, 1],
          [0, 0, 0, 4, 6, 1, 0] ]
    print(Prim(G))
    
if __name__ == "__main__":
    test()
