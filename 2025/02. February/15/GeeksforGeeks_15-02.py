'''
    GeeksforGeeks Daily Question (15-02-2025)
    Lowest Common Ancestor in a BST
    Python3 solution
'''

class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

class Solution:
    def LCA(self, root, n1, n2):
        if not root:
            return root
        if root.data >= min(n1.data, n2.data) and root.data <= max(n1.data, n2.data):
            return root
        elif root.data < min(n1.data, n2.data):
            return self.LCA(root.right, n1, n2)
        elif root.data > max(n1.data, n2.data):
            return self.LCA(root.left, n1, n2)
        
    

