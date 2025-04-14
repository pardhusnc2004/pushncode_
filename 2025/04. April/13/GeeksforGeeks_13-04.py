'''
    GeeksforGeeks Daily Question (13-04-2025)
    Clone an Undirected Graph
    Python3 solution
'''

#User function Template for python3

class Node:
    def __init__(self, val = 0, neighbors = []):
        self.val = val
        self.neighbors = neighbors

class Solution():
    def cloneGraph(self, node):
        #code here
        nodeMap = {}
        
        def go(node):
            nodeMap[node] = Node(node.val)
            for child in node.neighbors:
                if child not in nodeMap:
                    go(child)
            
        go(node)
        vis = set()
        
        def goMap(node):
            vis.add(node.val)
            for child in node.neighbors:
                nodeMap[node].neighbors.append(nodeMap[child])
                if child.val not in vis:
                    goMap(child)
        
        goMap(node)
        return nodeMap[node]