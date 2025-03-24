'''
    Leetcode Daily Question (24-03-2025)
    3169. Count Days Without Meetings
    Python3 solution
'''
from typing import List
from collections import *
from bisect import *
from math import *
from heapq import *

class Solution:
    def countDays(self, days: int, intervals: List[List[int]]) -> int:
        intervals.sort()
        res = []
        res.append(intervals[0])
        for i in range(1, len(intervals)):
            if intervals[i][0] <= res[-1][1]:
                res[-1][1] = max(intervals[i][1], res[-1][1])
            else:
                res.append(intervals[i])
        ans = days
        for x, y in res:
            ans -= (y-x+1)
        return ans
            