'''
    Leetcode Daily Question (14-12-2024)
    2762. Continuous Subarrays
    Python3 solution
'''
from typing import *
from collections import *
from bisect import *
from math import *
from heapq import *


class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        left = 0
        d = {}

        for i in range(n):
            d[nums[i]] = d.get(nums[i], 0)+1
            while max(d.keys()) - min(d.keys()) > 2:
                d[nums[left]] -= 1
                if not d[nums[left]]:
                    del d[nums[left]]
                left += 1
            res += (i-left+1)

        return res