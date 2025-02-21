'''
    Leetcode Daily Question (21-02-2025)
    1261. Find Elements in a Contaminated Binary Tree
    Python3 solution
'''
from typing import *
from collections import *
from bisect import *
from math import *
from heapq import *

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.Map = {}
        if root:
            root.val = 0
            self.buildTree(root)
        
    def buildTree(self, root):
        if root:
            self.Map[root.val] = 1
            if root.left:
                root.left.val = root.val*2+1
            if root.right:
                root.right.val = root.val*2+2
            self.buildTree(root.left)
            self.buildTree(root.right)

    def find(self, target: int) -> bool:
        return target in self.Map