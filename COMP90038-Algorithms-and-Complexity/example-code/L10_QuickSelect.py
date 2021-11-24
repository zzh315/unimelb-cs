# Licensing Information: You are free to use or extend this file for 
# educational purposes provided that (1) you retain this notice, and 
# (2) you provide clear attribution to the University of Melbourne, 
# including a link to https://cis.unimelb.edu.au.
#
# This file was created as part of teaching material for COMP90038
# January, 2020

from L10_LomutoPartition import LomutoPartition

def QuickSelect(A, lo, hi, k):
    s = LomutoPartition(A, lo, hi)
    if s - lo == k - 1:
        return A[s]
    else:
        if s - lo > k - 1:
            return QuickSelect(A, lo, s - 1, k)
        else:
            return QuickSelect(A, s + 1, hi, (k - 1) - (s - lo))

def test():
    array = [3, 1, 4, 5, 9, 2, 6, 8]
    print(QuickSelect(array, 0, len(array) - 1, 6))

if __name__ == "__main__":
    test()
