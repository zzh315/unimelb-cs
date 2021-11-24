# Licensing Information: You are free to use or extend this file for 
# educational purposes provided that (1) you retain this notice, and 
# (2) you provide clear attribution to the University of Melbourne, 
# including a link to https://cis.unimelb.edu.au.
#
# This file was created as part of teaching material for COMP90038
# January, 2020

def Merge(B, C, A):
    p = len(B)
    q = len(C)
    i = j = k = 0
    while i < p and j < q:
        if B[i] <= C[j]:
            A[k] = B[i]
            i = i + 1
        else:
            A[k] = C[j]
            j = j + 1
        k = k + 1
    if i == p:
        A[k: p + q] = C[j: q]
    else:
        A[k: p + q] = B[i: p]

def Mergesort(A):
    if len(A) > 1:
        n = len(A)
        B = A[:n // 2]
        C = A[n // 2:]
        Mergesort(B)
        Mergesort(C)
        Merge(B, C, A)

def test():
    array = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8]
    Mergesort(array)
    print(array)

if __name__ == "__main__":
    test()
