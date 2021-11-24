# Licensing Information: You are free to use or extend this file for 
# educational purposes provided that (1) you retain this notice, and 
# (2) you provide clear attribution to the University of Melbourne, 
# including a link to https://cis.unimelb.edu.au.
#
# This file was created as part of teaching material for COMP90038
# January, 2020

def Floyd(W):
    n = len(W)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                W[i][j] = min(W[i][j], W[i][k] + W[k][j])
    return W

def test():
    n = float("+inf")
    W = [ [0, 1, 1, 1, n],
          [1, 0, n, 1, 1],
          [1, n, 0, 1, n],
          [1, 1, 1, 0, 1],
          [n, 1, n, 1, 0] ]
    print(Floyd(W))
    
if __name__ == "__main__":
    test()
