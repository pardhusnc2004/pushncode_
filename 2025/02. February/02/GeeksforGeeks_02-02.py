'''
    GeeksforGeeks Daily Question (02-02-2025)
    Level order traversal
    Python3 solution
'''

class Node:
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None

class Solution:
    def levelOrder(self, root):
        # Your code here
        res = []
        q = [root]
        while q:
            sz = len(q)
            tmp = []
            for i in range(sz):
                node = q.pop(0)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                tmp.append(node.data)
            res.append(tmp)
        return res