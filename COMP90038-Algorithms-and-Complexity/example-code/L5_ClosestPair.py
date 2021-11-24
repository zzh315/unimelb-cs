# Licensing Information: You are free to use or extend this file for 
# educational purposes provided that (1) you retain this notice, and 
# (2) you provide clear attribution to the University of Melbourne, 
# including a link to https://cis.unimelb.edu.au
#
# This file was created as part of teaching material for COMP90038
# March, 2020

def ClosestPair(nodes):
    min = float("inf")
    n = len(nodes)
    for i in range(0, n - 1):
        xi, yi = nodes[i]
        for j in range(i + 1, n):
            xj, yj = nodes[j]
            d = ((xi - xj) ** 2 + (yi - yj) ** 2) ** 0.5
            if d < min:
                min = d
                pi = i
                pj = j
    return pi, pj

def test():
    N = [(1, 3), (5, 8), (-2, 7), (-9, 0), (-4, -6)]
    print(ClosestPair(N))

if __name__ == "__main__":
    test()
