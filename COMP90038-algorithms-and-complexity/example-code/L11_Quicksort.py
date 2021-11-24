# Licensing Information: You are free to use or extend this file for 
# educational purposes provided that (1) you retain this notice, and 
# (2) you provide clear attribution to the University of Melbourne, 
# including a link to https://cis.unimelb.edu.au.
#
# This file was created as part of teaching material for COMP90038
# January, 2020

from L10_LomutoPartition import LomutoPartition
from L11_HoarePartition import HoarePartition

Partition = LomutoPartition

def Quicksort(A, lo, hi):
    if lo < hi:
        s = Partition(A, lo, hi)
        Quicksort(A, lo, s - 1)
        Quicksort(A, s + 1, hi)

def test():
    array = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8]
    Quicksort(array, 0, len(array) - 1)
    print(array)

if __name__ == "__main__":
    test()