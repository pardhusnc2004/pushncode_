'''
    Leetcode Daily Question (18-03-2025)
    2401. Longest Nice Subarray
    Python3 solution
'''
from typing import List
from collections import *
from bisect import *
from math import *
from heapq import *

class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        left = 0
        cur = defaultdict(int)
        for right in range(n):
            for k in range(32):
                if nums[right]&(1<<k):
                    cur[k] += 1
            while max(cur.values()) > 1:
                for k in range(32):
                    if nums[left]&(1<<k):
                        cur[k] -= 1
                left += 1
            # print(right, cur)
            res = max(res, 1+right-left)
        return res