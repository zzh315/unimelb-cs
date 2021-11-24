# Licensing Information: You are free to use or extend this file for 
# educational purposes provided that (1) you retain this notice, and 
# (2) you provide clear attribution to the University of Melbourne, 
# including a link to https://cis.unimelb.edu.au.
#
# This file was created as part of teaching material for COMP90038
# January, 2020

def Hanoi(n, init, aux, fin):
    if n > 0:
        Hanoi(n - 1, init, fin, aux)
        fin.append(init.pop())
        print(init)
        print(aux)
        print(fin)
        print("---------")
        Hanoi(n - 1, aux, init, fin)

def test():
    init = [5, 4, 3, 2, 1]
    fin = []
    aux = []
    Hanoi(5, init, aux, fin)

if __name__ == "__main__":
    test()
