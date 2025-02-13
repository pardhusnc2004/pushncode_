'''
    GeeksforGeeks Daily Question (13-02-2025)
    Pair Sum in BST
    Python3 solution
'''

# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

class Solution:
    def findTarget(self, root, target): 
        # your code here.
        def go(root, d):
            if root:
                if root.data in d:
                    return True
                d[target-root.data] = 1
                if go(root.left, d) or go(root.right, d):
                    return True
                return False
            return False
        return go(root, {})