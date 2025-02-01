'''
    Leetcode Daily Question (26-12-2024)
    494. Target Sum
    Python solution
'''
from typing import *
from collections import *
from bisect import *
from math import *
from heapq import *

class Solution(object):
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        dp = {}
        def solve(nums, rem, ind) :
            if not rem and ind==len(nums):
                return 1
            if ind >= len(nums):
                return 0
            if (ind, rem) in dp:
                return dp[(ind, rem)]
            neg = solve(nums, rem+nums[ind], ind+1)
            pos = solve(nums, rem-nums[ind], ind+1)
            dp[(ind, rem)] = neg+pos
            return neg + pos
        return solve(nums, target, 0)