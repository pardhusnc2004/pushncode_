'''
    GeeksforGeeks Daily Question (07-04-2025)
    Directed Graph Cycle
    Python3 solution
'''

#User function Template for python3
from collections import defaultdict
class Solution:
    def isCycle(self, V, edges):
        # code here
        indeg = [0]*V
        adj = defaultdict(list)
        for i, j in edges:
            indeg[j] += 1
            adj[i].append(j)
        topo = []
        q = []
        for i in range(V):
            if indeg[i] == 0:
                q.append(i)
        while(q):
            node = q.pop(0)
            topo.append(node)
            for it in adj[node]:
                indeg[it] -= 1
                if indeg[it] == 0:
                    q.append(it)
        return len(topo) != V