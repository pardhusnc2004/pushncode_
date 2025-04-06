'''
    GeeksforGeeks Daily Question (06-04-2025)
    Topological sort
    Python3 solution
'''

class Solution:
    
    def topoSort(self, V, edges):
        # Code here 
        indegree = [0]*V
        adjList = [[] for _ in range(V)]
        for i, j in edges:
            adjList[i].append(j)
            indegree[j] += 1
            
        q = []
        for i in range(V):
            if indegree[i] == 0:
                q.append(i)
    
        res = []
        while q:
            node = q.pop(0)
            res.append(node)
            for adjNode in adjList[node]:
                indegree[adjNode] -= 1
                if not indegree[adjNode]:
                    q.append(adjNode)
        
        if len(res) == V:
            return res