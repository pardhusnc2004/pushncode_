'''
    GeeksforGeeks Daily Question (12-02-2025)
    k-th Smallest in BST
    Python3 solution
'''

class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

class Solution:
    # Return the kth smallest element in the given BST 
    def kthSmallest(self, root, k): 
        #code here.
        inorder = []
        def ino(root):
            if root:
                ino(root.left)
                inorder.append(root.data)
                ino(root.right)
        ino(root)
        if len(inorder) < k:
            return -1
        return inorder[k-1]
        