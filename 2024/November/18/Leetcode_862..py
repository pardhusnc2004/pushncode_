'''
    Leetcode Daily Question (18-11-2024)
    862. Shortest Subarray with Sum at Least K
    Python3 solution
'''
from typing import List
from collections import *
from bisect import *
from math import *

class Solution:
    def shortestSubarray(self, nums: List[int], target_sum: int) -> int:
        n = len(nums)
        pref = [0] * (n + 1)
        for i in range(1, n + 1):
            pref[i] = pref[i - 1] + nums[i - 1]

        dq = deque()
        res = inf

        for i in range(n + 1):
            while dq and pref[i] - pref[dq[0]] >= target_sum:
                res = min(res, i - dq.popleft())
            while dq and pref[i] <= pref[dq[-1]]:
                dq.pop()
            dq.append(i)

        return res if res != inf else -1