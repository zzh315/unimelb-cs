# Licensing Information: You are free to use or extend this file for 
# educational purposes provided that (1) you retain this notice, and 
# (2) you provide clear attribution to the University of Melbourne, 
# including a link to https://cis.unimelb.edu.au.
#
# This file was created as part of teaching material for COMP90038
# January, 2020

def BottomUp(H):
    n = len(H) - 1
    for i in range(n // 2, 0, -1):
        k = i
        v = H[k]
        heap = False
        while not heap and 2 * k <= n:
            j = 2 * k
            if j < n:
                if H[j] < H[j + 1]:
                    j = j + 1
            if v >= H[j]:
                heap = True
            else:
                H[k] = H[j]
                k = j
        H[k] = v

def test():
    a = [0, 2, 9, 7, 6, 5, 8, 3]
    BottomUp(a)
    print(a)
    
if __name__ == "__main__":
    test()