'''
    Leetcode Daily Question (19-03-2025)
    3191. Minimum Operations to Make Binary Array Elements Equal to One I
    Python3 solution
'''
from typing import List
from collections import *
from bisect import *
from math import *
from heapq import *

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        flips = []
        n = len(nums)

        for i in range(n):
            if flips and i-flips[-1] < 3:
                if len(flips) > 1 and i-flips[-2] < 3:
                    if nums[i] == 0:
                        flips.append(i)
                else:
                    if nums[i] == 1:
                        flips.append(i)
            else:
                if nums[i] == 0:
                    flips.append(i)
        # print(flips)
        if not flips:
            return 0
        return len(flips) if (flips and flips[-1] <= n-3) else -1