# Licensing Information: You are free to use or extend this file for 
# educational purposes provided that (1) you retain this notice, and 
# (2) you provide clear attribution to the University of Melbourne, 
# including a link to https://cis.unimelb.edu.au.
#
# This file was created as part of teaching material for COMP90038
# January, 2020

def LomutoPartition(A, lo, hi):
    p = A[lo]
    s = lo
    for i in range(lo + 1, hi + 1):
        if A[i] < p:
            s = s + 1
            A[s], A[i] = A[i], A[s]
    A[s], A[lo] = A[lo], A[s]
    return s

def test():
    array = [3, 1, 4, 5, 9, 2, 6, 8]
    print(LomutoPartition(array, 0, len(array) - 1))
    print(array)
    
if __name__ == "__main__":
    test()
