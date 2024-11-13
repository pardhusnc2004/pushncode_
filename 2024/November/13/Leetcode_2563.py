'''
    Leetcode Daily Question (12-11-2024)
    2563. Count the Number of Fair Pairs
    Python3 solution
'''
from typing import List
from collections import *
from bisect import *

class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        dp = []
        res = 0
        for num in nums:
            if not dp:
                dp.append(num)
                continue
            minReq, maxPoss = lower-num, upper-num
            l, r = bisect_left(dp, minReq), bisect_right(dp, maxPoss)
            # print(num, dp, minReq, maxPoss, l, r)
            res += r-l
            insort_left(dp, num)
        return res
