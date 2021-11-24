# Licensing Information: You are free to use or extend this file for 
# educational purposes provided that (1) you retain this notice, and 
# (2) you provide clear attribution to the University of Melbourne, 
# including a link to https://cis.unimelb.edu.au.
#
# This file was created as part of teaching material for COMP90038
# January, 2020

def BinSearch(A, lo, hi, key):
    if lo > hi:
        return -1
    mid = lo + (hi - lo) // 2
    if A[mid] == key:
        return mid
    else:
        if A[mid] > key:
            return BinSearch(A, lo, mid - 1, key)
        else:
            return BinSearch(A, mid + 1, hi, key)

def test():
    A = [1, 2, 3, 5, 8, 13, 21, 34, 55]
    print(BinSearch(A, 0, len(A) - 1, 5))
    print(BinSearch(A, 0, len(A) - 1, 50))

if __name__ == "__main__":
    test()
