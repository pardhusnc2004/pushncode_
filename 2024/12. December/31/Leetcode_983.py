'''
    Leetcode Daily Question (31-12-2024)
    983. Minimum Cost For Tickets
    Python3 solution
'''
from typing import *
from collections import *
from bisect import *
from math import *
from heapq import *
from functools import *

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        n = len(days)
        @cache
        def solve(i):
            if i >= n:
                return 0
            res = inf
            # 1-day
            oneday = solve(i+1)
            res = min(res, costs[0]+oneday)
            # 7-day
            sevenday = solve(bisect_right(days, days[i]+6))
            res = min(res, costs[1]+sevenday)
            # 30-day
            thirtyday = solve(bisect_right(days, days[i]+29))
            res = min(res, costs[2]+thirtyday)
            return res
        return solve(0)
        
