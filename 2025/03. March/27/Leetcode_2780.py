'''
    Leetcode Daily Question (27-03-2025)
    2780. Minimum Index of a Valid Split
    Python3 solution
'''
from typing import List
from collections import *
from bisect import *
from math import *
from heapq import *
from functools import cache

class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        n = len(nums)
        c = Counter(nums)
        EL = self.mooreVoting(nums, n)
        CTR = c[EL]
        left = 0
        for i in range(n-1):
            left += (nums[i] == EL)
            if (left > (i+1)>>1) and ((CTR-left) > (n-1-i)>>1):
                return i
        return -1
    
    def mooreVoting(self, nums, n):
        el, ctr = 0, 1
        for i in nums:
            if i == el:
                ctr += 1
            else:
                ctr -= 1
            if not ctr:
                el = i
                ctr = 1
        return el