'''
    Leetcode Daily Question (20-03-2025)
    3108. Minimum Cost Walk in Weighted Graph
    Python3 solution
'''
from typing import List
from collections import *
from bisect import *
from math import *
from heapq import *

class Solution:
    def minimumCost(self, N: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        adj_list = defaultdict(list)
        for u, v, w in edges:
            adj_list[u].append((v, w))
            adj_list[v].append((u, w))

        visited = [False] * N        
        def visit(node):
            tw = (1 << 20) - 1

            q = deque()
            q.append(node)
            visited[node] = True

            while len(q) > 0:
                current = q.popleft()
                root[current] = node

                for v, w in adj_list[current]:
                    tw &= w
                    if not visited[v]:
                        q.append(v)
                        visited[v] = True

            costs[node] = tw

        costs = {}
        root = [None] * N

        ans = []
        for u, v in query:
            if not visited[u]:
                visit(u)
            if not visited[v]:
                visit(v)

            ru = root[u]
            rv = root[v]

            if ru == rv:
                ans.append(costs[ru])
            else:
                ans.append(-1)
        return ans