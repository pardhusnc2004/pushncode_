'''
    Leetcode Daily Question (06-04-2025)
    368. Largest Divisible Subset
    Python3 solution
'''
from typing import List
from collections import *
from bisect import *
from math import *
from heapq import *

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums.sort()
        maxIndex = 0
        dp = [[1, i] for i in range(n)]
        for i in range(n):
            for j in range(i):
                if nums[i]%nums[j] == 0:
                    if dp[i][0] < 1+dp[j][0]:
                        dp[i] = [1+dp[j][0], j]
            if dp[maxIndex][0] < dp[i][0]:
                maxIndex = i
        
        res = []
        vis = set()
        while maxIndex >= 0 and maxIndex not in vis:
            vis.add(maxIndex)
            res.append(nums[maxIndex])
            maxIndex = dp[maxIndex][1]
        return res[::-1]