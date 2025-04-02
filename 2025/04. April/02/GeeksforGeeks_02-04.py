'''
    GeeksforGeeks Daily Question (02-04-2025)
    BFS of graph    
    Python3 solution
'''

#User function Template for python3
class Solution:
    # Function to return Breadth First Search Traversal of given graph.
    def bfs(self, adj):
        # code here
        vis = set()
        n = len(adj)
        
        res = []
        
        for i in range(n):
            if i not in vis:
                vis.add(i)
                q = [i]
                while q:
                    node = q.pop(0)
                    res.append(node)
                    
                    for adjNode in adj[node]:
                        if adjNode not in vis:
                            vis.add(adjNode)
                            q.append(adjNode)
        
        return res