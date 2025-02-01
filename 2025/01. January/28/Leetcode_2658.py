'''
    Leetcode Daily Question (28-01-2025)
    2658. Maximum Number of Fish in a Grid
    Python3 solution
'''
from typing import List
from collections import *
from bisect import *
from math import *
from heapq import *

class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        def valid(i, j):
            return 0<=i<m and 0<=j<n
        dxy = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        vis = set()
        def dfs(i, j):
            vis.add((i, j))
            cur = 0
            for k in range(4):
                dx, dy = dxy[k]
                ni, nj = i+dx, j+dy
                if valid(ni, nj) and (ni, nj) not in vis and grid[ni][nj]:
                    vis.add((ni, nj))
                    cur += dfs(ni, nj)
            return cur+grid[i][j]
        
        res = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] and (i, j) not in vis:
                    res = max(res, dfs(i, j))

        return res