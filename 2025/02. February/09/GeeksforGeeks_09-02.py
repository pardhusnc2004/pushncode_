'''
    GeeksforGeeks Daily Question (09-02-2025)
    Maximum path sum from any nod
    Python3 solution
'''

class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None

from math import inf

class Solution:
    #Function to return maximum path sum from any node in a tree.
    def findMaxSum(self, root): 
        #Your code here
        res = -inf
        def go(root):
            nonlocal res
            if not root:
                return -inf
            l, r = max(0, go(root.left)), max(0, go(root.right))
            res = max(res, root.data + l + r)
            return max(l, r)+root.data
        go(root)
        return res