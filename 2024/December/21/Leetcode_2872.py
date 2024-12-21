'''
    Leetcode Daily Question (21-12-2024)
    2872. Maximum Number of K-Divisible Components
    Python3 solution
'''
from typing import *
from collections import *
from bisect import *
from math import *
from heapq import *

class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        adjList = [[] for _ in range(n)]
        for i, j in edges:
            adjList[i].append(j)
            adjList[j].append(i)
        vis = set()
        # res = [0]
        def go(node):
            # nonlocal res
            # print(node, "start ----->")
            vis.add(node)
            if not adjList[node]:
                if(values[node]%k == 0):
                    return [0, 1]
                return [values[node], 0]
            compTillNow = 0
            sumTillNow = 0
            for adjNode in adjList[node]:
                if adjNode in vis:
                    continue
                tmp = go(adjNode)
                sumTillNow += tmp[0]
                compTillNow += tmp[1]
            # print(node, "end ----->", [(sumTillNow+values[node])%k, compTillNow+1 if (sumTillNow+values[node])%k == 0 else 0])

            return [(sumTillNow+values[node])%k, compTillNow+1 if (sumTillNow+values[node])%k == 0 else compTillNow]
        res = 0
        for i in range(n):
            if i not in vis:
                res += go(i)[1]
        return res