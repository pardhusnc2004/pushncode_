'''
    Leetcode Daily Question (31-10-2024)
    2463. Minimum Total Distance Traveled
    Python3 solution
'''
from math import inf
from typing import List, Optional
from functools import cache

class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:

        factory = [[i, j] for i, j in factory if j]
        factory.sort()
        robot.sort()
        m, n = len(robot), len(factory)

        @cache
        def solve(i, j, used):
            if i >= m:
                return 0
            if j >= n:
                return inf
            mini = solve(i, j+1, 0)
            if factory[j][1] > used:
                mini = min(mini, abs(robot[i]-factory[j][0]) + solve(i+1, j, 1+used))
            return mini

        return solve(0, 0, 0)