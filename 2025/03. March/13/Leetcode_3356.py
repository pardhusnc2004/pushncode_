'''
    Leetcode Daily Question (13-03-2025)
    3356. Zero Array Transformation II
    Python3 solution
'''
from typing import List
from collections import *
from bisect import *
from math import *
from heapq import *

class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        if len(set(nums)) == 1 and nums[0] == 0:
            return 0
        
        l, r = 0, len(queries)-1
        res = -1

        def good(m):
            diff = [0]*(n+1)
            for k in range(m+1):
                l, r, v = queries[k]
                diff[l] += v
                diff[r+1] -= v
            for i in range(1, n+1):
                diff[i] += diff[i-1]
            for i in range(n):
                if diff[i] < nums[i]:
                    return False
            return True

        while l <= r:
            m = (l+r) >> 1
            if good(m):
                res = m
                r = m-1
            else:
                l = m+1
        
        return res+1 if 0 < res+1 <= len(queries) else -1