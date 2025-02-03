'''
    Leetcode Daily Question (03-02-2025)
    3105. Longest Strictly Increasing or Strictly Decreasing Subarray
    Python3 solution
'''
from typing import List
from collections import *
from bisect import *
from math import *
from heapq import *

class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        res = 1
        for i in range(n):
            cur = 1
            prv = nums[i]
            for j in range(i+1, n):
                if nums[j] > prv:
                    cur += 1
                else:
                    break
                prv = nums[j]
            cur2 = 1
            prv2 = nums[i]
            for j in range(i+1, n):
                if nums[j] < prv2:
                    cur2 += 1
                else:
                    break
                prv2 = nums[j]
            # print(i, cur, cur2)
            res = max(res, cur, cur2)
        return res