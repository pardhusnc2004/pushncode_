'''
    Leetcode Daily Question (08-12-2024)
    2054. Two Best Non-Overlapping Events
    Python3 solution
'''
from typing import List
from collections import *
from bisect import *
from math import *
from heapq import *

class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        hp = []
        events.sort(key=lambda x: x[0])
        maxi = 0
        res = 0
        for start, end, value in events:
            while hp and hp[0][0] < start:
                maxi = max(maxi, hp[0][1])
                heappop(hp)
            res = max(res, maxi + value)
            heappush(hp, (end, value))
        return res