# Licensing Information: You are free to use or extend this file for 
# educational purposes provided that (1) you retain this notice, and 
# (2) you provide clear attribution to the University of Melbourne, 
# including a link to https://cis.unimelb.edu.au.
#
# This file was created as part of teaching material for COMP90038
# January, 2020

import random

def Ways(amount, denominations):
    if amount == 0:
        return 1
    if amount < 0:
        return 0
    if len(denominations) == 0:
        return 0
    d = random.sample(denominations, 1)[0]
    return Ways(amount - d, denominations) + Ways(amount, denominations.difference([d]))

def test():
    print(Ways(400, set([5, 10, 20, 50, 100, 200])))

if __name__ == "__main__":
    test()
