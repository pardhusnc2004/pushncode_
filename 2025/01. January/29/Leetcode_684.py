'''
    Leetcode Daily Question (29-01-2025)
    684. Redundant Connection
    Python3 solution
'''
from typing import List
from collections import *
from bisect import *
from math import *
from heapq import *

class DisjointSet:
    def __init__(self, n):
        self.parent = {i:i for i in range(1, n+1)}
        self.size = {i:1 for i in range(1, n+1)}
    def find(self, n):
        if self.parent[n] == n:
            return n
        self.parent[n] = self.find(self.parent[n])
        return self.parent[n]
    def union(self, a, b):
        a, b = self.find(a), self.find(b)
        if a == b:
            return
        if self.size[a] >= self.size[b]:
            self.size[a] += self.size[b]
            self.parent[b] = a
        else:
            self.size[b] += self.size[a]
            self.parent[a] = b
        return

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        dset = DisjointSet(n)
        for i, j in edges:
            if dset.find(i) == dset.find(j):
                return [i, j]
            dset.union(i, j)
        return [-1]