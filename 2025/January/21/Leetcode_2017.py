'''
    Leetcode Daily Question (21-01-2025)
    2017. Grid Game
    Python3 solution
'''
from typing import List
from collections import *
from bisect import *
from math import *
from heapq import *

class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        n = len(grid[0])

        pref1, suff0 = [0]*(n+1), [0]*(n+1)

        for i in range(n):
            pref1[i+1] = pref1[i]+grid[1][i]
        for i in range(n-1, -1, -1):
            suff0[i] = suff0[i+1]+grid[0][i]

        res = inf
        for vis in range(n):
            tmp = max(pref1[vis], suff0[vis+1])
            res = min(tmp, res)

        return res