'''
    Leetcode Daily Question (22-01-2025)
    1765. Map of Highest Peak
    Python3 solution
'''
from typing import List
from collections import *
from bisect import *
from math import *
from heapq import *

class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        # hp = []
        hp = deque([])
        m, n = len(isWater), len(isWater[0])
        for i in range(m):
            for j in range(n):
                if isWater[i][j]:
                    # heappush(hp, (0, i, j))
                    hp.append((0, i, j))
                    isWater[i][j] = 0
                else:
                    isWater[i][j] = inf
        dxy = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        while hp:
            # level, i, j = heappop(hp)
            level, i, j = hp.popleft()
            for k in range(4):
                dx, dy = dxy[k]
                ni, nj = i+dx, j+dy
                if 0<=ni<m and 0<=nj<n and isWater[ni][nj]>1+level:
                    isWater[ni][nj] = 1+level
                    # heappush(hp, (level+1, ni, nj))
                    hp.append((level+1, ni, nj))
        return isWater