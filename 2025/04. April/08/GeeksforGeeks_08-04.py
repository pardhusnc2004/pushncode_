'''
    GeeksforGeeks Daily Question (08-04-2025)
    Bridge edge in a graph
    Python3 solution
'''

class Solution:
    def isBridge(self, V, edges, c, d):
        adj = [[] for _ in range(V)]
        for u,v in edges:
            if (u==c and v==d) or (u==d and v==c):
                continue
            adj[u].append(v)
            adj[v].append(u)
        
        vis = set()
        
        def dfs(start):
            vis.add(start)
            for neigh in adj[start]:
                if neigh not in vis:
                    dfs(neigh)
        dfs(c)
        return d not in vis