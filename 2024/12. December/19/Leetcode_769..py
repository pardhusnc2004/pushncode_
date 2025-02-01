'''
    Leetcode Daily Question (19-12-2024)
    769. Max Chunks To Make Sorted
    Python3 solution
'''
from typing import *
from collections import *
from bisect import *
from math import *
from heapq import *

class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        def sumToN(n):
            return (n*(n+1))//2
        d = 0
        cursum = 0
        res = 0
        for i in arr:
            cursum += i
            d += 1
            if sumToN(d-1) == cursum:
                res += 1
        return res