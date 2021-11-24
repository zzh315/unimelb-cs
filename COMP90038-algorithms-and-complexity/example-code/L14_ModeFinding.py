# Licensing Information: You are free to use or extend this file for 
# educational purposes provided that (1) you retain this notice, and 
# (2) you provide clear attribution to the University of Melbourne, 
# including a link to https://cis.unimelb.edu.au.
#
# This file was created as part of teaching material for COMP90038
# January, 2020

from L11_Mergesort import Mergesort

def ModeFinding(A):
    n = len(A)
    Mergesort(A)
    i = 0
    maxfreq = 0
    while i < n:
        runlength = 1
        while i + runlength < n and A[i + runlength] == A[i]:
            runlength = runlength + 1
        if runlength > maxfreq:
            maxfreq = runlength
            mode = A[i]
        i = i + runlength
    return mode

def test():
    a = [42, 78, 13, 13, 57, 42, 57, 78, 13, 98, 42, 33]
    print(ModeFinding(a))
    
if __name__ == "__main__":
    test()
