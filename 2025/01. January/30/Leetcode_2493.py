'''
    Leetcode Daily Question (30-01-2025)
    2493. Divide Nodes Into the Maximum Number of Groups
    Python3 solution
'''
from typing import List
from collections import *
from bisect import *
from math import *
from heapq import *

class Solution:
    def isBipartite(self, adj: List[List[int]]) -> bool:
        def solve(curnode, last):
            color[curnode] = last
            for node in adj[curnode]:
                if color[node] == last:
                    return False
                elif color[node] == -1:
                    if not solve(node, last^1):
                        return False
            return True
        n = len(adj)
        color = [-1]*n
        for i in range(n):
            if color[i] == -1:
                if not solve(i, 0):
                    return False
        return True

    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:
        adjList = [[] for _ in range(n)]
        for i, j in edges:
            adjList[i-1].append(j-1)
            adjList[j-1].append(i-1)
                    
        if not self.isBipartite(adjList):
            return -1

        def helper(i, group):
            dist = [inf]*n
            dist[i] = 0

            hp = [(0, i)]
            while hp:
                curDist, node = heappop(hp)
                for adjNode in adjList[node]:
                    if dist[adjNode] > 1+curDist:
                        dist[adjNode] = 1+curDist
                        heappush(hp, (curDist+1, adjNode))
            
            res = 0
            for i in dist:
                if i != inf:
                    res = max(res, i)
            return res

        def solve(group):
            maxi = 0
            for i in group:
                maxi = max(maxi, helper(i, group))
            return maxi

        groups = []
        vis = set()

        for i in range(n):
            if i not in vis:
                ng = deque([i])
                tmp = []
                while ng:
                    node = ng.popleft()
                    if node in vis:
                        continue
                    tmp.append(node)
                    vis.add(node)
                    for adjNode in adjList[node]:
                        if adjNode not in vis:
                            ng.append(adjNode)
                groups.append(tmp)
        # print(groups)
        res = 0
        for group in groups:
            res += solve(group)+1
        return res