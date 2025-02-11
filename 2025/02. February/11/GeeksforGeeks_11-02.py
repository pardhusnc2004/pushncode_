'''
    GeeksforGeeks Daily Question (11-02-2025)
    Check for BST
    Python3 solution
'''

class Solution:
    
    #Function to check whether a Binary Tree is BST or not.
    def isBST(self, root):
        #code here
        def ino(root):
            if root:
                ino(root.left)
                inorder.append(root.data)
                ino(root.right)
        inorder = []
        ino(root)
        if sorted(inorder) == inorder:
            for i in range(len(inorder)-1):
                if inorder[i+1] <= inorder[i]:
                    return False
            return True
        return False
