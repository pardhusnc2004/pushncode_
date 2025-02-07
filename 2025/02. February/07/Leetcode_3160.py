'''
    Leetcode Daily Question (07-02-2025)
    3160. Find the Number of Distinct Colors Among the Balls
    Python3 solution
'''
from typing import List
from collections import *
from bisect import *
from math import *
from heapq import *

class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        visited = {}
        cols = {}
        unique = 0
        res = []
        for i, c in queries:
            if i in visited:
                cols[visited[i]] -= 1
                if not cols[visited[i]]:
                    del cols[visited[i]]
            cols[c] = cols.get(c, 0)+1
            visited[i] = c
            res.append(len(cols))
        return res