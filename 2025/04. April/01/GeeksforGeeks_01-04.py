'''
    GeeksforGeeks Daily Question (01-04-2025)
    DFS of Graph
    Python3 solution
'''

class Solution:
    
    #Function to return a list containing the DFS traversal of the graph.
    def dfs(self, adj):
        # code here
        vis = set()
        res = []
        n = len(adj)
        
        def helper(curNode):
            vis.add(curNode)
            res.append(curNode)
            for adjNode in adj[curNode]:
                if adjNode not in vis:
                    helper(adjNode)
            return
        
        helper(0)
        return res
