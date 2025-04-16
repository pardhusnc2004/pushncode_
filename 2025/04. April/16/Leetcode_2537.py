'''
    Leetcode Daily Question (16-04-2025)
    2537. Count the Number of Good Subarrays
    Python3 solution
'''
from typing import List
from collections import *
from bisect import *
from math import *
from heapq import *

class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        n = len(nums)
        res = 0

        d = {}
        left = 0
        tmpK = 0

        for right in range(n):
            tmpK +=  d.get(nums[right], 0)
            d[nums[right]] = d.get(nums[right], 0)+1
            while tmpK >= k:
                res += (n-right)
                tmpK -= (d[nums[left]]-1)
                d[nums[left]] -= 1
                if not d[nums[left]]:
                    del d[nums[left]]
                left += 1
        return res