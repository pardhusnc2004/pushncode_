'''
    Leetcode Daily Question (09-02-2025)
    2364. Count Number of Bad Pairs
    Python3 solution
'''
from typing import List
from collections import *
from bisect import *
from math import *
from heapq import *

class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        n = len(nums)
        TOTAL_PAIRS = (n*(n-1))//2
        good = 0

        d = {}
        for i in range(n):
            tmp = i-nums[i]
            good += d.get(tmp, 0)
            d[tmp] = d.get(tmp, 0)+1
            # print(i, good, d)

        return TOTAL_PAIRS - good