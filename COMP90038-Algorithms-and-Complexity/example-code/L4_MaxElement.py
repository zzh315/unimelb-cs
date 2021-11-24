# Licensing Information: You are free to use or extend this file for 
# educational purposes provided that (1) you retain this notice, and 
# (2) you provide clear attribution to the University of Melbourne, 
# including a link to https://cis.unimelb.edu.au.
#
# This file was created as part of teaching material for COMP90038
# January, 2020

def MaxElement(A):
    if len(A) == 0:
        return None
    max = A[0]
    for i in range(len(A)):
        if A[i] > max:
            max = A[i]
    return max

def test():
    print(MaxElement([3, 1, 4, 1, 5, 9, 2, 6]))

if __name__ == "__main__":
    test()
