'''
    GeeksforGeeks Daily Question (08-02-2025)
    Tree Boundary Traversal
    Python3 solution
'''

class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
        
class Solution:
    def boundaryTraversal(self, root):
        # Code here
        if not root:
            return []
            
        if not root.left and not root.right:
            return [root.data]
            
        leaves, leftB, rightB = [], [], []
        def getLeaves(root):
            if not root:
                return
            if not root.left and not root.right:
                leaves.append(root.data)
            getLeaves(root.left)
            getLeaves(root.right)
            return
        def getLeftB(root):
            tmp = root.left
            while tmp:
                if tmp and (tmp.left or tmp.right):
                    leftB.append(tmp.data)
                if tmp.left:
                    tmp = tmp.left
                elif tmp.right:
                    tmp = tmp.right
                else:
                    break
        def getRightB(root):
            tmp = root.right
            while tmp:
                if tmp and (tmp.left or tmp.right):
                    rightB.append(tmp.data)
                if tmp.right:
                    tmp = tmp.right
                elif tmp.left:
                    tmp = tmp.left
                else:
                    break
            
        getLeaves(root)
        getLeftB(root)
        getRightB(root)
        rightB.reverse()
        # print(leftB, leaves, rightB)
        return [root.data] + leftB + leaves + rightB