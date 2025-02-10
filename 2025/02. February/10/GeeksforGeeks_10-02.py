'''
    GeeksforGeeks Daily Question (10-02-2025)
    K Sum Paths
    Python3 solution
'''

class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

class Solution:
    def sumK(self,root,k):
        # code here
        res = [0]
        def go(root, rem):
            nonlocal res
            if not root:
                return
            rem += root.data
            if rem == k:
                res[0] += 1
            go(root.left, rem)
            go(root.right, rem)
            return
        def dfs(root):
            if not root:
                return
            go(root, 0)
            dfs(root.left)
            dfs(root.right)
            return
        if not root:
            return 0
        dfs(root)
        return res[0]