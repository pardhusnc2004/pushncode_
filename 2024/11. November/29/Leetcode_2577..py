'''
    Leetcode Daily Question (29-11-2024)
    2577. Minimum Time to Visit a Cell In a Grid
    Python3 solution
'''
from typing import List
from collections import *
from bisect import *
from math import *
from heapq import *

class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        if grid[0][1] > 1 and grid[1][0] > 1:
            return -1
        dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
        vis = set()
        def valid(x, y):
            return 0 <= x < R and 0 <= y < C
        hp = [(0, 0, 0)]
        while hp:
            curTime, x, y = heappop(hp)
            if x == R-1 and y == C-1:
                return curTime
            if (x, y) in vis:
                continue
            vis.add((x, y))
            for k in range(4):
                nx, ny = x+dx[k], y+dy[k]
                if valid(nx, ny) and (nx, ny) not in vis:
                    wait = 1 if (grid[nx][ny]-curTime)%2 == 0 else 0
                    heappush(hp, (max(curTime+1, grid[nx][ny]+wait), nx, ny))