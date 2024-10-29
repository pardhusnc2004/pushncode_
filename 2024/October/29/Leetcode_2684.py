'''
    Leetcode Daily Question (29-10-2024)
    2684. Maximum Number of Moves in a Grid
    Python3 solution
'''
from typing import List, Optional

class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        dp = {}
        m, n = len(grid), len(grid[0])
        def solve(i, j):
            # base  
            if j == n:
                return 0
            if (i, j) in dp:
                return dp[(i, j)]
            maxi = 0
            if i+1 < m and j+1 < n and grid[i][j] < grid[i+1][j+1]:
                maxi = max(maxi, solve(i+1, j+1))
            if i-1 >= 0 and j+1 < n and grid[i][j] < grid[i-1][j+1]:
                maxi = max(maxi, solve(i-1, j+1))
            if j+1 < n and grid[i][j] < grid[i][j+1]:
                maxi = max(maxi, solve(i, j+1))
            dp[(i, j)] = 1+maxi
            return dp[(i, j)]
        maxi = 0
        for i in range(m):
            maxi = max(maxi, solve(i, 0)-1)
                # print(i, j, solve(i, j))
        return maxi