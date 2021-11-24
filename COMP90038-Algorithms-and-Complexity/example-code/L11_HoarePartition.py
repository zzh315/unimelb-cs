# Licensing Information: You are free to use or extend this file for 
# educational purposes provided that (1) you retain this notice, and 
# (2) you provide clear attribution to the University of Melbourne, 
# including a link to https://cis.unimelb.edu.au.
#
# This file was created as part of teaching material for COMP90038
# January, 2020

def HoarePartition(A, lo, hi):
    p = A[lo]
    i = lo
    j = hi
    while i < j:
        while i < hi and A[i] <= p:
            i = i + 1
        while j >= lo and A[j] > p:
            j = j - 1
        A[i], A[j] = A[j], A[i]
    A[i], A[j] = A[j], A[i]
    A[lo], A[j] = A[j], A[lo]
    return j

def test():
    array = [3, 1, 4, 5, 9, 2, 6, 8]
    print(HoarePartition(array, 0, len(array) - 1))
    print(array)
    
if __name__ == "__main__":
    test()
