'''
    Leetcode Daily Question (23-02-2025)
    889. Construct Binary Tree from Preorder and Postorder Traversal
    Python3 solution
'''
from typing import *
from collections import *
from bisect import *
from math import *
from heapq import *

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        n = len(preorder)
        postMap = {postorder[i]:i for i in range(n)}

        def goConstruct(preLeft, preRight, postLeft, postRight):
            if preLeft > preRight:
                return None
            if preLeft == preRight:
                return TreeNode(preorder[preLeft])
            curNode = TreeNode(preorder[preLeft])
            postorderIndex = postMap[preorder[preLeft+1]]
            nodes = postorderIndex - postLeft + 1
            curNode.left = goConstruct(preLeft+1, preLeft+nodes, postLeft, postorderIndex)
            curNode.right = goConstruct(preLeft+nodes+1, preRight, postorderIndex+1, postRight)
            return curNode
        
        return goConstruct(0, n-1, 0, n-1)