'''
    Leetcode Daily Question (02-02-2025)
    1752. Check if Array Is Sorted and Rotated
    Python3 solution
'''
from typing import List
from collections import *
from bisect import *
from math import *
from heapq import *

class Solution:
    def check(self, nums: List[int]) -> bool:
        ct = 0
        n = len(nums)
        
        for i in range(n-1):
            if nums[i] <= nums[i+1]:
                continue
            else:
                ct += 1
        if nums[-1] > nums[0]:
            ct += 1
        if ct > 1:
            return False
        return True