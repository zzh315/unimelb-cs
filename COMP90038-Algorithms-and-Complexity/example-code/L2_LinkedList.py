# Licensing Information: You are free to use or extend this file for 
# educational purposes provided that (1) you retain this notice, and 
# (2) you provide clear attribution to the University of Melbourne, 
# including a link to https://cis.unimelb.edu.au.
#
# This file was created as part of teaching material for COMP90038
# January, 2020

class node:
    def __init__(self, val=None):
        self.val = val
        self.next = None
    
    def __str__(self):
        return str(self.val)

def find(p, value):
    while p != None:
        if p.val == value:
            return p
        p = p.next
    return None

def test():
    firstnode = node(50)
    secondnode = node(30)
    firstnode.next = secondnode
    print(find(firstnode, 30))
    print(find(firstnode, 1))

if __name__ == "__main__":
    test()
