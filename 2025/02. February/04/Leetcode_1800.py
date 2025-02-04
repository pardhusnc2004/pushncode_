'''
    Leetcode Daily Question (04-02-2025)
    1800. Maximum Ascending Subarray Sum
    Python3 solution
'''
from typing import List
from collections import *
from bisect import *
from math import *
from heapq import *

class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        res = 0
        cur = 0
        prv = -1
        for i in nums:
            if i > prv:
                cur += i
            else:
                cur = i
            res = max(res, cur)
            prv = i

        return res