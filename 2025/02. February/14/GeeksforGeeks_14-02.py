'''
    GeeksforGeeks Daily Question (14-02-2025)
    Fixing Two nodes of a BST
    Python3 solution
'''

class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

class Solution:
    def correctBST(self, root):
        # your code here
        wn1, wn2 = None, None
        def inorder(root):
            if root:
                inorder(root.left)
                ino.append(root)
                inorder(root.right)
                
        ino = []
        inorder(root)
        # print([i.data for i in inorder])
        first, second = None, None
        n = len(ino)
        for i in range(n-1):
            if ino[i].data > ino[i+1].data:
                first = ino[i]
                break
        for i in range(n-1, 0, -1):
            if ino[i].data < ino[i-1].data:
                second = ino[i]
                break
        first.data, second.data = second.data, first.data