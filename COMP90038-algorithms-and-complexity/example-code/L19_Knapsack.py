# Licensing Information: You are free to use or extend this file for 
# educational purposes provided that (1) you retain this notice, and 
# (2) you provide clear attribution to the University of Melbourne, 
# including a link to https://cis.unimelb.edu.au.
#
# This file was created as part of teaching material for COMP90038
# January, 2020

def Knapsack(W, v, w):
    n = len(v)
    K = []
    for i in range(n + 1):
        K.append([0] * (W + 1))
    for i in range(1, n + 1):
        for j in range(1, W + 1):
            if j < w[i - 1]:
                K[i][j] = K[i - 1][j]
            else:
                K[i][j] = max(K[i - 1][j], K[i - 1][j - w[i - 1]] + v[i - 1])
    return K[-1][-1]

def test():
    W = 8
    v = [42, 12, 40, 25]
    w = [7, 3, 4, 5]
    print(Knapsack(W, v, w))
    
if __name__ == "__main__":
    test()
