'''
    Leetcode Daily Question (19-01-2025)
    407. Trapping Rain Water II
    Python3 solution
'''
from typing import List
from collections import *
from bisect import *
from math import *
from heapq import *

class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        m, n = len(heightMap), len(heightMap[0])
        vis = set()
        heap = []
        
        for i in range(m):
            for j in range(n):
                if i == 0 or i == m-1 or j == 0 or j == n-1:
                    heappush(heap, (heightMap[i][j], i, j))
                    vis.add((i, j))
        
        res = 0
        dxy = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        while heap:
            height, x, y = heappop(heap)
            for dx, dy in dxy:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in vis:
                    vis.add((nx, ny))
                    res += max(0, height - heightMap[nx][ny])
                    heappush(heap, (max(height, heightMap[nx][ny]), nx, ny))
        
        return res