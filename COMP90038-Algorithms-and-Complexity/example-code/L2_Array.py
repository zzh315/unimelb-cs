# Licensing Information: You are free to use or extend this file for 
# educational purposes provided that (1) you retain this notice, and 
# (2) you provide clear attribution to the University of Melbourne, 
# including a link to https://cis.unimelb.edu.au.
#
# This file was created as part of teaching material for COMP90038
# January, 2020

def find(A, x, lo, hi):
# initial call: find(A, x, 0, len(A) - 1)
    if lo > hi:
        return -1
    elif A[lo] == x:
        return lo
    else:
        return find(A, x, lo + 1, hi)

def test():
    A = [1, 2, 3, 5, 8, 13]
    print(find(A, 8, 0, len(A) - 1))
    print(find(A, 6, 0, len(A) - 1))

if __name__ == "__main__":
    test()
