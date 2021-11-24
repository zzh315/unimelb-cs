# Licensing Information: You are free to use or extend this file for 
# educational purposes provided that (1) you retain this notice, and 
# (2) you provide clear attribution to the University of Melbourne, 
# including a link to https://cis.unimelb.edu.au.
#
# This file was created as part of teaching material for COMP90038
# January, 2020

def MatrixMult(A, B):
    n = len(A)
    C = [[0] * n for i in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] = C[i][j] + A[i][k] * B[k][j]
    return C

def test():
    A = [[1,2,3], [4,5,6], [7,8,9]]
    B = [[3,6,9], [1,7,4], [5,2,8]]
    print(MatrixMult(A, B))

if __name__ == "__main__":
    test()
