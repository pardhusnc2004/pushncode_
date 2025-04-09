'''
    GeeksforGeeks Daily Question (09-04-2025)
    Articulation Point - II
    Python3 solution
'''

class Solution:
    def articulationPoints(self, V, edges):
        # code here
        adjList = [[] for _ in range(V)]
        low, tin = [0]*V, [0]*V
        timer = 1
        for i, j in edges:
            adjList[i].append(j)
            adjList[j].append(i)
        
        def dfs(node, parent):
            nonlocal timer
            child = 0
            low[node], tin[node] = timer, timer
            timer += 1
            for adjNode in adjList[node]:
                if not low[adjNode]:
                    child += 1
                    dfs(adjNode, node)
                    low[node] = min(low[node], low[adjNode])
                    if parent != -1 and low[adjNode] >= tin[node]:
                        res.add(node)
                elif parent != adjNode:
                    low[node] = min(low[node], low[adjNode])
            if parent == -1 and child > 1:
                res.add(node)
            return
        
        res = set()
        for i in range(V):
            if not low[i]:
                dfs(i, -1)
        return list(res) if res else [-1]