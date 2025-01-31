'''
    Leetcode Daily Question (31-01-2025)
    827. Making A Large Island
    Python3 solution
'''
from typing import List
from collections import *
from bisect import *
from math import *
from heapq import *

class Ds:
    def __init__(self, n):
        self.par = [i for i in range(n+1)]
        self.size = [1 for i in range(n+1)]
    def findpar(self, a):
        if self.par[a] == a:
            return a
        self.par[a] = self.findpar(self.par[a])
        return self.par[a]
    def union(self, a, b):
        ua, ub = self.findpar(a), self.findpar(b)
        if ua == ub:
            return
        if self.size[ua] > self.size[ub]:
            self.par[ub] = ua
            self.size[ua] += self.size[ub]
        else:
            self.par[ua] = ub
            self.size[ub] += self.size[ua]
class Solution:
    def largestIsland(self, arr: List[List[int]]) -> int:
        m, n = len(arr), len(arr[0])
        ds = Ds(m*n)
        zrs = []
        dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]
        for i in range(m):
            for j in range(n):
                coor = i*n+j
                if not arr[i][j]:
                    ds.size[coor] = 0
                    zrs.append((i, j))
                else:
                    for k in range(4):
                        nr, nc = i+dx[k], j+dy[k]
                        if nr >= 0 and nc >= 0 and nr < m and nc < n and arr[nr][nc]:
                            ncoor = nr*n+nc
                            if ds.findpar(coor) == ds.findpar(ncoor):
                                continue
                            ds.union(coor, ncoor)
        maxsize = max(ds.size[:m*n])
        for i, j in zrs:
            coor = i*n+j
            neighs = set()
            for k in range(4):
                nr, nc = i+dx[k], j+dy[k]
                if nr >= 0 and nc >= 0 and nr < m and nc < n and arr[nr][nc]:
                    ncoor = nr*n+nc
                    neighs.add(ds.findpar(ncoor))
            curres = 0
            for i in neighs:
                curres += ds.size[i]
            maxsize = max(maxsize, curres+1)
        return maxsize