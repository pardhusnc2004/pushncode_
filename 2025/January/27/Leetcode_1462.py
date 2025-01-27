'''
    Leetcode Daily Question (27-01-2025)
    1462. Course Schedule IV
    Python3 solution
'''
from typing import List
from collections import *
from bisect import *
from math import *
from heapq import *

class Solution:
    def checkIfPrerequisite(self, n: int, adjList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adjMat = [[0]*n for _ in range(n)]
        for i, j in adjList:
            adjMat[i][j] = 1
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if adjMat[i][j]:
                        continue
                    adjMat[i][j] = adjMat[i][k]&adjMat[k][j]
        res = []
        for i, j in queries:
            res.append(True if adjMat[i][j] else False)
        return res