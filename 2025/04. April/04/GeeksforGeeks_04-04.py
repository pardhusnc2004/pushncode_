'''
    GeeksforGeeks Daily Question (04-04-2025)
    Undirected Graph Cycle
    Python3 solution
'''

class Solution:
	def isCycle(self, V, edges):
		#Code here
		adj = [[] for _ in range(V)]
		for i, j in edges:
		    adj[i].append(j)
		    adj[j].append(i)
		vis = set()
		def helper(node, parent):
		    vis.add(node)
		    for adjNode in adj[node]:
		        if adjNode != parent:
		            if adjNode in vis:
		                return True
		            if helper(adjNode, node):
		                return True
		                
		    return False
		   
	    for i in range(V):
	        if i not in adj:
	            if helper(i, -1):
	                return True
	    return False