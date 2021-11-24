# Licensing Information: You are free to use or extend this file for 
# educational purposes provided that (1) you retain this notice, and 
# (2) you provide clear attribution to the University of Melbourne, 
# including a link to https://cis.unimelb.edu.au.
#
# This file was created as part of teaching material for COMP90038
# January, 2020

def F(n):
    if n == 0:
        return 1
    else:
        return F(n - 1) * n

def test():
    print(F(7))

if __name__ == "__main__":
    test()
