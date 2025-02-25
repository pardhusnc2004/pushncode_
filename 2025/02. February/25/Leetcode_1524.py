'''
    Leetcode Daily Question (25-01-2025)
    1524. Number of Sub-arrays With Odd Sum
    Python3 solution
'''
from typing import List
from collections import *
from bisect import *
from math import *
from heapq import *

class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        d = {}
        cur = 0
        res = 0
        for i in arr:
            cur += i
            if cur&1:
                res += 1
            res += d.get((cur%2)^1, 0)
            d[cur%2] = d.get(cur%2, 0)+1
        return res%(10**9+7)