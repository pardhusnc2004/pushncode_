'''
    Leetcode Daily Question (14-01-2025)
    2657. Find the Prefix Common Array of Two Arrays
    Python3 solution
'''
from typing import List
from collections import *
from bisect import *
from math import *
from heapq import *

class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        s1, s2 = set(), set()
        res = []
        n = len(A)

        for i in range(n):
            s1.add(A[i])
            s2.add(B[i])
            res.append(len(s2.intersection(s1)))

        return res