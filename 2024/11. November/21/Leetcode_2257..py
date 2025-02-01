'''
    Leetcode Daily Question (21-11-2024)
    2257. Count Unguarded Cells in the Grid
    Python3 solution
'''
from typing import List
from collections import *
from bisect import *
from math import *

class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
        # guardsSize, wallsSize = len(guards), len(walls)
        walls = set([(i, j) for i, j in walls])
        guards = set([(i, j) for i, j in guards])
        grid = [[0]*n for _ in range(m)]
        res = 0
        hp = deque([('Guard', i, j) for i, j in guards])
        while hp:
            _, i, j = hp.popleft()
            if _ == 'Guard':
                for k in range(4):
                    ni, nj = i + dx[k], j + dy[k]
                    if 0 <= ni < m and 0 <= nj < n and (ni, nj) not in walls and (ni, nj) not in guards:
                        grid[ni][nj] += 1
                        hp.append((k, ni, nj))
            else:
                ni, nj = i + dx[_], j + dy[_]
                if 0 <= ni < m and 0 <= nj < n and (ni, nj) not in walls and (ni, nj) not in guards:
                    grid[ni][nj] += 1
                    hp.append((_, ni, nj))
                

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0 and (i, j) not in walls and (i, j) not in guards:
                    res += 1
        # for row in grid:
            # print(*row)
        return res