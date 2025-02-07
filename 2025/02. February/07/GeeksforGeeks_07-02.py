'''
    GeeksforGeeks Daily Question (07-02-2025)
    Inorder Traversal
    Python3 solution
'''

# Node Class:
class Node:
    def init(self,val):
        self.data = val
        self.left = None
        self.right = None

class Solution:
    def inOrder(self,root):
        # code here
        res = []
        
        def ino(root):
            if root:
                ino(root.left)
                res.append(root.data)
                ino(root.right)
        ino(root)
        return res