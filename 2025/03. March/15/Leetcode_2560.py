'''
    Leetcode Daily Question (15-03-2025)
    2560. House Robber IV
    Python3 solution
'''
from typing import List
from collections import *
from bisect import *
from math import *
from heapq import *

class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        n = len(nums)
        res = inf

        def good(m):
            prv = -2
            tmp = 0
            for i in range(n):
                if i-prv >= 2 and nums[i] <= m:
                    prv = i
                    tmp += 1
            return tmp >= k
            pass

        l, r = 1, max(nums)
        while l <= r:
            m = (l+r) >> 1
            if(good(m)):
                res = m
                r = m-1
            else:
                l = m+1 

        return res