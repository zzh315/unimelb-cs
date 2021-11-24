# Licensing Information: You are free to use or extend this file for 
# educational purposes provided that (1) you retain this notice, and 
# (2) you provide clear attribution to the University of Melbourne, 
# including a link to https://cis.unimelb.edu.au.
#
# This file was created as part of teaching material for COMP90038
# January, 2020

from queue import Queue

def BFS(G):
    mark = [0] * len(G)
    count = 0
    Q = Queue()
    for v in range(len(G)):
        if mark[v] == 0:
            count = count + 1
            mark[v] = count
            Q.put(v)
            while not Q.empty():
                u = Q.get()
                for w in range(len(G)):
                    if G[u][w] != 0:
                        if mark[w] == 0:
                            count = count + 1
                            mark[w] = count
                            Q.put(w)

def test():
    G = [[0, 1, 0, 1],
         [1, 0, 0, 1],
         [0, 0, 0, 1],
         [1, 1, 1, 0]]
    BFS(G)

if __name__ == "__main__":
    test()
