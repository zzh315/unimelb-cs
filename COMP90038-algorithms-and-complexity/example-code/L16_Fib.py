# Licensing Information: You are free to use or extend this file for 
# educational purposes provided that (1) you retain this notice, and 
# (2) you provide clear attribution to the University of Melbourne, 
# including a link to https://cis.unimelb.edu.au.
#
# This file was created as part of teaching material for COMP90038
# January, 2020

def Fib(n):
    global F
    if n == 0 or n == 1:
        return 1
    result = F[n]
    if result == 0:
        result = Fib(n - 1) + Fib(n - 2)
        F[n] = result
    return result

def test():
    global F
    n = 50
    F = [0] * (n + 1)
    print(Fib(n))
    
if __name__ == "__main__":
    test()
