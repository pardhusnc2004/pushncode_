'''
    Leetcode Daily Question (08-04-2025)
    3396. Minimum Number of Operations to Make Elements in Array Distinct
    Python3 solution
'''
from typing import List
from collections import *
from bisect import *
from math import *
from heapq import *

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        c = Counter(nums)
        res = 0
        n = len(nums)
        if len(c) == len(nums):
            return 0
        while nums:
            i = 0
            res += 1
            while nums and i<3:
                i += 1
                tmp = nums.pop(0)
                c[tmp] -= 1
                if not c[tmp]:
                    del c[tmp]
            if len(c) == len(nums):
                return res
        return res