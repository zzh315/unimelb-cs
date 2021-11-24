# Licensing Information: You are free to use or extend this file for 
# educational purposes provided that (1) you retain this notice, and 
# (2) you provide clear attribution to the University of Melbourne, 
# including a link to https://cis.unimelb.edu.au.
#
# This file was created as part of teaching material for COMP90038
# January, 2020

from L11_Mergesort import Mergesort

def BruteForce(A):
    n = len(A)
    for i in range(0, n - 1):
        for j in range(i + 1, n):
            if A[i] == A[j]:
                return False
    return True

def Presorting(A):
    n = len(A)
    Mergesort(A)
    for i in range(0, n - 2):
        if A[i] == A[i + 1]:
            return False
    return True

def test():
    a = [3, 1, 4, 5, 9, 2, 6, 8]
    print(BruteForce(a))
    
if __name__ == "__main__":
    test()
