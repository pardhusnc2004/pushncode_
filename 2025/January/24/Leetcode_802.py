'''
    Leetcode Daily Question (24-01-2025)
    802. Find Eventual Safe States
    Python3 solution
'''
from typing import List
from collections import *
from bisect import *
from math import *
from heapq import *

class Solution:
    def eventualSafeNodes(self, rgraph: List[List[int]]) -> List[int]:
        n = len(rgraph)
        res = []
        graph = [[] for _ in range(n)]
        for i in range(n):
            for j in rgraph[i]:
                graph[j].append(i)

        topo = self.getTopo(n, graph)
        return sorted(topo)

    def getTopo(self, n, graph):
        indegree = [0]*n
        for i in range(n):
            for j in graph[i]:
                indegree[j] += 1
        topo = []
        q = deque([])
        for i in range(n):
            if indegree[i] == 0:
                q.append(i)

        while q:
            node = q.popleft()
            topo.append(node)
            for adjNode in graph[node]:
                indegree[adjNode] -= 1
                if not indegree[adjNode]:
                    q.append(adjNode)
        
        return topo