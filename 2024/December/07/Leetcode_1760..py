'''
    Leetcode Daily Question (07-12-2024)
    1760. Minimum Limit of Balls in a Bag
    Python3 solution
'''
from typing import List
from collections import *
from bisect import *
from math import *
from heapq import *

class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        l, r = 0, sum(nums)
        def good(mid):
            cur = 0
            if mid == 0:
                return False
            for i in nums:
                cur += (i-1)//mid
            return cur <= maxOperations
        res = inf
        while l <= r:
            mid = (l+r) >> 1
            if good(mid):
                res = mid
                r = mid-1
            else:
                l = mid+1
        return res