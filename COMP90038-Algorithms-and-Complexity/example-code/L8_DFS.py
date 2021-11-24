# Licensing Information: You are free to use or extend this file for 
# educational purposes provided that (1) you retain this notice, and 
# (2) you provide clear attribution to the University of Melbourne, 
# including a link to https://cis.unimelb.edu.au.
#
# This file was created as part of teaching material for COMP90038
# January, 2020

def DFS(G):
    global count
    mark = [0] * len(G)
    count = 0
    for v in range(len(G)):
        if mark[v] == 0:
            DFSExplore(v, G, mark)
    #print(mark)

def DFSExplore(v, G, mark):
    global count
    count = count + 1
    mark[v] = count
    for w in range(len(G)):
        if G[v][w] != 0:
            if mark[w] == 0:
                DFSExplore(w, G, mark)

def test():
    G = [[0, 1, 0, 1],
         [1, 0, 0, 1],
         [0, 0, 0, 1],
         [1, 1, 1, 0]]
    DFS(G)

if __name__ == "__main__":
    test()
