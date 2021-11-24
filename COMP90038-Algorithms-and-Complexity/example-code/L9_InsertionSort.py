# Licensing Information: You are free to use or extend this file for 
# educational purposes provided that (1) you retain this notice, and 
# (2) you provide clear attribution to the University of Melbourne, 
# including a link to https://cis.unimelb.edu.au.
#
# This file was created as part of teaching material for COMP90038
# January, 2020

def InsertionSort(A):
    for i in range(1, len(A)):
        v = A[i]
        j = i - 1
        while j >= 0 and v < A[j]:
            A[j + 1] = A[j]
            j = j - 1
        A[j + 1] = v

def test():
    A = [3, 1, 4, 5, 9, 2, 6, 8, 7, 0]
    InsertionSort(A)
    print(A)

if __name__ == "__main__":
    test()
