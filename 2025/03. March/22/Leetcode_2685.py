'''
    Leetcode Daily Question (22-03-2025)
    2685. Count the Number of Complete Components
    Python3 solution
'''
from typing import *
from collections import *
from bisect import *
from math import *
from heapq import *

class DisjointSet:
    def __init__(self, n):
        self.parent = {i:i for i in range(n)}
        self.size = {i:1 for i in range(n)}
    def find(self, a):
        if self.parent[a] == a:
            return a
        self.parent[a] = self.find(self.parent[a])
        return self.parent[a]
    def union(self, a, b):
        a, b = self.find(a), self.find(b)
        if a != b:
            if self.size[a] >= self.size[b]:
                self.size[a] += self.size[b]
                self.parent[b] = a
            else:
                self.size[b] += self.size[a]
                self.parent[a] = b

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        ds = DisjointSet(n)
        indegree = [0]*n    
        for i, j in edges:
            ds.union(i, j)
            indegree[i] += 1
            indegree[j] += 1

        res = 0
        comps = defaultdict(list)
        for i in range(n):
            comps[ds.find(i)].append(i)

        for i in comps:
            if len(comps[i]) == 1:
                res += 1
            else:
                fl = 1
                for k in comps[i]:
                    if indegree[k] != len(comps[i])-1:
                        fl = 0
                        break
                if fl:
                    res += 1
            
        return res