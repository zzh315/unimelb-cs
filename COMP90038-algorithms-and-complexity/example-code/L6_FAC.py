# Licensing Information: You are free to use or extend this file for 
# educational purposes provided that (1) you retain this notice, and 
# (2) you provide clear attribution to the University of Melbourne, 
# including a link to https://cis.unimelb.edu.au.
#
# This file was created as part of teaching material for COMP90038
# January, 2020

def FAC(n):
    if n == 0:
        return 1
    return FAC(n - 1) * n

def FAC2(n):
    result = 1
    while n > 0:
        result = result * n
        n = n - 1
    return result

def test():
    print(FAC(7))
    print(FAC2(7))

if __name__ == "__main__":
    test()
