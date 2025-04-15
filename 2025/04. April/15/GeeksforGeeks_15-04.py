'''
    GeeksforGeeks Daily Question (15-04-2025)
    Bellman-Ford
    Python3 solution
'''

#User function Template for python3

class Solution:
    def bellmanFord(self, V, edges, src):
        #code here
        inf = 10**8
        dist = [inf]*V
        dist[src] = 0
        for i in range(V-1):
            for u, v, w in edges:
                if dist[u] != inf and dist[v] > dist[u]+w:
                    dist[v] = w+dist[u]
        for u, v, w in edges:
            if dist[u] != inf and dist[v] > dist[u]+w:
                return [-1]
        return dist