'''
    GeeksforGeeks Daily Question (11-04-2025)
    Dijkstra Algorithm
    Python3 solution
'''

from math import *
from heapq import *

class Solution:
    # Function to find the shortest distance of all the vertices
    # from the source vertex src.
    def dijkstra(self, n, edges, src):
        # Your code here
        adj = [[] for _ in range(n)]
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w))
        dist = [inf]*n
        dist[src] = 0
        hp = [(0, src)]
        while hp:
            curDist, curNode = heappop(hp)
            for adjNode, adjWt in adj[curNode]:
                if dist[adjNode] > adjWt+curDist:
                    dist[adjNode] = adjWt+curDist
                    heappush(hp, (dist[adjNode], adjNode))
        for i in range(n):
            if dist[i] == inf:
                dist[i] = -1
        return dist