'''
    Leetcode Daily Question (05-02-2025)
    1790. Check if One String Swap Can Make Strings Equal
    Python3 solution
'''
from typing import List
from collections import *
from bisect import *
from math import *
from heapq import *

class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        c1 = Counter(s1)
        c2 = Counter(s2)

        for i in c1:
            if c1[i] != c2.get(i, 0):
                return False
        
        for i in c2:
            if c2[i] != c1.get(i, 0):
                return False
        
        n = len(s1)

        misPlaced = 0
        for i in range(n):
            if s1[i] != s2[i]:
                misPlaced += 1
        
        return misPlaced in [0, 2]