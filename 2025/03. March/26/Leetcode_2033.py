'''
    Leetcode Daily Question (26-03-2025)
    2033. Minimum Operations to Make a Uni-Value Grid
    Python3 solution
'''
from typing import List
from collections import *
from bisect import *
from math import *
from heapq import *


class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        m, n = len(grid), len(grid[0])
        mods = defaultdict(int)

        for i in range(m):
            for j in range(n):
                mods[grid[i][j]%x] += 1

        if len(mods) > 1:
            return -1
        
        lst = sum(grid, [])
        lst.sort()
        md = len(lst)//2
        res = 0

        for i in lst:
            res += abs(i-lst[md])//x

        return res