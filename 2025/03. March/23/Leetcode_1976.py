'''
    Leetcode Daily Question (23-03-2025)
    1976. Number of Ways to Arrive at Destination
    Python3 solution
'''
from typing import *
from collections import *
from bisect import *
from math import *
from heapq import *

class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        dp = [[inf, 0] for _ in range(n)]
        MOD = 10**9+7
        adjList = defaultdict(list)
        dp[0] = [0, 1]

        for u, v, time in roads:
            adjList[u].append((v, time))
            adjList[v].append((u, time))

        q = [(0, 0)]
        while q:
            curTime, curNode = heappop(q)
            if curTime > dp[-1][0]:
                continue
            
            for adjNode, adjTime in adjList[curNode]:
                if dp[adjNode][0] > curTime+adjTime:
                    dp[adjNode] = [curTime+adjTime, dp[curNode][1]]
                    heappush(q, (curTime+adjTime, adjNode))
                elif dp[adjNode][0] == curTime + adjTime:
                    dp[adjNode][1] += dp[curNode][1]
                dp[adjNode][1] %= MOD
            
        return dp[-1][-1]