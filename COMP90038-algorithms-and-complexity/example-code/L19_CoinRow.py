# Licensing Information: You are free to use or extend this file for 
# educational purposes provided that (1) you retain this notice, and 
# (2) you provide clear attribution to the University of Melbourne, 
# including a link to https://cis.unimelb.edu.au.
#
# This file was created as part of teaching material for COMP90038
# January, 2020

def CoinRow(C):  # C[0..n-1] holds the coin values
    S = [0] * len(C)
    S[0] = C[0]
    S[1] = max(C[0], C[1])
    for i in range(2, len(C)):
        S[i] = max(S[i - 1], S[i - 2] + C[i])
    return S[-1]

def test():
    print(CoinRow([20, 10, 20, 50, 20, 10, 20]))
    
if __name__ == "__main__":
    test()
