'''
    Leetcode Daily Question (02-04-2025)
    2873. Maximum Value of an Ordered Triplet I
    Python3 solution
'''
from typing import List
from collections import *
from bisect import *
from math import *
from heapq import *

class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        fmax, smax, diff = 0, 0, 0
        res = 0
        n = len(nums)
        for i in range(n-1):
            if nums[i]>fmax:
                fmax=smax=nums[i]
            else:
                smax = min(smax, nums[i])
            if fmax==0 or smax==0:
                continue
            diff = max(diff, fmax-smax)
            res = max(res, diff*nums[i+1])
        return res