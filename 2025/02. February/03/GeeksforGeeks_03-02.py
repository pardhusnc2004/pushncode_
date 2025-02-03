'''
    GeeksforGeeks Daily Question (03-03-2025)
    Height of Binary Tree
    Python3 solution
'''

# Node Class:
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None

class Solution:
    #Function to find the height of a binary tree.
    def height(self, root):
        # code here
        if not root:
            return -1
        lm, rm = self.height(root.left), self.height(root.right)
        return 1+max(lm, rm)