'''
    Leetcode Daily Question (26-02-2025)
    1749. Maximum Absolute Sum of Any Subarray
    Python3 solution
'''
from typing import List
from collections import *
from bisect import *
from math import *
from heapq import *


class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        cur = [0, 0]
        res = abs(nums[0])

        for i in nums:
            cur[0] += i
            cur[1] += i
            # print(i, cur)
            res = max(res, abs(cur[0]), abs(cur[1]))
            if cur[0] > 0:
                cur[0] = 0
            if cur[1] < 0:
                cur[1] = 0
            # print(i, cur, "after")
        return res