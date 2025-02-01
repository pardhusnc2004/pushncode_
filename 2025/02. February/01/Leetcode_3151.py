'''
    Leetcode Daily Question (01-02-2025)
    3151. Special Array I
    Python3 solution
'''
from typing import List
from collections import *
from bisect import *
from math import *
from heapq import *

class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        res = 0
        n = len(nums)
        if n == 1:
            return True
        for i in range(n-1):
            if (nums[i]&1) ^ (nums[i+1]&1):
                res += 1
            else:
                return False

        return True