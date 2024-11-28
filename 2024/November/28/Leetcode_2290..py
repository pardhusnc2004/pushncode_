'''
    Leetcode Daily Question (28-11-2024)
    2290. Minimum Obstacle Removal to Reach Corner
    Python3 solution
'''
from typing import List
from collections import *
from bisect import *
from math import *
from heapq import *

class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dist = [[[inf, inf] for __ in range(n)] for _ in range(m)]
        hp = [(grid[0][0], 0, 0, 0)]
        dist[0][0] = [grid[0][0], 0]
        dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
        def valid(i, j):
            return 0 <= i < m and 0 <= j < n
        while hp:
            curObstacles, curDist, curI, curJ = heappop(hp)
            # print(dist[-1][-1])
            # assert 0 != 0
            if curObstacles >= dist[-1][-1][0]:
                break
            for k in range(4):
                nI, nJ = curI+dx[k], curJ+dy[k]
                if valid(nI, nJ):
                    if dist[nI][nJ][0] > curObstacles + grid[nI][nJ]:
                        if nI == m-1 and nJ == n-1:
                            return curObstacles + grid[nI][nJ]
                        dist[nI][nJ] = [curObstacles + grid[nI][nJ], curDist + 1]
                        heappush(hp, (dist[nI][nJ][0], dist[nI][nJ][1], nI, nJ))
        return dist[-1][-1][0]