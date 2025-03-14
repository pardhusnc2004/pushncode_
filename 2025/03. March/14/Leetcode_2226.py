'''
    Leetcode Daily Question (14-03-2025)
    2226. Maximum Candies Allocated to K Children
    Python3 solution
'''
from typing import List
from collections import *
from bisect import *
from math import *
from heapq import *

class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        n = len(candies)

        def good(m):
            cur = 0
            for i in candies:
                cur += i//m
                if cur >= k:
                    return True
            return cur >= k
            pass

        l, r = 1, sum(candies)
        if r < k:
            return 0
        res = -1
        while l <= r:
            m = (l+r)>>1
            if good(m):
                res = m
                l = m+1
            else:
                r = m-1
        return max(res, 0)