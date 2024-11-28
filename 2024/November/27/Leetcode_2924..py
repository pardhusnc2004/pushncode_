'''
    Leetcode Daily Question (27-11-2024)
    3243. Shortest Distance After Road Addition Queries I
    Python3 solution
'''
from typing import List
from collections import *
from bisect import *
from math import *
from heapq import *

class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        adjList = [[] for _ in range(n)]
        for i in range(n-1):
            adjList[i].append(i+1)
        res = []
        for i, j in queries:
            adjList[i].append(j)
            curDist = self.findShortestDistanceBetweenEnds(n, adjList)
            res.append(curDist)
        return res
    def findShortestDistanceBetweenEnds(self, n, adjList):
        hp = [(0, 0)]
        dist = [inf]*n
        dist[0] = 0
        while hp:
            curDist, curNode = heappop(hp)
            if curDist >= dist[-1]:
                break
            for adjNode in adjList[curNode]:
                if curDist + 1 < dist[adjNode]:
                    dist[adjNode] = curDist + 1
                    heappush(hp, (dist[adjNode], adjNode))
        return dist[-1]