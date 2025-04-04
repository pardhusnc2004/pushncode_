'''
    Leetcode Daily Question (03-04-2025)
    2874. Maximum Value of an Ordered Triplet II
    Python3 solution
'''
from typing import List
from collections import *
from bisect import *
from math import *
from heapq import *

class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        maxDiff = 0
        fm = nums[0]
        
        for i in range(1, n-1):
            maxDiff = max(maxDiff, fm-nums[i])
            res = max(res, maxDiff*nums[i+1])

            fm = max(fm, nums[i])

        return res