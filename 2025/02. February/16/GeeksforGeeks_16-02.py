'''
    GeeksforGeeks Daily Question (16-02-2025)
    Serialize and deserialize a binary tree
    Python3 solution
'''

class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None

class Solution:
    #Function to serialize a tree and return a list containing nodes of tree.
    def serialize(self, root):
        inor = []
        def inorder(root):
            if root == None:
                return 
            inorder(root.left)
            inor.append(root)
            inorder(root.right)
        inorder(root)
        preor = []
        def preorder(root):
            if root == None:
                return 
            preor.append(root)
            preorder(root.left)
            preorder(root.right)
        preorder(root)
        
        return [inor, preor]

    
    #Function to deserialize a list and construct the tree.   
    def deSerialize(self, a):
        #code here
        inorder_ = a[0]
        preorder = a[-1]
        def f(inor,preor):
            if len(inor):
                node = Node(preor[0].data)
                temp = inor.index(preor[0])
                preor.pop(0)
                node.left = f(inor[:temp],preor)
                node.right = f(inor[temp + 1:],preor)
                return node
            else:
                return None
        

        return f(inorder_,preorder)