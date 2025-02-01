'''
    Leetcode Daily Question (16-11-2024)
    3254. Find the Power of K-Size Subarrays I
    Python3 solution
'''
from typing import List
from collections import *
from bisect import *

class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        dq = deque()
        res = []
        n = len(nums)
        # left = 0
        for right in range(n):
            if dq and right-dq[0] >= k:
                dq.popleft()
            if dq and nums[right]-nums[dq[-1]] != 1:
                dq.clear()
            dq.append(right)
            if dq:
                if right >= k-1:
                    if right-dq[0] == k-1:
                        res.append(nums[dq[-1]])
                    else:
                        res.append(-1)
        return res