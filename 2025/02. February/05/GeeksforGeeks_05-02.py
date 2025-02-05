'''
    GeeksforGeeks Daily Question (05-02-2025)
    Mirror Tree
    Python3 solution
'''

class Node:
    def _init_(self, val):
        self.right = None
        self.data = val
        self.left = None
# your task is to complete this function

class Solution:
    #Function to convert a binary tree into its mirror tree.
    def mirror(self, root):
        # Code here
        if not root:
            return root
        tmp = root.right
        root.right = self.mirror(root.left)
        root.left = self.mirror(tmp)
        return root
