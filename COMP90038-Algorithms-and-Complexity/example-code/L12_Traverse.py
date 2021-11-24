# Licensing Information: You are free to use or extend this file for 
# educational purposes provided that (1) you retain this notice, and 
# (2) you provide clear attribution to the University of Melbourne, 
# including a link to https://cis.unimelb.edu.au.
#
# This file was created as part of teaching material for COMP90038
# January, 2020

from L12_TreeNode import Node
from queue import Queue

def PreorderTraverse(T):
    if T is not None:
        print(T.val)
        PreorderTraverse(T.left)
        PreorderTraverse(T.right)

def InorderTraverse(T):
    if T is not None:
        InorderTraverse(T.left)
        print(T.val)
        InorderTraverse(T.right)

def PostorderTraverse(T):
    if T is not None:
        PostorderTraverse(T.left)
        PostorderTraverse(T.right)
        print(T.val)

def LevelorderTraverse(T):
    Q = Queue()
    Q.put(T)
    while not Q.empty():
        X = Q.get()
        print(X.val)
        if X.left is not None:
            Q.put(X.left)
        if X.right is not None:
            Q.put(X.right)

def test():
    T = Node(17)
    T.left = Node(33)
    T.left.left = Node(19)
    T.left.right = Node(16)
    T.left.right.left = Node(38)
    T.left.right.right = Node(31)
    T.right = Node(48)
    T.right.left = Node(11)
    T.right.right = Node(14)
    
    PreorderTraverse(T)
    
if __name__ == "__main__":
    test()
