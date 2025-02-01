'''
    Leetcode Daily Question (26-11-2024)
    2924. Find Champion II
    Python3 solution
'''
from typing import List
from collections import *
from bisect import *
from math import *

class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        indegree = [0]*n
        adjList = defaultdict(list)
        for i, j in edges:
            indegree[j] += 1
            adjList[i].append(j)
        st = []
        for i in range(n):
            if indegree[i] == 0:
                if len(st) > 0:
                    return -1
                st.append(i)
        return st[-1]