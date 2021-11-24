# Licensing Information: You are free to use or extend this file for 
# educational purposes provided that (1) you retain this notice, and 
# (2) you provide clear attribution to the University of Melbourne, 
# including a link to https://cis.unimelb.edu.au.
#
# This file was created as part of teaching material for COMP90038
# January, 2020

def Fib(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    return Fib(n - 1) + Fib(n - 2)

def Fib2(n, a=1, b=0):
    if n == 0:
        return a
    return Fib2(n - 1, a + b, a)

def Fib3(n):
    a = 1
    b = 0
    while n > 0:
        a = a + b
        b = a - b
        n = n - 1
    return a

def test():
    print(Fib(15))
    print(Fib2(16))
    print(Fib3(17))

if __name__ == "__main__":
    test()
