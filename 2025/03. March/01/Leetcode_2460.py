'''
    Leetcode Daily Question (01-03-2025)
    2460. Apply Operations to an Array
    Python3 solution
'''
from typing import List
from collections import *
from bisect import *
from math import *
from heapq import *

class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n-1):
            if nums[i] == nums[i+1]:
                nums[i] *= 2
                nums[i+1] = 0
        zero = nums.count(0)
        l = 0
        for i in nums:
            if i != 0:
                nums[l] = i
                l += 1
        while l < n:
            nums[l] = 0
            l += 1
        return nums