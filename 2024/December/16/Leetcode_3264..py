'''
    Leetcode Daily Question (16-12-2024)
    3264. Final Array State After K Multiplication Operations I
    Python3 solution
'''
from typing import *
from collections import *
from bisect import *
from math import *
from heapq import *

class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        hp = [(nums[i], i) for i in range(len(nums))]
        heapify(hp)
        for i in range(k):
            last = heappop(hp)
            nums[last[1]] = last[0]*multiplier
            heappush(hp, (last[0]*multiplier, last[1]))
        return nums