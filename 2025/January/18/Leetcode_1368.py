'''
    Leetcode Daily Question (18-01-2025)
    1368. Minimum Cost to Make at Least One Valid Path in a Grid
    Python3 solution
'''
from typing import List
from collections import *
from bisect import *
from math import *
from heapq import *

class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        def valid(i, j):
            return 0 <= i < m and 0 <= j < n

        dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
        
        dist = [[inf]*n for _ in range(m)]
        hp = [(0, 0, 0)]
        dist[0][0] = 0
        while hp:
            cost, i, j = heappop(hp)
            # print(f'i {i}, j {j}, cost {cost}')
            if i == m-1 and j == n-1:
                return cost+dist[0][0]
            tmp = grid[i][j]-1

            if valid(i+dx[tmp], j+dy[tmp]):
                if dist[i+dx[tmp]][j+dy[tmp]] > cost:
                    dist[i+dx[tmp]][j+dy[tmp]] = cost
                    heappush(hp, (cost, i+dx[tmp], j+dy[tmp]))
            for k in range(1, 4):
                tmp2 = (tmp+k)%4
                if valid(i+dx[tmp2], j+dy[tmp2]):
                    if dist[i+dx[tmp2]][j+dy[tmp2]] > cost+1:
                        dist[i+dx[tmp2]][j+dy[tmp2]] = cost+1
                        heappush(hp, (cost+1, i+dx[tmp2], j+dy[tmp2]))