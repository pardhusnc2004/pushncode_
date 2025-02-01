'''
    Leetcode Daily Question (19-11-2024)
    2461. Maximum Sum of Distinct Subarrays With Length K
    Python3 solution
'''
from typing import List
from collections import *
from bisect import *
from math import *

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        d = {}
        res = 0
        left = 0
        curSum = 0
        for i in range(len(nums)):
            d[nums[i]] = d.get(nums[i], 0)+1
            curSum += nums[i]
            while i-left >= k or d[nums[i]] > 1:
                d[nums[left]] -= 1
                curSum -= nums[left]
                if not d[nums[left]]:
                    del d[nums[left]]
                left += 1
            if i >= k-1 and len(d) == k:
                res = max(res, curSum)
        return res