# Licensing Information: You are free to use or extend this file for 
# educational purposes provided that (1) you retain this notice, and 
# (2) you provide clear attribution to the University of Melbourne, 
# including a link to https://cis.unimelb.edu.au.
#
# This file was created as part of teaching material for COMP90038
# January, 2020

def Warshall(A):
    n = len(A)
    R = []
    for i in range(n + 1):
        t = []
        for j in range(n):
            t.append([0] * n)
        R.append(t)
    R[0] = A
    for k in range(1, n + 1):
        for i in range(n):
            for j in range(n):
                R[k][i][j] = R[k - 1][i][j] or (R[k - 1][i][k - 1] and R[k - 1][k - 1][j])
    return R[n]

def test():
    A = [ [0, 1, 0, 0, 1, 0, 0],
          [0, 0, 1, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 1, 1],
          [0, 0, 1, 0, 0, 0, 0],
          [0, 1, 0, 0, 0, 1, 0],
          [0, 0, 0, 1, 0, 0, 1],
          [0, 0, 0, 1, 0, 0, 0] ]
    print(Warshall(A))
    
if __name__ == "__main__":
    test()
