'''
    Leetcode Daily Question (25-01-2025)
    2948. Make Lexicographically Smallest Array by Swapping Elements
    Python3 solution
'''
from typing import List
from collections import *
from bisect import *
from math import *
from heapq import *

class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        tmp = sorted(nums)
        # print(tmp)
        groups = [deque([])]
        for i in tmp:
            if not groups[-1] or abs(i-groups[-1][-1]) <= limit:
                groups[-1].append(i)
            else:
                groups.append(deque([i]))

        d = {}
        for i in range(len(groups)):
            for j in groups[i]:
                d[j] = i
        
        res = []
        # print(d)
        for i in nums:
            idx = d[i]
            # print(idx, groups[idx])
            k = groups[idx].popleft()
            res.append(k)
        return res