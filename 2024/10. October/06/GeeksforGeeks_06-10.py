'''
    GeeksforGeeks Daily Question (06-10-2024)
    Find the number of islands
    Python3 solution
'''

import sys
sys.setrecursionlimit(10**8)
class Solution:
    def numIslands(self, grid):
        def valid(i, j):
            return 0<=i<n and 0<=j<m
        def solve(i, j):
            vis[(i, j)] = 1
            for di in range(-1, 2):
                for dj in range(-1, 2):
                    ni, nj = i+di, j+dj
                    if valid(ni, nj) and (ni, nj) not in vis and grid[ni][nj]:
                        grid[ni][nj] = 0
                        solve(ni, nj)
        res = 0
        vis = {}
        n, m = len(grid), len(grid[0])
        for i in range(n):
            for j in range(m):
                if (i, j) not in vis and grid[i][j]:
                    grid[i][j] = 0
                    res += 1
                    solve(i, j)
        return res