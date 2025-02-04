'''
    GeeksforGeeks Daily Question (04-02-2025)
    Diameter of a Binary Tree
    Python3 solution
'''

class Node:

    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
        
class Solution:
    def diameter(self, root):
        # Your code here
        res = [0]
        def go(root):
            if not root:
                return 0
            lm, rm = go(root.left), go(root.right)
            res[0] = max(res[0], lm+rm+1)
            return 1+max(lm, rm)
        go(root)
        return res[0]-1