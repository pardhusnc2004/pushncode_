'''
    Leetcode Daily Question (19-01-2025)
    2661. First Completely Painted Row or Column
    Python3 solution
'''
from typing import List
from collections import *
from bisect import *
from math import *
from heapq import *

class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        k = len(arr)
        rows, cols = [0]*m, [0]*n
        mp = {}
        for i in range(m):
            for j in range(n):
                mp[mat[i][j]] = (i, j)
        for i in range(k):
            r, c = mp[arr[i]]
            rows[r] += 1
            cols[c] += 1
            if rows[r] == n or cols[c] == m:
                return i
        