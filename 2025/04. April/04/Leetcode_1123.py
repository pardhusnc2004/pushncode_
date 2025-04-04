'''
    Leetcode Daily Question (04-04-2025)
    1123. Lowest Common Ancestor of Deepest Leaves
    Python3 solution
'''
from typing import List, Optional
from collections import *
from bisect import *
from math import *
from heapq import *

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self.res = None
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root or (not root.right and not root.left):
            return root
        deepestLeaves = defaultdict(set)
        q = deque([root])
        lvl = 0
        while q:
            sz = len(q)
            for i in range(sz):
                node = q.popleft()
                deepestLeaves[lvl].add(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            lvl += 1
        deepestLvl = max(deepestLeaves)
        if len(deepestLeaves[deepestLvl]) == 1:
            return self.find(root, deepestLeaves[deepestLvl])
        self.helper(root, deepestLeaves[deepestLvl])
        return self.res

    def find(self, root, val):
        if not root:
            return None
        if root.val in val:
            # print("FOUND")
            return root
        left, right = self.find(root.left, val), self.find(root.right, val)
        if left:
            return left
        return right

    def helper(self, root, deepestLeaves):
        if not root:
            return 0
        if root.val in deepestLeaves:
            return 1
        left, right = self.helper(root.left, deepestLeaves), self.helper(root.right, deepestLeaves)
        # print(root.val, left, right)
        if left+right == len(deepestLeaves):
            self.res = root
            return 1
        return left+right