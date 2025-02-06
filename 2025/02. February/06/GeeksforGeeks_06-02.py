'''
    GeeksforGeeks Daily Question (06-02-2025)
    Construct Tree from Inorder & Preorder
    Python3 solution
'''

# Node class
class Node:
    def __init__(self,val):
        self.data = val
        self.right = None
        self.left = None

# Note: Build tree and return root node
class Solution:
    def buildTree(self, inorder, preorder):
        # code here
        inMap = {}
        for i in range(len(inorder)):
            inMap[inorder[i]] = i
            
        def construct(il, ir, pl, pr):
            if il > il or pl > pr:
                return None
            el = preorder[pl]
            elIndex = inMap[el]
            tmp = elIndex-il
            
            node = Node(el)
            node.left = construct(il, elIndex-1, pl+1, pl+tmp)
            node.right = construct(elIndex+1, ir, pl+tmp+1, pr)
            return node
            
        return construct(0, len(inorder)-1, 0, len(preorder)-1)