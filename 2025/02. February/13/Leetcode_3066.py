'''
    Leetcode Daily Question (13-02-2025)
    3066. Minimum Operations to Exceed Threshold Value II
    Python3 solution
'''
from typing import List
from collections import *
from bisect import *
from math import *
from heapq import *

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        res = 0

        heapify(nums)
        while len(nums) >= 2:
            x, y = heappop(nums), heappop(nums)
            if x >= k and y >= k:
                break
            res += 1
            heappush(nums, min(x, y)*2+max(x, y))

        return res