'''
    Leetcode Daily Question (13-12-2024)
    2593. Find Score of an Array After Marking All Elements
    Python3 solution
'''
from typing import *
from collections import *
from bisect import *
from math import *
from heapq import *


class Solution:
    def findScore(self, nums: List[int]) -> int:
        vis = set()
        nums = [[nums[i], i] for i in range(len(nums))]
        heapify(nums)
        res = 0
        while nums:
            smallest, _ = heappop(nums)
            # print(smallest, _, res, vis)
            if _ in vis:
                continue
            vis.add(_)
            res += smallest
            vis.add(_-1)
            vis.add(_+1)
        return res