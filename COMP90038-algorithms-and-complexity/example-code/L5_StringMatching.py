# Licensing Information: You are free to use or extend this file for 
# educational purposes provided that (1) you retain this notice, and 
# (2) you provide clear attribution to the University of Melbourne, 
# including a link to https://cis.unimelb.edu.au.
#
# This file was created as part of teaching material for COMP90038
# January, 2020

def StringMatching(pattern, text):
    m = len(pattern)
    n = len(text)
    for i in range(0, n - m + 1):
        j = 0
        while j < m and pattern[j] == text[i + j]:
            j = j + 1
        if j == m:
            return i
    return -1

def test():
    print(StringMatching("hello", "abchellodef"))

if __name__ == "__main__":
    test()
