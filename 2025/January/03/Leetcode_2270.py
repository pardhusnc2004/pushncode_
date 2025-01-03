'''
    Leetcode Daily Question (03-01-2025)
    2270. Number of Ways to Split Array
    Python3 solution
'''
from typing import List
from collections import *
from bisect import *
from math import *
from heapq import *

class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        total = sum(nums)
        res = 0
        n = len(nums)
        left = 0
        for i in range(n-1):
            left += nums[i]
            total -= nums[i]
            if left >= total:
                res += 1
        return res