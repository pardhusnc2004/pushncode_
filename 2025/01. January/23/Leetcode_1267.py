'''
    Leetcode Daily Question (23-01-2025)
    1267. Count Servers that Communicate
    Python3 solution
'''
from typing import List
from collections import *
from bisect import *
from math import *
from heapq import *

class DisjointSet:
    def __init__(self, n):
        self.parent = {i:i for i in range(n)}
        self.size = {i:1 for i in range(n)}
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
    

class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        ds = DisjointSet(m+n+1)
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    ds.union(i, j+m)
        
        d = {}
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    a, b = i, j+m
                    pa, pb = ds.find(a), ds.find(b)
                    if ds.size[pa] > 1:
                        d[pa] = d.get(pa, 0)+1
                    if pa == pb:
                        continue
                    if ds.size[pb] > 1:
                        d[pb] = d.get(pb, 0)+1
        # print(ds.parent)
        # print(ds.size)
        # print(d)
        res = 0
        for i in d:
            if d[i] > 1:
                res += d[i]
        return res