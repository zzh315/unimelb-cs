# Licensing Information: You are free to use or extend this file for 
# educational purposes provided that (1) you retain this notice, and 
# (2) you provide clear attribution to the University of Melbourne, 
# including a link to https://cis.unimelb.edu.au.
#
# This file was created as part of teaching material for COMP90038
# January, 2020

def InterpolationSearch(A, k):
    lo = 0
    hi = len(A) - 1
    while lo < hi:
        if A[lo] > k or A[hi] < k:
            break
        if lo == hi:
            if A[lo] == k:
                return lo
            else:
                break
        m = lo + (k - A[lo]) * (hi - lo) // (A[hi] - A[lo])
        if A[m] == k:
            return m
        if A[m] > k:
            hi = m - 1
        else:
            lo = m + 1
    return -1

def test():
    for i in range(15):
        print(InterpolationSearch([1, 2, 3, 5, 8, 13], i))

if __name__ == "__main__":
    test()
